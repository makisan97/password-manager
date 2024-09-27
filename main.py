from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = ''.join(password_list) 
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
     
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message='Please make sure to complete all fields')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'This is what will be saved: {email} : {password}')
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f"{website}  |  {email}  |  {password}\n")
            website_entry.delete(0,END)
            email_entry.delete(0, END)
            password_entry.delete(0,END)
            website_entry.focus()
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

label1 = Label(text='Website:')
label1.grid(row=1, column=0)

label2 = Label(text='Email/Username:')
label2.grid(row=2, column=0)

label3 = Label(text='Password:')
label3.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', width=15, command=generate_password)
generate_password_button.grid(row=3, column=3)

add_button = Button(text='Add', width=30, command=save_password)
add_button.grid(row=4, column=1)







window.mainloop()