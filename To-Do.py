def mainMenu():

    while True:
        print()
        print('''

        ### TO-DO LIST ###
            
            Select a number for the action that you would like to do. 
            1. View To-Do list
            2. Add items to To-Do list
            3. Remove item from the To-Do list
            4. Check if item is in To-Do list
            5. How many items on To-Do list
            6. Clear To-Do list
            
        ''')
        # Ask user to make selection    
        selection = input("Please choose your selection")

        # Determine which action to perform based on user's selection
        if selection == '1':
            show_list()
        elif selection == '2':
            add_item()
        elif selection == '3':
            remove_item()
        elif selection == '4':
            check_item()
        elif selection == '5':
            count_item()
        elif selection == '6':
            clear_list()
        else: 
            print("Please enter valid number")

# Example of given to-do list
todo_list = ["make to do list with python" , 
            "gather data and do completed/not completed graph"]

# To show all the items in the list
def show_list():

    print()
    print("--- TO-DO LIST---")
    print()
    for i in todo_list:
        print("- ", i)

# To add item to the list by the user
def add_item():
    
    item = input("Enter what's on your mind: ")
    todo_list.append(item)
    print('"' + item + '"' + " has been added to the to-do list")

# To remove item from the list as entered by the user
def remove_item():
    
    item = input("What to delete from your list? ")
    todo_list.remove(item)
    print('"' + item + '"' + " has been removed to the to-do list")

# To check and add the item as entered by the user
def check_item():

    item = input("What are you checking on?")
    if item in todo_list:
        print('"' + item + '"' + " is in your to-do list")
    else: 
        print("Do you want to add" + ' "' + item + '" ' + "to your to-do")
        answer = input("Yes/No")
        if answer.startswith('Y'):
            todo_list.append(item)
            print('"' + item + '"' + " has been added to the to-do list")
        
# To count how many items are there in the list
def count_item():
    print("There are", len(todo_list), " items on your to-do list")

# To clear out everything in the list
def clear_list():
    todo_list.clear()
    print("To-do list is now empty")

mainMenu()

import tkinter
import tkinter.messagebox

# Crete the window
root = tkinter.Tk()
root.title("Your To-Do List")

# Create GUI, height 3 rows
listbox_task = tkinter.Listbox(root, height = 3, width = 50)
listbox_task.pack()

# Add entry task
entry_task = tkinter.Entry(root, width = 50)
entry_task.pack()

# Add button
button_add_task = tkinter.Button(root, text = "Add task", width = 48, command = add_item)
button_add_task.pack()

root.mainloop()
