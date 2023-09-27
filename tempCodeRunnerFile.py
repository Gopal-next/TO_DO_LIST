from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import backend


selected_row = []
def selected(event):
    global selected_row
    index=list.curselection()
    selected_row=list.get(index)
    e1.delete(0,END)
    e1.insert(END, selected_row[1])
    e2.delete(0,END)
    e2.insert(END, selected_row[2])
    e3.delete(0,END)
    e3.insert(END, selected_row[3])
    e4.delete(0,END)
    e4.insert(END, selected_row[4])
    e5.delete(0,END)
    e5.insert(END, selected_row[5])
    e6.delete(0,END)
    e6.insert(END, selected_row[6])

def delete_cmd():
    if not selected_row:
            messagebox.showwarning("Warning", "Please select a row to delete")
            return

    result = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected row?")
    if result:
        backend.delete(selected_row[0])
        messagebox.showinfo("Success", "Row deleted successfully")
    view_cmd()

def view_cmd():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_cmd():
    list.delete(0, END)
    search_results = backend.search(date_text.get(), earning_text.get(), excercise_text.get(), study_text.get(),
                                    diet_text.get(), expense_text.get())
    count = len(search_results)
    for row in search_results:
        list.insert(END, row)
    messagebox.showinfo("Search Results", f"Found {count} rows matching the search criteria")


def add_cmd():
    if not date_text.get() or not earning_text.get() or not excercise_text.get() or not study_text.get() \
            or not diet_text.get() or not expense_text.get():
        messagebox.showerror("Error", "Please fill in all the fields")
        return

    try:
        earnings = int(earning_text.get())
        expense = int(expense_text.get())
    except ValueError:
        messagebox.showerror("Error", "Earnings and Expense should be numeric values")
        return
    
    backend.insert(date_text.get(), earning_text.get(), excercise_text.get(), study_text.get(), diet_text.get(), expense_text.get())
    list.delete
    list.insert(END,(date_text.get(), earning_text.get(), excercise_text.get(), study_text.get(), diet_text.get(), expense_text.get()))


def update_cmd():
    global selected_row
    backend.update(selected_row[0], date_text.get(), earning_text.get(), excercise_text.get(),
                   study_text.get(), diet_text.get(), expense_text.get())
    view_cmd()
    

def refresh_cmd():
    view_cmd()


win = Tk()

win.wm_title("Daily Routine")

label_style = {
    "bg": "#F3F4F6",
    "fg": "dark orange",
    "font": ("Lato", 12),
    "borderwidth": 2,
    "relief": "groove",
    "padx": 4,
    "pady": 4
}

labels = [
    {"text": "Date", "row": 0, "column": 0},
    {"text": "Earnings", "row": 0, "column": 2},
    {"text": "Exercise", "row": 1, "column": 0},
    {"text": "Study", "row": 1, "column": 2},
    {"text": "Diet", "row": 2, "column": 0},
    {"text": "Expenses", "row": 2, "column": 2}
]

for lbl in labels:
    label = Label(win, text=lbl["text"], **label_style)
    label.grid(row=lbl["row"], column=lbl["column"], sticky=N+S+E+W)


date_text=StringVar()
e1=Entry(win,textvariable=date_text)
e1.grid(row=0,column=1)


earning_text=StringVar()
e2=Entry(win,textvariable=earning_text)
e2.grid(row=0,column=3)

excercise_text=StringVar()
e3=Entry(win,textvariable=excercise_text)
e3.grid(row=1,column=1)

study_text=StringVar()
e4=Entry(win,textvariable=study_text)
e4.grid(row=1,column=3)

diet_text=StringVar()
e5=Entry(win,textvariable=diet_text)
e5.grid(row=2,column=1)

expense_text=StringVar()
e6=Entry(win,textvariable=expense_text)
e6.grid(row=2,column=3)

list=Listbox(win,height=10,width=40)
list.grid(row=3,column=0,rowspan=10,columnspan=2)

sb = Scrollbar(win)
sb.grid(row=3, column=2, rowspan=9, sticky="NS")

list = Listbox(win, height=10, width=40, yscrollcommand=sb.set)
list.grid(row=3, column=0, rowspan=10, columnspan=2)

sb.config(command=list.yview)

list.bind('<<ListboxSelect>>',selected)


style = ttk.Style()
style.configure("CustomButton.TButton",
                background="white",
                foreground="blue",
                font=("Lato", 12),
                borderwidth=2,
                relief="groove")
style.map("CustomButton.TButton",
          background=[('active', 'light blue')],
          foreground=[('active', 'dark blue')])

buttons = [
    {"text": "ADD", "command": add_cmd, "row": 3},
    {"text": "SEARCH", "command": search_cmd, "row": 4},
    {"text": "UPDATE", "command": update_cmd, "row": 5},
    {"text": "REFRESH", "command": refresh_cmd, "row": 6},
    {"text": "DELETE", "command": delete_cmd, "row": 7},
    {"text": "VIEW", "command": view_cmd, "row": 8},
    {"text": "CLOSE", "command": win.destroy, "row": 9}
]

for btn in buttons:
    button = ttk.Button(win, text=btn["text"], width=12, command=btn["command"], style="CustomButton.TButton")
    button.grid(row=btn["row"], column=3, pady=5)


win.mainloop()
