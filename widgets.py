import tkinter as tk

app = tk.Tk()
leftFrame = tk.Frame(app, borderwidth=1, relief=tk.SOLID)
leftFrame.pack(side=tk.LEFT, padx=20, pady=10)
rightFrame = tk.Frame(app, borderwidth=2, relief=tk.SOLID)
rightFrame.pack(side=tk.RIGHT, padx=20, pady=10, ipadx=5, ipady=5)

var = tk.StringVar()
label = tk.Label(leftFrame, text='I am a label').pack()
entry = tk.Entry(leftFrame, textvariable=var).pack()
text = tk.Text(leftFrame, height=5, width=25).pack()
button = tk.Button(leftFrame, text='I am a button').pack()

options = ['option 1', 'option 2', 'option 3']
optionVar = tk.StringVar(rightFrame, 'option 1')
dropdown = tk.OptionMenu(rightFrame, optionVar, *options).pack()

chkVar = tk.IntVar(rightFrame, 1)
checkbox = tk.Checkbutton(rightFrame, text='check1', variable=chkVar).pack()

radVar = tk.IntVar(rightFrame,2)
radio1 = tk.Radiobutton(rightFrame, text='radio1', variable=radVar, value=3).pack()
radio2 = tk.Radiobutton(rightFrame, text='radio2',variable=radVar, value=2).pack()

app.mainloop()