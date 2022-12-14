from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Commando to write info to txt file


def add_button_command():
    # Getting the info
    website = entry_website.get()
    user = entry_email_username.get()
    password = entry_password.get()
    # Message box to confirm the add
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Deleting the entries
            entry_website.delete(0, END)
            entry_email_username.delete(0, END)
            entry_password.delete(0, END)
            # Opening and writing
            with open("data.txt", "a") as data_text:
                data_text.write(f"{website} | {user} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

# Window

window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=50, pady=50)


# Logo
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Entries

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()  # Places the cursor in the query
entry_email_username = Entry(width=35)
entry_email_username.grid(column=1, row=2, columnspan=2)
entry_email_username.insert(0, "pedrowilliamrd@gmail.com")  # Insert the text on the 0th caracter
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons

password_button = Button(text="Generate password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_button_command)
add_button.grid(column=1, row=4, columnspan=2)
clipboard_button = Button(text="Add to clipboard", command=pyperclip.copy)
clipboard_button.grid(column=1, row=5, columnspan=2)

window.mainloop()