import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry("500x500")
window.configure(bg="#333333")

def login():
    username = "reyalo"
    password = "yess69"
    if username_entry.get() == "" or password_entry.get() == "":
        messagebox.showerror(title="Error", message="Please enter your username and password")
    else:
        messagebox.showinfo(title="Login", message="You successfully logged in" )

frame = tkinter.Frame(bg="#333333")

login_label = tkinter.Label(frame, text="Login", bg="#333333", fg="#ffffff", font=("Arial", 50))
username_label = tkinter.Label(frame, text="Username:", bg="#333333", fg="#ffffff", font=("Arial", 20))
username_entry = tkinter.Entry(frame, font=("Arial", 20))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 20))
password_label = tkinter.Label(frame, text="Password:", bg="#333333", fg="#ffffff", font=("Arial", 20))
login_button = tkinter.Button(frame, text="Login", bg="#ff3399", fg="#ffffff", font=("Arial", 20), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=50)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=10)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=10)
login_button.grid(row=3, column=0, columnspan=2, pady= 40)

frame.pack()


window.mainloop()