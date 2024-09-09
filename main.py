import tkinter as tk
# new

def on_button_click():
    label_out.config(text=f'Привет, {str(entry.get())}')

root  = tk.Tk()
root.title("В - Вежливость")
root.geometry('400x150')

label = tk.Label(root, text="Как вас зовут?")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Ответить", command=on_button_click)
button.pack()

label_out = tk.Label(root, text="")
label_out.pack()


root.mainloop()
