def task():
    tasks=[] #empty list
    print("----Welcome to to do list----")
    total_task=int(input("Enter how many task you want to add:"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task {i}=")
        tasks.append(task_name)
    print(f"Today's tasks are\n{tasks}")
    
    while True:
        print("Enter 1 for Add,2 for Update,3 for Delete,4 for View,5 for Exit")
        operation=int(input("Enter your choice:"))
        if operation==1:
         add_task=input("Enter task you want to add=")
         tasks.append(add_task)
         print(f"Task {add_task} has been successfully added...")
         
        elif operation==2:
         updated_task=input("Enter the name of task you want to update:")
         if updated_task in tasks:
            new_task=input("Enter new task=")
            index=tasks.index(updated_task)
            tasks[index]=new_task
            print(f"updated task {new_task}")
            
        elif operation==3:
            delete_task=input("Which task you want to delete:")
            if delete_task in tasks:
                index=tasks.index(delete_task)
                del tasks[index]
                print(f"Task {delete_task} has been deleted...")
        
        elif operation==4:
            print(f"Total tasks={tasks}") 
        
        elif operation==5:
            print("Closing the program...")
            break
        
        else:
            print("Invalid input")
                 
task()           