#include <Eigen/Dense>
#include <chrono>
#include <cpr/cpr.h>
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {

  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/"});

  json data = json::parse(r.text);

  std::vector<std::vector<double>> a =
      data["a"].get<std::vector<std::vector<double>>>();
  std::vector<double> b = data["b"].get<std::vector<double>>();
  int id = data["id"].get<int>();

  if (a.size() != a[0].size() || a.size() != b.size()) {
    std::cerr << "Erreur : Dimensions incompatibles pour la résolution."
              << std::endl;
    return 1;
  }

  Eigen::MatrixXd A(a.size(), a[0].size());
  Eigen::VectorXd B(b.size());

  for (size_t i = 0; i < a.size(); ++i) {
    for (size_t j = 0; j < a[0].size(); ++j) {
      A(i, j) = a[i][j];
    }
    B(i) = b[i];
  }

  auto start = std::chrono::high_resolution_clock::now();

  Eigen::VectorXd X = A.ldlt().solve(B);

  auto end = std::chrono::high_resolution_clock::now();
  std::chrono::duration<double> t_duration = end - start;

  std::cout << "Temps de calcul : " << t_duration.count() << " secondes"
            << std::endl;

  json result;
  result["a"] = a;
  result["b"] = b;
  result["x"] = std::vector<double>(
      X.data(),
      X.data() + X.size()); // Convertir Eigen::VectorXd en std::vector<double>
  result["time"] = t_duration.count();
  result["id"] = id;

  // Envoyer les données avec une requête POST
  cpr::Response post_response =
      cpr::Post(cpr::Url{"http://localhost:8000/"},
                cpr::Header{{"Content-Type", "application/json"}},
                cpr::Body{result.dump()});

  // Vérification de la réponse du POST
  std::cout << "POST Status Code: " << post_response.status_code << std::endl;
  std::cout << "POST Response Text: " << post_response.text << std::endl;

  return 0;
}
