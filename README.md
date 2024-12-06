# Comparaison des performances : Python vs C++ pour une tâche de taille = 1000

Ce document présente les métriques de performance pour résoudre une tâche de calcul impliquant la résolution d'un système d'équations linéaires de taille 1000, en utilisant Python et C++.

---

## **Résultats en Python**
**Méthode** : `numpy.linalg.solve` de Python.

### Temps d'exécution :
- Tâche 1 : **0.030459381 secondes**
- Tâche 2 : **0.031772915 secondes**
- Tâche 3 : **0.030362346 secondes**
- Tâche 4 : **0.032150176 secondes**
- Tâche 5 : **0.032449290 secondes**

### **Temps moyen d'exécution** : **0.03143882159 secondes**

---

## **Résultats en C++**
Les tâches ont été résolues en utilisant trois méthodes : **ColPivHouseholderQr**, **LLT** et **LDLT**, en utilisant la bibliothèque Eigen.

### **1. ColPivHouseholderQr**
**Temps d'exécution** :
- **0.492553 secondes**
- **0.469289 secondes**
- **0.478498 secondes**
- **0.522793 secondes**
- **0.481524 secondes**

**Temps moyen d'exécution** : **0.4889314 secondes**

---

### **2. LLT (Décomposition de Cholesky)**
**Temps d'exécution** :
- **0.00418424 secondes**
- **0.00570986 secondes**
- **0.00366202 secondes**
- **0.00674121 secondes**
- **0.00433043 secondes**

**Temps moyen d'exécution** : **0.004925552 secondes**

---

### **3. LDLT (Décomposition de Cholesky)**
**Temps d'exécution** :
- **0.0507618 secondes**
- **0.0637664 secondes**
- **0.0502109 secondes**
- **0.0627403 secondes**
- **0.0530262 secondes**

**Temps moyen d'exécution** : **0.05610112 secondes**

---

## **Résumé**

| **Méthode**                    | **Temps moyen d'exécution (s)** |
|---------------------------------|--------------------------------|
| Python (`numpy.linalg.solve`)  | **0.03143882159**              |
| C++ (`ColPivHouseholderQr`)    | **0.4889314**                  |
| C++ (`LLT`)                    | **0.004925552**                |
| C++ (`LDLT`)                   | **0.05610112**                 |

### Points clés à noter :
- La méthode **LLT** (C++) surperforme les autres méthodes, démontrant la puissance des techniques de décomposition matricielle spécialisées dans Eigen.
- La méthode **ColPivHouseholderQr** (C++) est plus lente que la méthode `numpy.linalg.solve` en Python pour cette taille de tâche.
- La méthode **LDLT** (C++) montre des performances modérées, meilleure que **ColPivHouseholderQr**, mais plus lente que **LLT**.
