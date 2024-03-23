# A to-do list that shows priority
# Author: Osiro Asunde

import os
import time

toDoList = []
print("To Do List Manager:")


def prettyPrint():
    os.system("clear")
    print("Here is all you have to do today: ")
    print()
    for task in toDoList:
        for value in task:
            print(f"{value:^4}", end="|")
        print()


def prettyPrintPriority(priority):
    os.system("clear")
    print(f"Here is everything urgent you have to do today ({priority}): ")
    print()
    for task in toDoList:
        if task[2] == priority:
            for value in task:
                print(f"{value:^4}", end="|")
            print()


def add():
    os.system("clear")
    item = input("What do you want to add to the list?: \n> ")
    dueTime = input("When is it due by?: \n> ")
    priority = input("What is the priority? (High, Medium or Low): \n> ").strip().title()
    priorityList = ["High", "Medium", "Low"]

    if priority not in priorityList:
        print("Please enter a valid priority")
        time.sleep(1)
        return

    newTask = [item, dueTime, priority]

    if newTask not in toDoList:
        toDoList.append(newTask)
        print(f"{item} has been added to the list.")
    else:
        print(f"{item} already on the list before")
    time.sleep(1)


def edit():
    os.system("clear")
    prettyPrint()
    print("Please select the number of the item you want to edit")
    selectedItem = int(input("> ")) - 1

    if selectedItem in range(len(toDoList)):
        attributeToEdit = input("Enter the attribute to edit (name, time, priority): ").lower()
        newValue = input(f"Please type in the new {attributeToEdit}\n>>")
        indexToEdit = {"name": 0, "time": 1, "priority": 2}[attributeToEdit]
        toDoList[selectedItem][indexToEdit] = newValue
    else:
        print("Number chosen not on the list")
        choice = input("Press 1 to choose again or any other key to go back to the menu\n>>")
        if choice != "1":
            return
    time.sleep(1)


def remove():
    os.system("clear")
    prettyPrint()
    choice = int(input("Please select the number you would like to delete\n>>")) - 1

    if choice in range(len(toDoList)):
        listItem = toDoList[choice]
        confirmation = input(f"Are you sure you want to delete {listItem[0]}? (y/n)\n>>")

        if confirmation.lower() == "y":
            toDoList.remove(listItem)
            print(f"{listItem[0]} has been removed from the list")
        else:
            print("Item not removed")
    else:
        print("Invalid choice. Please select a valid number.")


def deleteAll():
    os.system("clear")
    toDoList.clear()
    print("The list has been cleared")
    time.sleep(1)


while True:
    print("1. View The List\n2. Add to the List\n3. Edit the List\n4. Remove from the List\n5. Delete All")
    choice = input(">>")

    if choice == "1":
        os.system("clear")
        kindOfView = input("1. View All\n2. View Priority\n>> ")

        if kindOfView == "1":
            prettyPrint()
        elif kindOfView == "2":
            priorityToView = input("Enter the priority to view (High, Medium, Low): ").strip().title()
            prettyPrintPriority(priorityToView)
        else:
            print("Invalid choice. Please select a valid option.")
            time.sleep(1)
            os.system("clear")

    elif choice == "2":
        add()
    elif choice == "3":
        edit()
    elif choice == "4":
        remove()
    elif choice == "5":
        deleteAll()
    else:
        print("Invalid Choice. Please select a valid number")
