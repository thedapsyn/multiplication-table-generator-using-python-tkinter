from tkinter import *
from tkinter import ttk
import math

#Create an instance of Tkinter frame
root = Tk()

#Set the geometry of tkinter frame
root.geometry("1000x1000")

#Set the Title of Tkinter rootdow
root.title("Multiplication Table Generator")

    
def multiplication_table():
    """Generate  multiplication table from the range 1 to 12"""
    global table
    try:
        no= int(entry.get())
        entry.delete(0, 'end')
        Label(root, text=f'Multiplication Table: {no}',font="BOLD").pack()
        for i in range(1,13):
            product = no * i
            table = ttk.Label(text=f'{no} * {i} = {product}', font="BOLD")
            table.pack()
    except ValueError:
        hint = ttk.Label(root, text="Bad Input,\n Enter only number")
        hint.pack()      

# Create an entry widget to accept user input
Label(root, text='Enter Your Times-table Number:',font="BOLD").pack()
entry= Entry(root, width=30, font=('Helvetica', 30))
entry.pack(ipadx=60,pady=20)

# Create a button to generate the tables
generate_button = ttk.Button(root, text= "Generate", command=multiplication_table)
generate_button.pack()

# Exit
quit_button = ttk.Button(root, text= "Quit", command=root.destroy)
quit_button.pack()

 
root.mainloop()