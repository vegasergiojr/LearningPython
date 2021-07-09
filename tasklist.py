task_list = [] #global list

while True:
    print(
        """
        1 - add task
        2 - delete task
        3 - look at tasks
        q - to quit """
    )

    option = int(input("Please enter a choice from menu: "))

    if option == "q":
        break
    elif option == 1:
        title = input("please enter a title for task: ")
        priority = input("please enter level priority: high, medium, low: ")
        task = {"title" : title, "priority" : priority}
        task_list.append(task)
    elif option == 2:
        title = input("please enter the title you wish to remove: ")
        task = {"title" : title, "priority" : priority}
        task_list.remove(task)
    elif option == 3:
        for list in task_list:
                print(list.get("title"), list.get("priority"))
        for list in task_list:
                print("-" + " " + list.get("title"), "-" + " " + list.get("priority"))
        
        
