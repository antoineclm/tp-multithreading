import queue_mc as q
from task import Task
import time

# Initialisation du client de file d'attente
qc = q.QueueClient()

# Générateur de tâches
task_id = 1  # Compteur pour générer des identifiants de tâches
task_result = Task()
while True:
    # Création et ajout d'une nouvelle tâche toutes les secondes
    new_task = Task(task_id, 1000)  # Exemple de tâche avec ID et paramètre
    qc.taskQueue.put(new_task)
    print(f"Tâche ajoutée à la file d'attente :  {new_task.identifier}")
    task_id += 1

    # Récupération des résultats
    try:
        while not qc.resultQueue.empty():
            task_result = qc.resultQueue.get()
            print(f"Tache récupéré : {task_result.identifier} en  {task_result.time} s")
    except Exception as e:
        print(f"Erreur lors de la récupération des résultats : {e}")

    # Pause d'une seconde avant de poster une nouvelle tâche
    time.sleep(1)
