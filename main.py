import tkinter

window = tkinter.Tk()
window.title("List in list")
window.geometry("500x500")

first_enter = tkinter.Entry()
first_enter.place(y=190, x=176)

second_enter = tkinter.Entry()
second_enter.place(y=120, x=176)


people = []

def addb():
    first_text = first_enter.get()
    second_text = second_enter.get()

    people.append([second_text, first_text])


    first_enter.delete(0, tkinter.END)
    second_enter.delete(0, tkinter.END)


    display_people()

def display_people():

    for widget in window.pack_slaves():
        if isinstance(widget, tkinter.Label) and widget.winfo_y() < 80:
            widget.destroy()


    for idx, person in enumerate(people):
        text = tkinter.Label(text=f"{idx + 1}. Имя: {person[0]}, Возраст: {person[1]}")
        text.place(y=80 + idx * 20, x=176)

button_add = tkinter.Button(text="Добавить", command=addb)
button_add.place(y=150, x=207)

window.mainloop()
