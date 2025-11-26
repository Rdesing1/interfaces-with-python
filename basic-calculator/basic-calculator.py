import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.iconbitmap("calculator.ico")
root.resizable(False, False)

#functions

def show_number(button):
    number = ""+button.cget("text")
    entry.insert(0, number)


#Entry
entry = tk.Entry(root)
entry.config( font=("Arial", 30, "bold"),width=20, justify="right")
entry.grid(row=0, column=0, columnspan=3, sticky="we")


# Buttons de la calculadora:
button_7 = tk.Button(root, text="7",)
button_7.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_7.grid(row=1, column=0, sticky="nsew")
button_7.bind("<Button-1>", lambda event: show_number(button_7))

button_8 = tk.Button(root, text="8")
button_8.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_8.grid(row=1, column=1, sticky="nsew")

button_9 = tk.Button(root, text="9")
button_9.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_9.grid(row=1, column=2, sticky="nsew")

#################################################

button_4 = tk.Button(root, text="4")
button_4.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_4.grid(row=2, column=0, sticky="nsew")

button_5 = tk.Button(root, text="5")
button_5.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_5.grid(row=2, column=1, sticky="nsew")

button_6 = tk.Button(root, text="6")
button_6.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_6.grid(row=2, column=2, sticky="nsew")

#################################################

button_1 = tk.Button(root, text="1")
button_1.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_1.grid(row=3, column=0, sticky="nsew")

button_2 = tk.Button(root, text="2")
button_2.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_2.grid(row=3, column=1, sticky="nsew")

button_3 = tk.Button(root, text="3")
button_3.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_3.grid(row=3, column=2, sticky="nsew")

#################################################
button_0 = tk.Button(root, text="0")
button_0.config(padx=50, pady=50, bg="#1F1F1F", fg="#fff", font=("Arial",12,"bold"))
button_0.grid(row=4, column=0, sticky="nsew")

button_result = tk.Button(root, text="=")
button_result.config(padx=50, pady=50, bg="#4472C4", fg="#fff", font=("Arial",12,"bold"))
button_result.grid(row=4, column=1,columnspan=2,sticky="we")



#anchor="nw": Posiciona desde la esquina superior izquierda (north-west)

#anchor="w": Alinea a la izquierda (west)

#side="top": Apila verticalmente desde arriba

#sticky="w": En grid, pega a la izquierda

root.mainloop()