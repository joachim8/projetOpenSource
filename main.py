# la classe TaskManager
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    # ajout de l'une tache
    def add_task(self, description):
        self.tasks.append(description)
        print("Tache ajoutee avec succes.")
    
    #affichage list des taches existantes
    def list_tasks(self):
        if not self.tasks:
            print("Aucune tache enregistree.")
        else:
            print("Liste des taches a faire:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    
    #completion d'une tache (suppression)
    def mark_task_completed(self, task_num):
        if 1 <= task_num <= len(self.tasks):
            self.tasks.pop(task_num - 1)
            print("Tache marquee comme terminee avec succes.")
        else:
            print("Numero de tache invalide.")
    
    #affichage menu en console & interaction avec l'utilisateur
    def run(self):
        while True:
            print("\nBienvenue dans le Gestionnaire de Taches en python.")
            print("Selectionnez une option :")
            print("1. Ajouter une tache")
            print("2. Afficher les taches")
            print("3. Marquer une tache comme terminee")
            print("4. Quitter")
            
            option = input("Entrez le numero de l'option : ")
            
            if option == '1':
                description = input("Entrez la description de la tache : ")
                self.add_task(description)
            elif option == '2':
                self.list_tasks()
            elif option == '3':
                task_num = int(input("Entrez le numero de la tache a marquer comme terminee : "))
                self.mark_task_completed(task_num)
            elif option == '4':
                break
            else:
                print("Option invalide. Veuillez reessayer.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()



