import tkinter as tk
import datetime

root = tk.Tk()
root.title("WeekDay")

entry_label = tk.Label(root, text = "Date Format :dd/mm/yy: ")
entry_label.grid(row = 0, column = 0)

#Entry field for user guesses.
user_entry = tk.Entry(root)
user_entry.grid(row = 0, column = 1)

text_box=tk.Label(root,text="WeekDay")
text_box = tk.Text(root, width = 20, height = 2)
text_box.grid(row = 1, column = 0, columnspan = 2)

text_box.insert("end-1c", "      WeekDay")


def guess_number(event = None):
    #Get the string of the user_entry widget
    guess = user_entry.get()
    day, month, year = (int(x) for x in guess.split('/'))
    ans = datetime.date(year, month, day)
    ans=ans.strftime("%A")
    text_box.delete(1.0, "end-1c") # Clears the text box of data
    text_box.insert("end-1c", ans) # adds text to text box


# binds the enter widget to the guess_number function
# while the focus/cursor is on the user_entry widget
user_entry.bind("<Return>", guess_number) 

root.mainloop() 
