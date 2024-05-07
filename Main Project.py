import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("TOTAL MONEY")
window.geometry("400x400")
 

def addition():
    try:
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
        num3 = int(number3_entry.get())
        num4 = int(number4_entry.get())

        result = num1 + num2 + num3 + num4
        print(result)
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        
         

def subtraction():
    try:
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
        num3 = int(number3_entry.get())
        num4 = int(number4_entry.get())

        result = num1 - num2 - num3 - num4
        print(result)
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        
         
def multiplication():
    try:
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
        num3 = int(number3_entry.get())
        num4 = int(number4_entry.get())

        result = num1 * num2 * num3 * num4
        print(result)
        messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        
         

def division():
    try:
        num1 = int(number1_entry.get())
        num2 = int(number2_entry.get())
        num3 = int(number3_entry.get())
        num4 = int(number4_entry.get())

        if num4 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
        else:
            result = num1 / num2 / num3 / num4
            print(result)
            messagebox.showinfo("Result", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        
         


number1_label = tk.Label(window, text="Number 1:")
number1_label.grid(row=0,column=0)

number2_label = tk.Label(window, text="Number 2:")
number2_label.grid(row=1,column=0)

number3_label = tk.Label(window, text="Number 3:")
number3_label.grid (row=2, column=0)

number4_label = tk.Label(window, text="Number 4:")
number4_label.grid (row=3, column=0)

number1_entry = tk.Entry(window)
number2_entry = tk.Entry(window)

number1_entry.grid(row=0, column=1)
number2_entry.grid(row=1, column=1)

number3_entry = tk.Entry(window)
number3_entry.grid(row=2, column=1)

number4_entry = tk.Entry(window)
number4_entry.grid(row=3, column=1)



add_button = tk.Button(window, text="Add", command=addition)
add_button.grid(row=4, column=0)
subtract_button = tk.Button(window, text="Subtract", command=subtraction)
subtract_button.grid(row=4, column=1)
multiply_button = tk.Button(window, text="Multiply", command=multiplication)
multiply_button.grid(row=5, column=0)
divide_button = tk.Button(window, text="Divide", command=division)
divide_button.grid(row=5, column=1)

 
window.mainloop()
 