import tkinter
import tkinter.messagebox
import pickle 
import tkinter.ttk

# Body of creating window
root = tkinter.Tk()
root.title("To-Do List")

# Change root window background color
root.config(bg = "white")

# Create frame to hold list box task and scrollbar task
frame_task = tkinter.Frame(root)
frame_task.pack()


# Definition for add task
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)                                                        # .insert(position, string)
        entry_task.delete(0, tkinter.END)                                                             # To clear entry box once click/enter task 
    else:
        tkinter.messagebox.showwarning(title ="Warning!", message = "Please enter a task.")

# Definition for delete task
def delete_task():
    try :                                                                                             # Try this, if there is error, it does 'except'
        task_index = listbox_task.curselection()[0]                                                   # [0] to select one item at a time
        listbox_task.delete(task_index)
    except: 
        tkinter.messagebox.showwarning(title ="Warning!", message = "Please select a task.")

# Definition for save task
def save_task():
    task = listbox_task.get(0, listbox_task.size())
    pickle.dump(task, open("task_data", "wb"))                                                          # wb -> write binary, change from \ to / to save
                                                                                                        # file is saved to \Users\USER 
                                                                                                        # or preferred path can be replaced here
# Definition for load task
def load_task():
    task = pickle.load(open("task_data" , "rb"))                                                        # rb -> reading binary
    listbox_task.delete(0, tkinter.END)                                                         
    for task in task:
        listbox_task.insert(tkinter.END, task)

# Definition for edit task
def edit_task(): 
    if entry_task.get() == "":                                                                         # to select one task at a time to edit
        task_index = listbox_task.curselection()[0]                                                    # to get the selected index line
        task = listbox_task.get(task_index)
        entry_task.insert(0, task)
        listbox_task.delete(task_index)
    else:
        tkinter.messagebox.showwarning(title ="Warning!", message = "Please select only one task.")

# Definition to grey out a task as completed
def complete_task():
    task = listbox_task.get(0, listbox_task.size())
    listbox_task.itemconfig(
        listbox_task.curselection(),
        fg = "grey")
    listbox_task.selection_clear(0, tkinter.END)                                                        # remove the highlight bar when click complete task

# To undo they grey out task
def undocomplete_task():
    task = listbox_task.get(0, listbox_task.size())
    listbox_task.itemconfig(listbox_task.curselection(), fg = "black")
    listbox_task.selection_clear(0, tkinter.END)

# To delete all completed/grey tasks
def deletecompleted_task():
    count = 0
    while count < listbox_task.size():
        if listbox_task.itemcget(count, "fg") == "grey":
            listbox_task.delete(listbox_task.index(count))
        else: 
            count += 1

# Create key binding for add task 
def key_handler(event):
    add_task()   

# Create binding double click to edit task
def double_click(event):
    edit_task()   

# Create GUI, height 7 rows
listbox_task = tkinter.Listbox(frame_task, height = 7, width = 60, highlightthickness = 0, selectbackground = "#a6a6a6", activestyle = "none")
listbox_task.pack(side = tkinter.LEFT)

# Add scroll bar
scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side = tkinter.RIGHT, fill = tkinter.Y)

# Make scrollbar functioning
listbox_task.config(yscrollcommand = scrollbar_task.set)
scrollbar_task.config(command = listbox_task.yview)

# Add entry task
entry_task = tkinter.Entry(root, width = 60)
entry_task.pack()

# Add button add task
button_add_task = tkinter.Button(root, text = "Add Task", width = 20, command = add_task, bg = "peachpuff")
root.bind("<Return>", key_handler)                                                                         # bind(event, action)
button_add_task.pack()

# Add button delete task
button_delete_task = tkinter.Button(root, text = "Delete Task", width = 20, command = delete_task, bg = "white")
button_delete_task.pack()

# Add button load task
button_load_task = tkinter.Button(root, text = "Load Task", width = 20, command = load_task, bg = "white")
button_load_task.pack()

# Add button save task
button_save_task = tkinter.Button(root, text = "Save Task", width = 20, command = save_task, bg = "white")
button_save_task.pack()

# Add edit task
button_edit_task = tkinter.Button(root, text = "Edit Task", width = 20, command = edit_task, bg = "white")
root.bind("<Double-1>", double_click)
button_edit_task.pack()

# Add cross task
button_complete_task = tkinter.Button(root, text = "Complete Task", width = 20, command = complete_task, bg = "white")
button_complete_task.pack()

# Add cross task
button_undocomplete_task = tkinter.Button(root, text = "Undo Complete Task", width = 20, command = undocomplete_task, bg = "white")
button_undocomplete_task.pack()

# Add button delete task
button_deletecompleted_task = tkinter.Button(root, text = "Delete Completed Task", width = 20, command = deletecompleted_task, bg = "white")
button_deletecompleted_task.pack()

# Start the main events loop
root.mainloop()
