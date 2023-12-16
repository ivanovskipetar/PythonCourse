from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_data():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nWebsite: {website}\nEmail/Username: {email_username}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email_username} | {password}\n")
            website_entry.delete(0, END)
            website_entry.focus()
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=51)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "email_example@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
