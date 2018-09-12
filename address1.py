import tkinter as tk
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG, filename='log.txt')

conn = sqlite3.connect('addressbook.db')
c = conn.cursor()


def insert_database():
    c.execute("""INSERT INTO book (name, lastname, address, phone) VALUES (?,?,?,?) """, (input_name.get(), input_lastname.get(), input_address.get(), input_phonenumber.get()))
    logging.info((input_name.get(), input_lastname.get(), input_address.get(), input_phonenumber.get()))
    conn.commit()
    input_name.set('')
    input_lastname.set('')
    input_address.set('')
    input_phonenumber.set('')


def find():
    if input_find.get()!='':
        like ="%{0}%".format(input_find.get())
        dane = c.execute("""SELECT * FROM book WHERE name like ? OR lastname like ? OR address like ?; """, (like, like, like,))
        for line in dane:
            logging.info(line)
            text_field.insert(tk.INSERT, str(line[1])+' '+str(line[2])+' '+line[3]+' '+line[4]+"\n")


def find_all():
    dane = c.execute("""SELECT * FROM book""")
    for line in dane:
        # logging.info(line)
        text_field.insert(tk.INSERT, str(line[1]) + ' ' + str(line[2]) + ' ' + line[3] + ' ' + line[4] + "\n")

def find_telephone_nr():
    if input_find.get() != '':
        like = "%{0}%".format(input_find.get())
        dane = c.execute("""SELECT * FROM book WHERE phone like ? ;""", (like, ))
        for line in dane:
            logging.info(line)
            text_field.insert(tk.INSERT, str(line[1])+' '+str(line[2])+' '+line[3]+' '+line[4]+"\n")


def clear():
        text_field.delete('1.0', tk.END)
        input_find_field.delete(0, tk.END)


root = tk.Tk()

# background color
bg_colour = 'cyan'
inputs_colour = '#E0FFFF'
root.configure(background=bg_colour)

# left column

tk.Label(root, text='Wprowadź dane', background=bg_colour).grid(row=0, column=1)

input_name = tk.StringVar()
input_lastname = tk.StringVar()
input_address = tk.StringVar()
input_phonenumber = tk.StringVar()

tk.Label(root, text='Imię', background=bg_colour).grid(row=1, column=0)
input_name_field = tk.Entry(root, textvariable=input_name, background=inputs_colour)
input_name_field.grid(row=1, column=1)

tk.Label(root, text='Nazwisko', background=bg_colour).grid(row=2, column=0)
input_lastname_field = tk.Entry(root, textvariable=input_lastname, background=inputs_colour)
input_lastname_field.grid(row=2, column=1)

tk.Label(root, text='Adres', background=bg_colour).grid(row=3, column=0)
input_address_field = tk.Entry(root, textvariable=input_address, background=inputs_colour)
input_address_field.grid(row=3, column=1)

tk.Label(root, text='Nr telefonu', background=bg_colour).grid(row=4, column=0)
input_phonenumber_field = tk.Entry(root, textvariable=input_phonenumber, background=inputs_colour)
input_phonenumber_field.grid(row=4, column=1)

button_insert_database = tk.Button(root, text='Zapisz do \n bazy daych', background=bg_colour, command=insert_database)
button_insert_database.grid(row=5, column=1, sticky=tk.N)

# right column
input_find = tk.StringVar()

tk.Label(root, text='Wpisz szukany tekst', background=bg_colour).grid(row=0, column=3)
input_find_field = tk.Entry(root, textvariable=input_find,background=inputs_colour)
input_find_field.grid(row=1, column=3, sticky=tk.N)

buttons = tk.PanedWindow()
buttons.grid(row=3, column=3, sticky=tk.N)

# buttons are pinned up to "buttons"
button_find = tk.Button(buttons, text='Wyszukaj', background=bg_colour, command=find)
button_find.grid(row=3, column=3, sticky=tk.N)
button_show = tk.Button(buttons, text='Szukaj po numerze telefonu', background=bg_colour, command=find_telephone_nr)
button_show.grid(row=3, column=4, sticky=tk.N)
button_clear = tk.Button(buttons, text='Wyczyść', background=bg_colour, command=clear)
button_clear.grid(row=3, column=5, sticky=tk.N)

button_show_all = tk.Button(root, text='Wyświetl wszystko', background=bg_colour, command=find_all)
button_show_all.grid(row=5, column=3, sticky=tk.N)

#text filed
text_field = tk.Text(root)
text_field.grid(row=6, column=3, sticky=tk.N)
text_field.config(width=50, background=inputs_colour)


root.mainloop()

conn.close()
