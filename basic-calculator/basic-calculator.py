import tkinter as tk 

root = tk.Tk()
root.title("Calculadora")
root.iconbitmap("calculator.ico")
root.resizable(False, False)

result = tk.StringVar(root, "")
operador = ""
operation = ""
result_operation = 0

#functions
def operations():
    pass

def show_number(button):
    global operador
    if operador != "":
        result.set(button.cget("text"))
        operador = ""
    else:
        result.set(entry.get()+button.cget("text"))
        

def suma():
    global operador
    global operation
    global result_operation 
    operador = "suma"
    operation = "+"
    result_operation += int(entry.get())
    result.set(result_operation)

def resta():
    global operador
    global operation
    global result_operation
    operador = "resta"
    operation = "-"

    first_num = int(entry.get())
    if result_operation == 0:
       result_operation = first_num

    else:
        result_operation -= first_num
        result.set(result_operation)

def results_general():
    global result_operation
    global operation
    if operation == "+":
        result_operation += int(entry.get())
        result.set(result_operation)
        result_operation = 0
    
    if operation == "-":
        result_operation -= int(entry.get())
        result.set(result_operation)
        result_operation = 0





#Entry
entry = tk.Entry(root, state=tk.DISABLED)
entry.config(font=("Arial", 30, "bold"),width=20, justify="right", textvariable=result)
entry.grid(row=0, column=0, columnspan=4, sticky="we")


# Buttons de la calculadora:
button_7 = tk.Button(root, text="7",)
button_7.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_7.grid(row=1, column=0, sticky="nsew")
button_7.bind("<Button-1>", lambda event: show_number(button_7))

button_8 = tk.Button(root, text="8")
button_8.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_8.grid(row=1, column=1, sticky="nsew")
button_8.bind("<Button-1>", lambda event: show_number(button_8))


button_9 = tk.Button(root, text="9")
button_9.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_9.grid(row=1, column=2, sticky="nsew")
button_9.bind("<Button-1>", lambda event: show_number(button_9))


button_div = tk.Button(root, text="/")
button_div.config(padx=50, pady=50, bg="#4472C4", fg="#fff", font=("Arial",15,"bold"))
button_div.grid(row=1, column=3, sticky="nsew")
button_div.bind("<Button-1>", lambda event: operations("/"))


###########################################################################################


button_4 = tk.Button(root, text="4",)
button_4.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_4.grid(row=2, column=0, sticky="nsew")
button_4.bind("<Button-1>", lambda event: show_number(button_4))

button_5 = tk.Button(root, text="5",)
button_5.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_5.grid(row=2, column=1, sticky="nsew")
button_5.bind("<Button-1>", lambda event: show_number(button_5))

button_6 = tk.Button(root, text="6",)
button_6.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_6.grid(row=2, column=2, sticky="nsew")
button_6.bind("<Button-1>", lambda event: show_number(button_6))

button_mul = tk.Button(root, text="x")
button_mul.config(padx=50, pady=50, bg="#4472C4", fg="#fff", font=("Arial",15,"bold"))
button_mul.grid(row=2, column=3, sticky="nsew")
button_mul.bind("<Button-1>", lambda event: operations("x"))


############################################################################################


button_1 = tk.Button(root, text="1",)
button_1.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_1.grid(row=3, column=0, sticky="nsew")
button_1.bind("<Button-1>", lambda event: show_number(button_1))

button_2 = tk.Button(root, text="2",)
button_2.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_2.grid(row=3, column=1, sticky="nsew")
button_2.bind("<Button-1>", lambda event: show_number(button_2))

button_3 = tk.Button(root, text="3",)
button_3.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_3.grid(row=3, column=2, sticky="nsew")
button_3.bind("<Button-1>", lambda event: show_number(button_3))

button_menos = tk.Button(root, text="-")
button_menos.config(padx=50, pady=50, bg="#4472C4", fg="#fff", font=("Arial",15,"bold"))
button_menos.grid(row=3, column=3, sticky="nsew")
button_menos.bind("<Button-1>", lambda event: resta())

############################################################################################
button_0 = tk.Button(root, text="0")
button_0.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_0.grid(row=4, column=0, sticky="nsew")
button_0.bind("<Button-1>", lambda event: show_number(button_0))


button_mas = tk.Button(root, text="+")
button_mas.config(padx=50, pady=50, bg="#4472C4", fg="#fff", font=("Arial",12,"bold"))
button_mas.grid(row=4, column=3, sticky="nsew")
button_mas.bind("<Button-1>", lambda event: suma())

button_result = tk.Button(root, text="=" )
button_result.config(padx=50, pady=50, bg="#4472C4", fg="#fff", font=("Arial",15,"bold"))
button_result.grid(row=4, column=1,columnspan=2,sticky="we") 
button_result.bind("<Button-1>", lambda event: results_general())




#anchor="nw": Posiciona desde la esquina superior izquierda (north-west)

#anchor="w": Alinea a la izquierda (west)

#side="top": Apila verticalmente desde arriba

#sticky="w": En grid, pega a la izquierda

root.mainloop()