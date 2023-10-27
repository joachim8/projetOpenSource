# la classe TaskManager
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    # ajout de l'une tâche
    def add_task(self, description):
        self.tasks.append(description)
        print("Tâche ajoutée avec succes.")
    
    #affichage list des tâches existantes
    def list_tasks(self):
        if not self.tasks:
            print("Aucune tâche enregistrée.")
        else:
            print("Liste des tâches à faire:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    
    #complétion d'une tâche (suppression)
    def mark_task_completed(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks.pop(task_num - 1)
            print("Tâche marquée comme terminée avec succes.")
        else:
            print("Numéro de la tâche invalide.")
    
    #affichage menu en console & interaction avec l'utilisateur
    def run(self):
        while True:
            print("\nBienvenue dans le Gestionnaire de Tâches en python.")
            print("Sélectionnez une option :")
            print("1. Ajouter une tâche")
            print("2. Afficher les tâches")
            print("3. Marquer une tâche comme terminée")
            print("4. Quitter")
            
            option = input("Entrez le numéro de l'option : ")
            
            if option == '1':
                description = input("Entrez la description de la tâche : ")
                self.add_task(description)
            elif option == '2':
                self.list_tasks()
            elif option == '3':
                if len(self.tasks) < 1:
                    print("Aucune tâche en cours")
                else:
                    task_num = int(input("Entrez le numero de la tache a marquer comme terminee : "))
                    self.mark_task_completed(task_num)
            elif option == '4':
                break
            else:
                print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()



