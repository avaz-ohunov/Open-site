# "Open site.py"

import webbrowser
from PIL import ImageTk
from copypaste import paste
import keyboard
from tkinter import *
from tkinter import messagebox
import os


# Создаём окно
window = Tk()
window.title("Open site")
window.resizable(width=False, height=False)
window["bg"] = "#06062e"
window.iconbitmap("images/Иконка.ico")


width = 600 # Ширина 
height = 400 # Высота

screen_width = window.winfo_screenwidth()  # Ширина экрана
screen_height = window.winfo_screenheight() # Высота экрана

# Координаты, где надо открыть окно
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2) - 50

# Передаём размер окна и координаты tkinter
window.geometry("%dx%d+%d+%d" % (width, height, x, y))


# Задаём вопрос пользователю
label = Label(window, font = ("Comfortaa",31),
			text = "Какой сайт вы хотите открыть?", 
			bg = "#06062e", fg = "#fff",)

label.grid(column = 0, row = 0, pady = 20,)


# Поле ввода текста
wvod = Entry(window, font = ("Comfortaa", 33), 
            bg = "#b8b8d4", fg = "#000",
            relief = "solid", justify = "center")

wvod.focus()
wvod.grid(column = 0, row = 1)



# Функция открытия Базы данных с сайтами
def open_file():
	os.startfile("url.txt")

# Импортируем фотку формы
form_img = ImageTk.PhotoImage(file = "images/Form.png")

btn_form = Button(window, image = form_img,
				bg = "#b8b8d4", cursor = "hand2",
				highlightthickness = 0, bd = 0,
				relief = "flat",
				activebackground = "#b8b8d4",
				command = open_file)

btn_form.place(x = 60, y = 95)



# Функция кнопки клавиатуры
def click_keyboard():
	keyboard.send("win+ctrl+o")


# Импортируем фотку клавиатуры
keyboard_img = ImageTk.PhotoImage(file = "images/Клавиатура.png")

btn_keyboard = Button(window, image = keyboard_img, 
					bg = "#b8b8d4", cursor = "hand2",
					highlightthickness = 0, bd = 0,
					relief = "flat", 
					activebackground = "#b8b8d4",
					command = click_keyboard)

btn_keyboard.place(x = 485, y = 95)



# Открываем файл с сайтами
def open_file():
	global url
	with open("url.txt", "r", encoding = "utf-8") as file:
	    url = eval(file.read())
	    window.after(1000, open_file)

open_file()



# Функция нажатия клавиши Enter
def enter(event):
    click()

window.bind("<Return>", enter)


# Функция нажатия клавиши Escape
def esc(event):
    window.wm_state("iconic")

window.bind("<Escape>", esc)


# Список в котором будут храниться введённые кодовые слова
codewords = []
up_down = 0

# Функции клика по стрелкам ↑↓
def click_up(event):
	try:
		global up_down, codewords
		wvod.delete(0, END)
		up_down -= 1
		wvod.insert(END, codewords[up_down])

	except IndexError:
		wvod.delete(0, END)
		up_down = -1
		wvod.insert(END, codewords[up_down])

window.bind("<Key-Up>", click_up)


def click_down(event):
	try:
		global up_down, codewords 
		wvod.delete(0, END)
		up_down += 1
		wvod.insert(END, codewords[up_down])

	except IndexError:
		wvod.delete(0, END)
		up_down = 0
		wvod.insert(END, codewords[up_down])

window.bind("<Key-Down>", click_down)
    

# Функция клика по кнопке "Открыть"
def click():
	global codewords, up_down

	site = wvod.get() # Заключаем в переменную значение ввода
	
	if site not in url:
		messagebox.showwarning("Ошибка", "Неверное кодовое слово!")
	
	else:
		webbrowser.open( url[site] )
		wvod.delete(0, END)

		if site not in codewords:
			codewords.append(site)
		else:
			codewords.append(codewords.pop(codewords.index(site)))
		
		up_down = 0



# Импортируем фотку лупы
img = ImageTk.PhotoImage(file = "images/Лупа.ico")

# Параметры кнопки
btn = Button(window, image = img, bg = "#06062e", bd = 0,
            highlightthickness = 0, relief = "flat",
            activebackground = "#06062e", cursor = "hand2",
            command = click)

btn.grid(column = 0, row = 2, pady = 30)



# Горячие клавиши
def ctrl_bs(event):
	text = wvod.get()
	index = text.rfind(" ")
	wvod.delete(index+1, END)

wvod.bind("<Control-BackSpace>", ctrl_bs)



# События мыши
def right_click(e):
    wvod.insert( END, paste() )

wvod.bind("<Button-3>", right_click)







# Создаём бесконечный цикл, пока пользователь не нажмёт крестик
window.mainloop()


# "Open site.py"