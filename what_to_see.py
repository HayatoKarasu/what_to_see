from tkinter import Tk, Button, font, ttk, Label, PhotoImage
import tkinter as tk
import pickle
import random
from moviepy.editor import *
import pygame

pygame.display.set_caption('Видео')
 
clip = VideoFileClip(r"333.mp4")
clip.preview() # Задание размера экрана видео
 
pygame.quit()

items = []
root = None  # объявляем переменную root в глобальной области видимости

def start():
    global root
    if root is not None:  # проверяем, существует ли уже окно
        root.destroy()  # закрываем старое окно, если оно существует
    root = Tk()     # создаем корневой объект - окно

    #root.configure(bg="light blue") #если хотим однотонный фон вместо картинки

    image = PhotoImage(file="E:/new folder/new folder/films/imgfon.png") #полный адрес картинки
    background_label = Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)

    root.title("ЧЁ ПОСМОТРЕТЬ?")     # устанавливаем заголовок окна
    root.iconbitmap(default="logo_.ico") # создали логотип
    # Получаем ширину и высоту экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисляем координаты окна приложения
    window_width = 800
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.resizable(True, True) # первый параметр указывает, может ли пользователь растягивать окно по ширине, а второй параметр - можно ли растягивать по высоте

    my_font = font.Font(family="Arial", weight="bold", size=12)


    label = ttk.Label(text="Привет! Выбери что хочешь сделать.", font=("Arial", 21)) # создаем текстовую метку
    label.pack()    # размещаем метку в окне

    btn1 = Button(root, text="Выйти из программы", background = '#ffb76f', foreground = "black", font=my_font, command=exit, bd=4, highlightthickness=4) # создаем кнопку из пакета ttk
    btn1.place(relx=0.5, rely=0.5, anchor="nw", relwidth=0.33, relheight=0.25)   # размещаем кнопку в окне растянув ее по горизонтали

    btn2 = Button(root,text="Показать весь список", background = '#ffb76f', foreground = "black", font=my_font, command=show, bd=4, highlightthickness=4) # создаем кнопку из пакета ttk
    btn2.place(relx=0.5, rely=0.5, anchor="ne", relwidth=0.33, relheight=0.25)

    btn3 = Button(root,text="Выбрать Чё посмотреть :)", background = '#ffb76f', foreground = "black", font=my_font, command=choice, bd=4, highlightthickness=4) # создаем кнопку из пакета ttk
    btn3.place(relx=0.5, rely=0.5, anchor="sw", relwidth=0.33, relheight=0.25)

    btn4 = Button(root, text="Добавить фильм в список", background='#ffb76f', foreground="black", font=my_font, command=addf, bd=4, highlightthickness=4)
    btn4.place(relx=0.5, rely=0.5, anchor="se", relwidth=0.33, relheight=0.25)

    root.mainloop()


def load_items():
    global items
    try:
        with open('items.pickle', 'rb') as file:
            items = pickle.load(file)
    except FileNotFoundError:
        items = []


def add_to_list(entry):
    new_item = entry.get()  # получаем элемент из элемента ввода
    items.append(new_item)  # добавляем элемент в список
    with open('items.pickle', 'wb') as file:  # сохраняем список в файл 'items.pickle'
        pickle.dump(items, file)
    entry.delete(0, 'end')  # очищаем поле ввода


def addf():
    global items  # объявляем items как глобальную переменную
    global root
    if root is not None:  # проверяем, существует ли уже окно
        root.destroy()
    root = Tk()      # создаем корневой объект - окно

    #root.configure(bg="light blue") #если хотим однотонный фон вместо картинки

    image = PhotoImage(file="E:/new folder/new folder/films/imgfon.png") #полный адрес картинки
    background_label = Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)

    root.title("ЧЁ ПОСМОТРЕТЬ?")     # устанавливаем заголовок окна
    root.iconbitmap(default="logo_.ico") # создали логотип
    # Получаем ширину и высоту экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисляем координаты окна приложения
    window_width = 800
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.resizable(True, True) # первый параметр указывает, может ли пользователь растягивать окно по ширине, а второй параметр - можно ли растягивать по высоте

    try:
        with open('items.pickle', 'rb') as file:
            items = pickle.load(file)
    except FileNotFoundError:
        items = []

    label = tk.Label(root, text="Запиши желаемый фильм:", font=("Arial", 16))
    label.pack(pady=50)

    entry = tk.Entry(root, width=30, font=("Arial", 16))
    entry.pack()

    button = tk.Button(root, text="Добавить", background='#ffb76f', foreground="black", command=lambda: add_to_list(entry), font=("Arial", 16), bd=4, highlightthickness=4)  # увеличиваем размер шрифта кнопки
    button.pack(pady=50)  # устанавливаем расстояние между виджетами

    back_button = tk.Button(root, text="Назад", background='#ffb76f', foreground="black", command=start, font=("Arial", 16), bd=4, highlightthickness=4)
    back_button.pack()

    # Выводим окно на экран
    root.mainloop()


def choice():
    global items
    load_items()  # загружаем данные из файла 'items.pickle'
    global root
    if root is not None:
        root.destroy()
    root = Tk()

    #root.configure(bg="light blue") #если хотим однотонный фон вместо картинки

    image = PhotoImage(file="E:/new folder/new folder/films/imgfon.png") #полный адрес картинки
    background_label = Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)

    root.title("ЧЁ ПОСМОТРЕТЬ?")
    root.iconbitmap(default="logo_.ico")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(True, True)

    label = Label(root, text="Выбираем случайный фильм:", font=("Arial", 16))
    label.pack(pady=50)

    button = Button(root, text="Назад", background='#ffb76f', foreground="black", command=start, font=("Arial", 16), bd=4, highlightthickness=4)
    button.pack(pady=50)

    if items:
        picked_item = random.choice(items)
        items.remove(picked_item)
        with open('items.pickle', 'wb') as file:
            pickle.dump(items, file)

        message = f"Выбранный фильм: {picked_item}"
    else:
        message = "Список пуст."

    label_items = Label(root, text=message, font=("Arial", 16))
    label_items.pack(pady=50)

    root.mainloop()


def show():
    global root
    if root is not None: 
        root.destroy()
    root = Tk()

    #root.configure(bg="light blue") #если хотим однотонный фон вместо картинки

    image = PhotoImage(file="E:/new folder/new folder/films/imgfon.png") #полный адрес картинки
    background_label = Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)

    root.title("ЧЁ ПОСМОТРЕТЬ?")     
    root.iconbitmap(default="logo_.ico")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(True, True)

    label = Label(root, text="Список фильмов:", font=("Arial", 16))
    label.pack(pady=50)
    
    button = Button(root, text="Назад", background='#ffb76f', foreground="black", command=start, font=("Arial", 16), bd=4, highlightthickness=4)
    button.pack(pady=50)

    global items 
    load_items()  # загружаем данные из файла 'items.pickle' 
    if not items:
        message = "Список пуст."
    else:
        message = "Список фильмов:" + ", ".join(items)
    
    label_items = Label(root, text=message, font=("Arial", 16))
    label_items.pack(pady=50)

    root.mainloop() 


def exit():
    root.destroy()


start()