import tkinter as tk
from tkinter import StringVar
from tkinter import OptionMenu
calculation = ""
NatureAbundanceMod = 100
has_reduced_mod = False
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end") #this is how to delete contents of text resultt field
    text_result.insert(1.0, calculation) #this is what inserts the string



def evaluate_calculation():
    global calculation, NatureAbundanceMod
    try:
        if nature_abundance.get() == "Very Poor":
            NatureAbundanceMod = 140
        elif nature_abundance.get() == "Poor":
            NatureAbundanceMod = 120
        elif nature_abundance.get() == "Normal":
            NatureAbundanceMod = 100
        elif nature_abundance.get() == "Abundant":
            NatureAbundanceMod = 80
        elif nature_abundance.get() == "Very Abundant":
            NatureAbundanceMod = 60
            
            
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end") 
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
        pass
        
def handle_option(selection):
    add_to_calculation(selection)

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def show():
    label.config( text = clicked.get() )
    
    
def calculate_probability():
    global NatureAbundanceMod
    CurrentHour = int(entry.get())
    if CurrentHour >= 4 and CurrentHour <= 6 or CurrentHour >= 18 and CurrentHour <= 20:
        NatureAbundanceMod -= 10
        has_reduced_mod = True
    has_reduced_mod = False
    probability = 1 / (NatureAbundanceMod + 1)
    print(probability)
    print(NatureAbundanceMod)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, f"Probability: {probability:.5f}")



root = tk.Tk()

root.geometry("300x450")
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24)) #these make the text field
text_result.grid(columnspan=5) #these make the text field
'''
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14)) #better to use lambda rather than just calling the function where as lambda will refer to a function that will be called
btn_1.grid(row=2, column=1)
'''


clicked = StringVar()
clicked.set("Fishing Level")

nature_abundance = StringVar() #this is the nature abundance thingy
nature_abundance.set("Normal")  #setting normal as default value




nature_abundance_options = [ "Very Poor", "Poor", "Normal", "Abundant", "Very Abundant"]
drop_nature_abundance = OptionMenu(root, nature_abundance ,*nature_abundance_options)
drop_nature_abundance.grid(row=7, column=2)

entry = tk.Entry(root, width = 10, font=("Arial", 14))
entry.grid(row = 9, column = 1, columnspan = 4, pady=(20, 0))

btn_print = tk.Button(root, text="Print", command=lambda: print(NatureAbundanceMod), width=11, font=("Arial", 14)) #better to use lambda rather than just calling the function where as lambda will refer to a function that will be called
btn_print.grid(row=7, column=3)

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14)) #better to use lambda rather than just calling the function where as lambda will refer to a function that will be called
btn_equal.grid(row=6, column=1, columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14)) #better to use lambda rather than just calling the function where as lambda will refer to a function that will be called
btn_clear.grid(row=6, column=3, columnspan=2)

btn_probability = tk.Button(root, text="Probability Calculator", command=calculate_probability, width=16, font=("Arial", 14), )
btn_probability.grid(row = 8, column = 1, columnspan = 4, pady=(20, 0))
root.mainloop()