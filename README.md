# Comparaison des performances : Python vs C++ pour une tâche de taille = 1000

## **Résultats en Python**
**Méthode** : `numpy.linalg.solve` de Python.

### Temps d'exécution :
- **0.030459381 secondes**
- **0.031772915 secondes**
- **0.030362346 secondes**
- **0.032150176 secondes**
- **0.032449290 secondes**

### **Temps moyen d'exécution** : **0.03143882159 secondes**

---

## **Résultats en C++**

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
| C++ (`LLT`)                    | **0.004925552**                |
| Python (`numpy.linalg.solve`)  | **0.03143882159**              |
| C++ (`LDLT`)                   | **0.05610112**                 |
| C++ (`ColPivHouseholderQr`)    | **0.4889314**                  |


### Conclusion :
La méthode **LLT** (C++) est plus rapide que la méthode Python `numpy.linalg.solve`, mais la méthode Python reste plus performante que la méthode **LDLT** (C++) et bien plus rapide que la méthode **ColPivHouseholderQr** (C++) qui est la plus lente des trois.

On peut donc conclure que les méthodes C++ ne sont pas toujours plus rapides que les méthodes Python.
