#* Imports
import tkinter as tk
from tkinter import messagebox as msg

#* Variables
todo, doing, done = [], [], []
popUp = object()

#* Functions
def fillAll():
    toDoList.delete(0, tk.END)
    doingList.delete(0, tk.END)
    doneList.delete(0, tk.END)
    for el in todo:
        toDoList.insert(tk.END, el)
    for el in doing:
        doingList.insert(tk.END, el)
    for el in done:
        doneList.insert(tk.END, el)

def newTask():
    global popUp
    #* Pop Up Window
    popUp = tk.Toplevel(app)
    popUp.grab_set()

    newTaskLabel = tk.Label(popUp, text='Enter Task')
    newTaskLabel.grid(row=0, column=1, pady=5)

    newTaskVar = tk.StringVar()
    newTaskEntry = tk.Entry(popUp, textvariable=newTaskVar)
    newTaskEntry.grid(row=1,column=0, columnspan=3)

    listTypeVar = tk.IntVar(popUp, 1)
    toDoRadio = tk.Radiobutton(popUp, text='To Do', variable=listTypeVar, value=1)
    toDoRadio.grid(row=2, column=0, padx=5, pady=5)
    doingRadio = tk.Radiobutton(popUp, text='Doing', variable=listTypeVar, value=2)
    doingRadio.grid(row=2, column=1, padx=5, pady=5)
    doneRadio = tk.Radiobutton(popUp, text='Done', variable=listTypeVar, value=3)
    doneRadio.grid(row=2, column=2, padx=5, pady=5)

    createTaskButton = tk.Button(
        popUp,
        text='Create Task', 
        command=lambda: createTask(newTaskVar.get(), listTypeVar.get())
    )
    createTaskButton.grid(row=3, column=1, pady=5)

    popUp.mainloop()

def createTask(value, listType):
    if not len(value):
        msg.showerror('Empty Task', 'Task cannot be empty.')
        return
    global popUp
    if listType is 1:
        todo.append(value)
    elif listType is 2:
        doing.append(value)
    else:
        done.append(value)

    fillAll()
    popUp.destroy()


def viewTask(value, listType):
    global popUp
    #* Pop Up Window
    popUp = tk.Toplevel(app)
    popUp.grab_set()

    viewTaskLabel = tk.Label(popUp, text='Update Task')
    viewTaskLabel.grid(row=0, column=1, pady=5)

    viewTaskVar = tk.StringVar(popUp, value)
    viewTaskEntry = tk.Entry(popUp, textvariable=viewTaskVar)
    viewTaskEntry.grid(row=1,column=0, columnspan=3, padx=5, pady=5)

    updateTaskButton = tk.Button(popUp, 
        text='Update', 
        command=lambda: updateTask(viewTaskVar.get(), listType)
    )
    updateTaskButton.grid(row=2, column=1, pady=5)


    popUp.mainloop()

def updateTask(value, listType):
    global popUp
    if listType is 1:
        todo[toDoList.curselection()[0]] = value
    elif listType is 2:
        doing[doingList.curselection()[0]] = value
    elif listType is 3:
        done[doneList.curselection()[0]] = value
    
    fillAll()
    popUp.destroy()

def moveUpToDoing():
    index = toDoList.curselection()[0]
    doing.append(todo[index])
    del todo[index]
    fillAll()

def moveToDo():
    index = doingList.curselection()[0]
    todo.append(doing[index])
    del doing[index]
    fillAll()

def moveToDone():
    index = doingList.curselection()[0]
    done.append(doing[index])
    del doing[index]
    fillAll()

def moveDownToDoing():
    index = doneList.curselection()[0]
    doing.append(done[index])
    del done[index]
    fillAll()


#* GUI
app = tk.Tk()
app.title('Tasks Manager')


#* New Task
newTaskButton = tk.Button(app, text='New Task',command=newTask)
newTaskButton.grid(row=0, column=5, pady=10)

#* To Do
toDoLabel = tk.Label(app, text='To Do')
toDoLabel.grid(row=1, column=1)

toDoList = tk.Listbox(app, width=30, height=12)
toDoList.grid(row=2, column=0, columnspan=3, rowspan=4, padx=10, pady=10)

#? Widget Configuration
toDoList.config(exportselection=False)

#? Event Binding
toDoList.bind('<Double-1>', lambda event: viewTask(toDoList.get(toDoList.curselection()[0]), 1))

moveUpToDoingButton = tk.Button(app, text='Move to Doing', command=moveUpToDoing)
moveUpToDoingButton.grid(row=3, column=3)

#* Doing
doingLabel = tk.Label(app, text='Doing')
doingLabel.grid(row=1, column=5)

doingList = tk.Listbox(app, width=30, height=12)
doingList.grid(row=2, column=4, columnspan=3, rowspan=4, padx=10, pady=10)

moveToDoButton = tk.Button(app, text='Move to To Do', command=moveToDo)
moveToDoButton.grid(row=4, column=3)

moveToDoneButton = tk.Button(app, text='Move to Done', command=moveToDone)
moveToDoneButton.grid(row=3, column=7)

#* Done
doneLabel = tk.Label(app, text='Done')
doneLabel.grid(row=1, column=9)

doneList = tk.Listbox(app, width=30, height=12)
doneList.grid(row=2, column=8, columnspan=3, rowspan=4, padx=10, pady=10)

moveDownToDoingButton = tk.Button(app, text='Move to Doing', command=moveDownToDoing)
moveDownToDoingButton.grid(row=4, column=7)


app.mainloop()