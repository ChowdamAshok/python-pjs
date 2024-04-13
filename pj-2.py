import random
from tkinter import *
from tkinter import messagebox

gui = Tk()
gui.title('Password Generator')
gui.geometry('250x200')
gui.resizable(0, 0)

def show_password():
    entered_password = string_pass.get()
    if entered_password:
        generated_password = generate_password(len(entered_password))
        
        new_window = Toplevel(gui)
        new_window.title("Passwords")
        new_window.geometry('300x150')
        new_window.resizable(0, 0)
        
        label_entered = Label(new_window, text=f'Your entered password is {entered_password}')
        label_entered.pack(pady=5)
        
        label_generated = Label(new_window, text=f'Your generated password is {generated_password}')
        label_generated.pack(pady=5)
        
        button_copy = Button(new_window, text="Copy Generated Password", command=lambda: copy_to_clipboard(generated_password))
        button_copy.pack(pady=10)
    else:
        messagebox.showwarning('Warning', 'Please enter a password before generating.')

def generate_password(length):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['@', '#', '$', '%', '&', '*']
    all_chars = lower + upper + num + special
    return "".join(random.sample(all_chars, length))

def copy_to_clipboard(text):
    gui.clipboard_clear()
    gui.clipboard_append(text)
    gui.update()

string_pass = StringVar()
label = Label(text="Password Length")
label.pack(pady=10)
txt = Entry(textvariable=string_pass)
txt.pack()
btn_entered = Button(text="Show Passwords", command=show_password)
btn_entered.pack(pady=5)

gui.mainloop()
