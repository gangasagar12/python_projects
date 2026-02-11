
def task():
    tasks= []  # empty list
    print(" ==========Welcome to the task management app=====")
    

total_task=int(input("enter how many task you want to add="))   #5
for i in range(1,total_task+1):
    task_name=input("enter task{i}=") # enter task 3
    tasks.append(task_name)

print(f"Todays tasks are \n {tasks}")

while True:
    operation=int(input("enter 1- Add \n2-Update\n3 -delete\n4-view\n5 -Exit/stop"))
    if operation==1:
        add=input("enter the task  you want to add :")
        tasks.append(add)
        print("task{add} has been sucessfully added ....")

    elif operation==2:
        update_val=input("enter the task name you want to update=")
        if update_val in tasks:
            up=input("enter new tasks=")
            ind=tasks.index(update_val)
            tasks[ind]=up
            print(f"updated task{up}")

    elif operation==3:
        del_val=input("which task you want to delete =")
        if del_val in tasks:
            ind=tasks.index(del_val)
            del tasks[ind]
            print(f"task {del_val} has been deleted:")

    elif operation==4:
        print(f"total trasks={tasks}")

    elif operation==5:
        print("closing the program...")
        break
    else:
        print("invilid inpits")