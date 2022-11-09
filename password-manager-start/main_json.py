from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def find_password():
    try:
        with open("data.json", "r") as data_text:
            # Reading old data
            data = json.load(data_text)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found!")
    else:
        website_name = entry_website.get()

        if website_name in data: # Getting the info
            user_search = data[website_name]["user"]
            password_search = data[website_name]["password"]
            messagebox.showinfo(title="Search", message=f"User: {user_search}\n Password: {password_search}")
        else:
            messagebox.showinfo(title="Search", message="There is no info for this website.")





# ---------------------------- SAVE PASSWORD ------------------------------- #
# Commando to write info to txt file


def add_button_command():
    # Getting the info
    website = entry_website.get()
    user = entry_email_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "user": user,
            "password": password
        },
    }
    # Message box to confirm the add
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_text:
                # Reading old data
                data = json.load(data_text)
        except FileNotFoundError:
            with open("data.json", "w") as data_text:
                # Creating new file
                json.dump(new_data, data_text, indent=4)
        else:
            # Updating
            data.update(new_data)

            with open("data.json", "w") as data_text:
                # Saving
                json.dump(data, data_text, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

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

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1)
entry_website.focus()  # Places the cursor in the query
entry_email_username = Entry(width=35)
entry_email_username.grid(column=1, row=2, columnspan=2)
entry_email_username.insert(0, "pedrowilliamrd@gmail.com")  # Insert the text on the 0th character
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

# Buttons

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)
password_button = Button(text="Generate password", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=35, command=add_button_command)
add_button.grid(column=1, row=4, columnspan=2)
clipboard_button = Button(text="Add to clipboard", command=pyperclip.copy)
clipboard_button.grid(column=1, row=5, columnspan=2)

window.mainloop()