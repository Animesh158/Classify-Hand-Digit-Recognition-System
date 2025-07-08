from tkinter import *
import os
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x350")
    register_screen.configure(bg="#f0f0f0")

    global username, password, username_entry, password_entry
    username = StringVar()
    password = StringVar()

    frame = Frame(register_screen, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Please enter details below", bg="#f0f0f0", fg="#333", font=("Calibri", 14)).pack(pady=10)
    
    Label(frame, text="Username *", bg="#f0f0f0", fg="#333", font=("Calibri", 12)).pack(pady=5)
    username_entry = Entry(frame, textvariable=username, font=("Calibri", 12))
    username_entry.pack(pady=5)
    
    Label(frame, text="Password *", bg="#f0f0f0", fg="#333", font=("Calibri", 12)).pack(pady=5)
    password_entry = Entry(frame, textvariable=password, show='*', font=("Calibri", 12))
    password_entry.pack(pady=5)
    
    Button(frame, text="Register", width=15, height=2, bg="#4CAF50", fg="white", font=("Calibri", 12), command=register_user).pack(pady=20)

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x350")
    login_screen.configure(bg="#f0f0f0")

    global username_verify, password_verify
    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry, password_login_entry

    frame = Frame(login_screen, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Please enter details below to login", bg="#f0f0f0", fg="#333", font=("Calibri", 14)).pack(pady=10)
    
    Label(frame, text="Username *", bg="#f0f0f0", fg="#333", font=("Calibri", 12)).pack(pady=5)
    username_login_entry = Entry(frame, textvariable=username_verify, font=("Calibri", 12))
    username_login_entry.pack(pady=5)
    
    Label(frame, text="Password *", bg="#f0f0f0", fg="#333", font=("Calibri", 12)).pack(pady=5)
    password_login_entry = Entry(frame, textvariable=password_verify, show='*', font=("Calibri", 12))
    password_login_entry.pack(pady=5)
    
    Button(frame, text="Login", width=15, height=2, bg="#4CAF50", fg="white", font=("Calibri", 12), command=login_verify).pack(pady=20)

def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x450")
    main_screen.title("Account Login")
    main_screen.configure(bg="#f0f0f0")

    Label(main_screen, text="Select Your Choice", bg="#4CAF50", fg="white", width="300", height="2", font=("Calibri", 16)).pack(pady=10, anchor=N)

    frame = Frame(main_screen, bg="#f0f0f0")
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    Button(frame, text="Login", height="2", width="30", bg="#2196F3", fg="white", font=("Calibri", 12), command=login).pack(pady=10)
    Button(frame, text="Register", height="2", width="30", bg="#2196F3", fg="white", font=("Calibri", 12), command=register).pack(pady=10)
    
    main_screen.mainloop()


import subprocess

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=run_ml_app).pack()

def run_ml_app():
    login_success_screen.destroy()
    # Run the ML application code
    subprocess.Popen(["python", "ml_app.py"])


main_account_screen()