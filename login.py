from tkinter import *
from tkinter import Text, messagebox
from PIL import ImageTk

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1920x1080+80+50")

        self.bg = ImageTk.PhotoImage(file = "images/bg_image.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Login_Frame = Frame(self.root, bg="white", bd=4)
        Login_Frame.place(x=400, y=190, height=340, width=500)

        title = Label(Login_Frame, text="Login Here", bg="white", font=("Impact",30,"normal"), fg="red")
        title.grid(row=0, column=0, padx=150, pady=15)

        self.username = StringVar()
        self.password = StringVar()

        Username_Text = Label(Login_Frame, text="Username", bg="white", font=("times new roman", 15))
        Username_Text.grid(row=1, column=0, pady=10)
        Username_Box = Entry(Login_Frame, textvariable=self.username, bg="lightgrey", width=30, font=("times new roman", 14))
        Username_Box.grid(row=2, column=0, pady=10)

        Password_Text = Label(Login_Frame, text="Password", bg="white", font=("times new roman", 15))
        Password_Text.grid(row=3, column=0)
        Password_Box = Entry(Login_Frame, textvariable=self.password, bg="lightgrey", width=30, font=("times new roman", 14))
        Password_Box.grid(row=4, column=0, pady=10)

        Login_Button = Button(Login_Frame, command=self.Create_Login, text="Login", height=1, width=12, font=("times new roman", 15), fg="black", bg="skyblue")
        Login_Button.grid(row=5, column=0, pady=20)

    def Create_Login(self):
        username = self.username.get()
        password = self.password.get()

        if not username or username == "":
            messagebox.showerror("Error", "Provide your username")
        elif not password or password == "":
            messagebox.showerror("Error", "Provide password")
        elif username == "admin" and password == "admin":
            messagebox.showinfo("Success", "Logged in as Admin")
        else:
            messagebox.showerror("Error", "Username/password not found.")


window = Tk()
execute = Login(window)
window.mainloop()