from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import random

MORSE_CODE_DICT = {'А': '.-', 'Б': '-...', 'В': '.--',
                   'Г': '--.', 'Д': '-..', 'Е': '.',
                   'Ё': '.', 'Ж': '...-', 'З': '--..',
                   'И': '..', 'Й': '.---', 'К': '-.-',
                   'Л': '.-..', 'М': '--', 'Н': '-.',
                   'О': '---', 'П': '.--.', 'Р': '.-.',
                   'С': '...', 'Т': '-', 'У': '..-',
                   'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                   'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
                   'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-',
                    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
                   'а': '.-*', 'б': '-...*', 'в': '.--*',
                   'г': '--.*', 'д': '-..*', 'е': '.*',
                   'ё': '.*', 'ж': '...-*', 'з': '--..*',
                   'и': '..*', 'й': '.---*', 'к': '-.-*',
                   'л': '.-..*', 'м': '--*', 'н': '-.*',
                   'о': '---*', 'п': '.--.*', 'р': '.-.*',
                   'с': '...*', 'т': '-*', 'у': '..-*',
                   'ф': '..-.*', 'х': '....*', 'ц': '-.-.*',
                   'ч': '---.*', 'ш': '----*', 'щ': '--.-*',
                   'ъ': '.--.-.*', 'ы': '-.--*', 'ь': '-..-*',
                   'э': '..-..*', 'ю': '..--*', 'я': '.-.-*',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


tk = Tk()  # Создаём окно
tk.title('Болотуду')  # Заголовок окна
board = Canvas(tk, width=995, height=495, bg='#FFFFFF')
tk.resizable(width=False, height=False)
board.pack()

Stage_1 = True
Stage_2 = False
blue_count = 0  # Кол-во живых синих фигур
green_count = 0  # Кол-во живых зелёных фигур
blue = 0
green = 0
hod_igroka = True
tri_v_ryad_sinih = False
tri_v_ryad_zelenih = False
vozmozhnost_shodit = False
vozmozhnost_zabrat = False
AI = True
running = False
winner = "Нет"

def on_closing():
    global blue_count,green_count
    global running, winner
    running = False
    tk.quit()
    PersonalAccount.show()
    if running == False:
        qi.label_12.setText(f"Последний результат:\n\n\nСиних в живых:{blue_count}\n\n\nЗеленых в живых:{green_count}\n\n\nПобедитель:{winner}")
    tk.withdraw()
    Start_new()

def button_press1():
    global AI
    if AI == False:
        AI = True
    else:
        AI = False
    vivod(-1,-1)
def Start_new():
    global running
    global blue_count
    global green_count
    global hod_igroka
    global AI
    global Stage_1
    global Stage_2
    global winner
    if running:
        if askyesno("Игра закончена", "Хотите начать новую?"):
            novaya_igra()
            winner = "Нет"
            blue_count = 0
            green_count = 0
            AI = False
            vivod(-1, -1)
            Stage_1 = True
            Stage_2 = False
            hod_igroka = True
        else:
            on_closing()

def izobrazheniya_figur():  # загружаем изображения фигур
    global figuri,i5,i6
    i1 = PhotoImage(file="res\\Blue.png")
    i2 = PhotoImage(file="res\\Green.png")
    i3 = PhotoImage(file="res\\BlueGray.png")
    i4 = PhotoImage(file="res\\GreenGray.png")
    i5 = PhotoImage(file ="res\\SmallBlue.png")
    i6 = PhotoImage(file ="res\\SmallGreen.png")
    figuri = [0, i1, i2, i3, i4]


def novaya_igra():  # начинаем новую игру
    global pole
    pole = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

def Check():
    global St,hod,ii
    if Stage_1:
        St = "Стадия 1. Расстановка фишек"
    if Stage_2:
        St = "Стадия 2. Игра"
    if hod_igroka:
        hod = "Ход синих"
    if hod_igroka == False:
        hod = "Ход зелёных"
    if hod_igroka == None:
        hod = "Конец игры"
    if AI == False:
        ii = "ИИ выключен"
    else:
        ii = "ИИ включен"
def vivod(x_poz_1, y_poz_1):  # рисуем игровое поле
    global figuri
    global pole
    Check()
    k = 100
    x = 0
    board.delete('all')
    board.create_rectangle(995, 5, 605, 495, fill="#fdfff5")
    board.create_text(780,20,fill="Black", font="Open 18 bold", text=f"Статистика")
    board.create_image(650, 175, image=i5)
    board.create_image(870, 175, image=i6)
    board.create_text(800,75,fill="Black", font="Open 18 bold", text=f"{St}")
    board.create_text(775, 125, fill="Black", font="Open 18 bold", text=f"{hod}")
    board.create_text(690,175,fill="Black", font="Open 18 bold", text=f":{blue_count}")
    board.create_text(910, 175, fill="Black", font="Open 18 bold", text=f":{green_count}")
    board.create_text(780, 225, fill="Black", font="Open 18 bold", text=f"{ii}")
    b1 = Button(tk, text="Вкл/Выкл ИИ", command=button_press1)
    b1.place(x=725, y=300, width=120, height=50)


    while x < 6 * k:  # рисуем доску
        y = k
        while y < 5 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="White")
            y += k
        x += k
    x = k
    while x < 6 * k:  # рисуем доску
        y = 0
        while y < 5 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="White")
            y += k
        x += k

    for y in range(5):  # рисуем стоячие пешки
        for x in range(6):
            z = pole[y][x]
            if z:
                if (x_poz_1, y_poz_1) != (x, y):  # стоячие пешки?
                    board.create_image(x * k, y * k, anchor=NW, image=figuri[z])


def ryad_sinih(y, x):
    global tri_v_ryad_sinih
    if ((x < 3 and (pole[x + 2][y] == 1 and pole[x + 1][y] == 1)) or (
            x >= 2 and pole[x - 2][y] == 1 and pole[x - 1][y] == 1) or (
                0 < x < 4 and (pole[x + 1][y] == 1 and pole[x - 1][y] == 1))) or (
            (y < 4 and (pole[x][y + 2] == 1 and pole[x][y + 1] == 1)) or (
            y >= 2 and pole[x][y - 2] == 1 and pole[x][y - 1] == 1) or (
                    0 < y <= 4 and (pole[x][y + 1] == 1 and pole[x][y - 1] == 1))):
        tri_v_ryad_sinih = True
    else:
        tri_v_ryad_sinih = False


def ryad_zelenih(y, x):
    global tri_v_ryad_zelenih
    if ((x < 3 and (pole[x + 2][y] == 2 and pole[x + 1][y] == 2)) or (
            x >= 2 and pole[x - 2][y] == 2 and pole[x - 1][y] == 2) or (
                0 < x < 4 and (pole[x + 1][y] == 2 and pole[x - 1][y] == 2))) or (
            (y < 4 and (pole[x][y + 2] == 2 and pole[x][y + 1] == 2)) or (
            y >= 2 and pole[x][y - 2] == 2 and pole[x][y - 1] == 2) or (
                    0 < y <= 4 and (pole[x][y + 1] == 2 and pole[x][y - 1] == 2))):
        tri_v_ryad_zelenih = True
    else:
        tri_v_ryad_zelenih = False


def proverka_sinie(y, x):
    global vozmozhnost_zabrat
    if (x < 3 and pole[x + 2][y] == 1 and pole[x + 1][y] == 1):
        vozmozhnost_zabrat = True
        if x != 0 and pole[x - 1][y] == 2:
            pole[x - 1][y] = 4
        if x != 2 and pole[x + 3][y] == 2:
            pole[x + 3][y] = 4
        if y > 0 and y < 5 and x < 2 and pole[x + 1][y] == 1 and pole[x + 2][y] == 1 and pole[x+3][y] == 1:
            if pole[x + 3][y+1] == 2:
                pole[x + 3][y+1] = 4
            if pole[x-3][y-1] == 2:
                pole[x-3][y-1] = 4
        if x == 0 and pole[x+1][y] == 1 and pole[x+2][y] == 1 and pole[x+3][y] == 1 and pole[x+4][y] == 2:
            pole[x+4][y] = 4
        if y != 0 and x < 2 and pole[x + 3][y] == 1 and pole[x + 3][y - 1] == 2:
            pole[x + 3][y - 1] = 4
        if y != 0 and x < 1 and pole[x + 3][y] == 1 and pole[x + 4][y] == 1 and pole[x + 4][y - 1] == 2:
            pole[x + 4][y - 1] = 4
        if y != 5 and x < 2 and pole[x + 3][y] == 1 and pole[x + 3][y + 1] == 2:
            pole[x + 3][y + 1] = 4
        if y != 5 and x < 1 and pole[x + 3][y] == 1 and pole[x + 4][y] == 1 and pole[x + 4][y + 1] == 2:
            pole[x + 4][y + 1] = 4
        if y != 0 and pole[x][y - 1] == 2:
            pole[x][y - 1] = 4
        if y != 0 and pole[x + 1][y - 1] == 2:
            pole[x + 1][y - 1] = 4
        if y != 0 and pole[x + 2][y - 1] == 2:
            pole[x + 2][y - 1] = 4
        if y != 5 and pole[x][y + 1] == 2:
            pole[x][y + 1] = 4
        if y != 5 and pole[x + 1][y + 1] == 2:
            pole[x + 1][y + 1] = 4
        if y != 5 and pole[x + 2][y + 1] == 2:
            pole[x + 2][y + 1] = 4

    if (x >= 2 and pole[x - 2][y] == 1 and pole[x - 1][y] == 1):
        vozmozhnost_zabrat = True
        if x != 2 and pole[x - 3][y] == 2:
            pole[x - 3][y] = 4
        if x != 4 and pole[x + 1][y] == 2:
            pole[x + 1][y] = 4
        if y > 0 and y < 5 and x > 2 and pole[x - 1][y] == 1 and pole[x - 2][y] == 1 and pole[x-3][y] == 1:
            if pole[x - 3][y+1] == 2:
                pole[x - 3][y+1] = 4
            if pole[x-3][y-1] == 2:
                pole[x-3][y-1] = 4
        if x == 4 and pole[x-1][y] == 1 and pole[x-2][y] == 1 and pole[x-3][y] == 1 and pole[x-4][y] == 2:
            pole[x-4][y] = 4
        if y > 0 and x > 2 and pole[x - 3][y] == 1 and pole[x - 3][y - 1] == 2:
            pole[x - 3][y - 1] = 4
        if y > 0 and x > 3 and pole[x - 3][y] == 1 and pole[x - 4][y] == 1 and pole[x - 4][y - 1] == 2:
            pole[x - 4][y - 1] = 4
        if y != 5 and x > 2 and pole[x - 3][y] == 1 and pole[x - 3][y + 1] == 2:
            pole[x - 3][y + 1] = 4
        if y != 5 and x > 3 and pole[x - 3][y] == 1 and pole[x - 4][y] == 1 and pole[x - 4][y + 1] == 2:
            pole[x - 4][y + 1] = 4
        if y != 0 and pole[x][y - 1] == 2:
            pole[x][y - 1] = 4
        if y != 0 and pole[x - 1][y - 1] == 2:
            pole[x - 1][y - 1] = 4
        if y != 0 and pole[x - 2][y - 1] == 2:
            pole[x - 2][y - 1] = 4
        if y != 5 and pole[x][y + 1] == 2:
            pole[x][y + 1] = 4
        if y != 5 and pole[x - 1][y + 1] == 2:
            pole[x - 1][y + 1] = 4
        if y != 5 and pole[x - 2][y + 1] == 2:
            pole[x - 2][y + 1] = 4

    if (0 < x < 4 and pole[x + 1][y] == 1 and pole[x - 1][y] == 1):
        vozmozhnost_zabrat = True
        if x != 1 and pole[x - 2][y] == 2:
            pole[x - 2][y] = 4
        if x != 3 and pole[x + 2][y] == 2:
            pole[x + 2][y] = 4
        if y != 0 and pole[x + 1][y - 1] == 2:
            pole[x + 1][y - 1] = 4
        if y != 0 and pole[x][y - 1] == 2:
            pole[x][y - 1] = 4
        if y != 0 and pole[x - 1][y - 1] == 2:
            pole[x - 1][y - 1] = 4
        if y != 5 and pole[x + 1][y + 1] == 2:
            pole[x + 1][y + 1] = 4
        if y != 5 and pole[x][y + 1] == 2:
            pole[x][y + 1] = 4
        if y != 5 and pole[x - 1][y + 1] == 2:
            pole[x - 1][y + 1] = 4

    if (y < 4 and pole[x][y + 2] == 1 and pole[x][y + 1] == 1):
        vozmozhnost_zabrat = True
        if y != 0 and pole[x][y - 1] == 2:
            pole[x][y - 1] = 4
        if y != 3 and pole[x][y + 3] == 2:
            pole[x][y + 3] = 4
        if y == 0 and pole[x][y+1] == 1 and pole[x][y+2] == 1 and pole[x][y+3] == 1 and pole[x][y+4] == 2:
            pole[x][y+4] = 4
        if x != 0 and y < 3 and pole[x][y + 3] == 1 and pole[x - 1][y + 3] == 2:
            pole[x - 1][y + 3] = 4
        if x != 0 and y < 2 and pole[x][y + 3] == 1 and pole[x][y + 4] == 1 and pole[x - 1][y + 4] == 2:
            pole[x - 1][y + 4] = 4
        if x != 0 and y < 1 and pole[x][y + 3] == 1 and pole[x][y + 4] == 1 and pole[x][y + 5] == 1 and pole[x - 1][y + 5] == 2:
            pole[x - 1][y + 5] = 4
        if x != 4 and y < 3 and pole[x][y + 3] == 1 and pole[x + 1][y + 3] == 2:
            pole[x + 1][y + 3] = 4
        if x != 4 and y < 2 and pole[x][y + 3] == 1 and pole[x][y + 4] == 1 and pole[x + 1][y + 4] == 2:
            pole[x + 1][y + 4] = 4
        if x != 4 and y < 1 and pole[x][y + 3] == 1 and pole[x][y + 4] == 1 and pole[x][y + 5] == 1 and pole[x + 1][y + 5] == 2:
            pole[x + 1][y + 5] = 4
        if x != 0 and pole[x - 1][y] == 2:
            pole[x - 1][y] = 4
        if x != 0 and pole[x - 1][y + 1] == 2:
            pole[x - 1][y + 1] = 4
        if x != 0 and pole[x - 1][y + 2] == 2:
            pole[x - 1][y + 2] = 4
        if x != 4 and pole[x + 1][y] == 2:
            pole[x + 1][y] = 4
        if x != 4 and pole[x + 1][y + 1] == 2:
            pole[x + 1][y + 1] = 4
        if x != 4 and pole[x + 1][y + 2] == 2:
            pole[x + 1][y + 2] = 4

    if (y >= 2 and pole[x][y - 2] == 1 and pole[x][y - 1] == 1):
        vozmozhnost_zabrat = True
        if y != 5 and pole[x][y + 1] == 2:
            pole[x][y + 1] = 4
        if y != 2 and pole[x][y - 3] == 2:
            pole[x][y - 3] = 4
        if y == 5 and pole[x][y-1] == 1 and pole[x][y-2] == 1 and pole[x][y-3] == 1 and pole[x][y-4] == 2:
            pole[x][y-4] = 4
        if x != 0 and y > 2 and pole[x][y - 3] == 1 and pole[x - 1][y - 3] == 2:
            pole[x - 1][y - 3] = 4
        if x != 0 and y > 3 and pole[x][y - 3] == 1 and pole[x][y - 4] == 1 and pole[x - 1][y - 4] == 2:
            pole[x - 1][y - 4] = 4
        if x != 0 and y > 4 and pole[x][y - 3] == 1 and pole[x][y - 4] == 1 and pole[x][y - 5] == 1 and pole[x - 1][y - 5] == 2:
            pole[x - 1][y - 5] = 4
        if x != 4 and y > 2 and pole[x][y - 3] == 1 and pole[x + 1][y - 3] == 2:
            pole[x + 1][y - 3] = 4
        if x != 4 and y > 3 and pole[x][y - 3] == 1 and pole[x][y - 4] == 1 and pole[x + 1][y - 4] == 2:
            pole[x + 1][y - 4] = 4
        if x != 4 and y > 4 and pole[x][y - 3] == 1 and pole[x][y - 4] == 1 and pole[x][y - 5] == 1 and pole[x + 1][y - 5] == 2:
            pole[x + 1][y - 5] = 4
        if x != 0 and pole[x - 1][y] == 2:
            pole[x - 1][y] = 4
        if x != 0 and pole[x - 1][y - 1] == 2:
            pole[x - 1][y - 1] = 4
        if x != 0 and pole[x - 1][y - 2] == 2:
            pole[x - 1][y - 2] = 4
        if x != 4 and pole[x + 1][y] == 2:
            pole[x + 1][y] = 4
        if x != 4 and pole[x + 1][y - 1] == 2:
            pole[x + 1][y - 1] = 4
        if x != 4 and pole[x + 1][y - 2] == 2:
            pole[x + 1][y - 2] = 4

    if (0 < y <= 4 and pole[x][y + 1] == 1 and pole[x][y - 1] == 1):
        vozmozhnost_zabrat = True
        if y != 4 and pole[x][y + 2] == 2:
            pole[x][y + 2] = 4
        if y != 1 and pole[x][y - 2] == 2:
            pole[x][y - 2] = 4
        if x != 0 and pole[x - 1][y + 1] == 2:
            pole[x - 1][y + 1] = 4
        if x != 0 and pole[x - 1][y] == 2:
            pole[x - 1][y] = 4
        if x != 0 and pole[x - 1][y - 1] == 2:
            pole[x - 1][y - 1] = 4
        if x != 4 and pole[x + 1][y + 1] == 2:
            pole[x + 1][y + 1] = 4
        if x != 4 and pole[x + 1][y] == 2:
            pole[x + 1][y] = 4
        if x != 4 and pole[x + 1][y - 1] == 2:
            pole[x + 1][y - 1] = 4

def proverka_zelenie(y, x):
    global vozmozhnost_zabrat
    if (x < 3 and pole[x + 2][y] == 2 and pole[x + 1][y] == 2):
        vozmozhnost_zabrat = True
        if x != 0 and pole[x - 1][y] == 1:
            pole[x - 1][y] = 3
        if x != 2 and pole[x + 3][y] == 1:
            pole[x + 3][y] = 3
        if y > 0 and y < 5 and x < 2 and pole[x + 1][y] == 2 and pole[x + 2][y] == 2 and pole[x+3][y] == 2:
            if pole[x + 3][y+1] == 1:
                pole[x + 3][y+1] = 3
            if pole[x+3][y-1] == 1:
                pole[x+3][y-1] = 3
        if x == 0 and pole[x+1][y] == 2 and pole[x+2][y] == 2 and pole[x+3][y] == 2 and pole[x+4][y] == 1:
            pole[x+4][y] = 3
        if y != 0 and x < 2 and pole[x + 3][y] == 2 and pole[x + 3][y - 1] == 1:
            pole[x + 3][y - 1] = 3
        if y != 0 and x < 1 and pole[x + 3][y] == 2 and pole[x + 4][y] == 2 and pole[x + 4][y - 1] == 1:
            pole[x + 4][y - 1] = 3
        if y != 5 and x < 2 and pole[x + 3][y] == 2 and pole[x + 3][y + 1] == 1:
            pole[x + 3][y + 1] = 3
        if y != 5 and x < 1 and pole[x + 3][y] == 2 and pole[x + 4][y] == 2 and pole[x + 4][y + 1] == 1:
            pole[x + 4][y + 1] = 3
        # if y != 0 and x != 0 and pole[x-1][y-1] == 2:
        #     pole[x-1][y-1] = 4
        if y != 0 and pole[x][y - 1] == 1:
            pole[x][y - 1] = 3
        if y != 0 and pole[x + 1][y - 1] == 1:
            pole[x + 1][y - 1] = 3
        if y != 0 and pole[x + 2][y - 1] == 1:
            pole[x + 2][y - 1] = 3
        # if y != 0 and x != 2 and pole[x+3][y-1] == 2:
        #     pole[x+3][y-1] = 4
        # if y != 5 and x != 0 and pole[x-1][y+1] == 2:
        #     pole[x-1][y+1] = 4
        if y != 5 and pole[x][y + 1] == 1:
            pole[x][y + 1] = 3
        if y != 5 and pole[x + 1][y + 1] == 1:
            pole[x + 1][y + 1] = 3
        if y != 5 and pole[x + 2][y + 1] == 1:
            pole[x + 2][y + 1] = 3
        # if y != 5 and x != 2 and pole[x+3][y+1] == 2:
        #     pole[x+3][y+1] = 4

    if (x >= 2 and pole[x - 2][y] == 2 and pole[x - 1][y] == 2):
        vozmozhnost_zabrat = True
        if x != 2 and pole[x - 3][y] == 1:
            pole[x - 3][y] = 3
        if x != 4 and pole[x + 1][y] == 1:
            pole[x + 1][y] = 3
        if y > 0 and y < 5 and x > 2 and pole[x - 1][y] == 2 and pole[x - 2][y] == 2 and pole[x-3][y] == 2:
            if pole[x - 3][y+1] == 1:
                pole[x - 3][y+1] = 3
            if pole[x-3][y-1] == 1:
                pole[x-3][y-1] = 3
        if x == 4 and pole[x-1][y] == 2 and pole[x-2][y] == 2 and pole[x-3][y] == 2 and pole[x-4][y] == 1:
            pole[x-4][y] = 3
        if y != 0 and x > 2 and pole[x - 3][y] == 2 and pole[x - 3][y - 1] == 1:
            pole[x - 3][y - 1] = 3
        if y != 0 and x > 3 and pole[x - 3][y] == 2 and pole[x - 4][y] == 2 and pole[x - 4][y - 1] == 1:
            pole[x - 4][y - 1] = 3
        if y != 5 and x > 2 and pole[x - 3][y] == 2 and pole[x - 3][y + 1] == 1:
            pole[x - 3][y + 1] = 3
        if y != 5 and x > 3 and pole[x - 3][y] == 2 and pole[x - 4][y] == 2 and pole[x - 4][y + 1] == 1:
            pole[x - 4][y + 1] = 3
        # if y != 0 and x != 4 and pole[x+1][y-1] == 2:
        #     pole[x+1][y-1] = 4
        if y != 0 and pole[x][y - 1] == 1:
            pole[x][y - 1] = 3
        if y != 0 and pole[x - 1][y - 1] == 1:
            pole[x - 1][y - 1] = 3
        if y != 0 and pole[x - 2][y - 1] == 1:
            pole[x - 2][y - 1] = 3
        # if y != 0 and x != 2 and pole[x-3][y-1] == 2:
        #     pole[x-3][y-1] = 4
        # if y != 5 and x != 4 and pole[x+1][y+1] == 2:
        #     pole[x+1][y+1] = 4
        if y != 5 and pole[x][y + 1] == 1:
            pole[x][y + 1] = 3
        if y != 5 and pole[x - 1][y + 1] == 1:
            pole[x - 1][y + 1] = 3
        if y != 5 and pole[x - 2][y + 1] == 1:
            pole[x - 2][y + 1] = 3
        # if y != 5 and x != 2 and pole[x-3][y+1] == 2:
        #     pole[x-3][y+1] = 4
    if (0 < x < 4 and pole[x + 1][y] == 2 and pole[x - 1][y] == 2):
        vozmozhnost_zabrat = True
        if x != 1 and pole[x - 2][y] == 1:
            pole[x - 2][y] = 3
        if x != 3 and pole[x + 2][y] == 1:
            pole[x + 2][y] = 3
        # if y != 0 and x != 3 and pole[x+2][y-1] == 2:
        #     pole[x+2][y-1] = 4
        if y != 0 and pole[x + 1][y - 1] == 1:
            pole[x + 1][y - 1] = 3
        if y != 0 and pole[x][y - 1] == 1:
            pole[x][y - 1] = 3
        if y != 0 and pole[x - 1][y - 1] == 1:
            pole[x - 1][y - 1] = 3
        # if y != 0 and x != 1 and pole[x-2][y-1] == 2:
        #     pole[x-2][y-1] = 4
        # if y != 5 and x != 3 and pole[x+2][y+1] == 2:
        #     pole[x+2][y+1] = 4
        if y != 5 and pole[x + 1][y + 1] == 1:
            pole[x + 1][y + 1] = 3
        if y != 5 and pole[x][y + 1] == 1:
            pole[x][y + 1] = 3
        if y != 5 and pole[x - 1][y + 1] == 1:
            pole[x - 1][y + 1] = 3
        # if y != 5 and x != 1 and pole[x-2][y+1] == 2:
        #     pole[x-2][y+1] = 4

    if (y < 4 and pole[x][y + 2] == 2 and pole[x][y + 1] == 2):
        vozmozhnost_zabrat = True
        if y != 0 and pole[x][y - 1] == 1:
            pole[x][y - 1] = 3
        if y != 3 and pole[x][y + 3] == 1:
            pole[x][y + 3] = 3
        if y == 0 and pole[x][y+1] == 2 and pole[x][y+2] == 2 and pole[x][y+3] == 2 and pole[x][y+4] == 1:
            pole[x][y+4] = 3
        if x != 0 and y < 3 and pole[x][y + 3] == 2 and pole[x - 1][y + 3] == 1:
            pole[x - 1][y + 3] = 3
        if x != 0 and y < 2 and pole[x][y + 3] == 2 and pole[x][y + 4] == 2 and pole[x - 1][y + 4] == 1:
            pole[x - 1][y + 4] = 3
        if x != 0 and y < 1 and pole[x][y + 3] == 2 and pole[x][y + 4] == 2 and pole[x][y + 5] == 2 and pole[x - 1][y + 5] == 1:
            pole[x - 1][y + 5] = 3
        if x != 4 and y < 3 and pole[x][y + 3] == 2 and pole[x + 1][y + 3] == 1:
            pole[x + 1][y + 3] = 3
        if x != 4 and y < 2 and pole[x][y + 3] == 2 and pole[x][y + 4] == 2 and pole[x + 1][y + 4] == 1:
            pole[x + 1][y + 4] = 3
        if x != 4 and y < 1 and pole[x][y + 3] == 2 and pole[x][y + 4] == 2 and pole[x][y + 5] == 2 and pole[x + 1][y + 5] == 1:
            pole[x + 1][y + 5] = 3
        # if x != 0 and y != 0 and pole[x-1][y-1] == 2:
        #     pole[x-1][y-1] = 4
        if x != 0 and pole[x - 1][y] == 1:
            pole[x - 1][y] = 3
        if x != 0 and pole[x - 1][y + 1] == 1:
            pole[x - 1][y + 1] = 3
        if x != 0 and pole[x - 1][y + 2] == 1:
            pole[x - 1][y + 2] = 3
        # if x != 0 and y != 3 and pole[x-1][y+3] == 2:
        #     pole[x-1][y+3] = 4
        # if x != 4 and y != 0 and pole[x+1][y-1] == 2:
        #     pole[x+1][y-1] = 4
        if x != 4 and pole[x + 1][y] == 1:
            pole[x + 1][y] = 3
        if x != 4 and pole[x + 1][y + 1] == 1:
            pole[x + 1][y + 1] = 3
        if x != 4 and pole[x + 1][y + 2] == 1:
            pole[x + 1][y + 2] = 3
        # if x != 4 and y != 3 and pole[x+1][y+3] == 2:
        #     pole[x+1][y+3] = 4

    if (y >= 2 and pole[x][y - 2] == 2 and pole[x][y - 1] == 2):
        vozmozhnost_zabrat = True
        if y != 5 and pole[x][y + 1] == 1:
            pole[x][y + 1] = 3
        if y != 2 and pole[x][y - 3] == 1:
            pole[x][y - 3] = 3
        if y == 5 and pole[x][y-1] == 2 and pole[x][y-2] == 2 and pole[x][y-3] == 2 and pole[x][y-4] == 1:
            pole[x][y-4] = 3
        if x != 0 and y > 2 and pole[x][y - 3] == 2 and pole[x - 1][y - 3] == 1:
            pole[x - 1][y - 3] = 3
        if x != 0 and y > 3 and pole[x][y - 3] == 2 and pole[x][y - 4] == 2 and pole[x - 1][y - 4] == 1:
            pole[x - 1][y - 4] = 3
        if x != 0 and y > 4 and pole[x][y - 3] == 2 and pole[x][y - 4] == 2 and pole[x][y - 5] == 2 and pole[x - 1][y - 5] == 1:
            pole[x - 1][y - 5] = 3

        if x != 4 and y > 2 and pole[x][y - 3] == 2 and pole[x + 1][y - 3] == 1:
            pole[x + 1][y - 3] = 3
        if x != 4 and y > 3 and pole[x][y - 3] == 2 and pole[x][y - 4] == 2 and pole[x + 1][y - 4] == 1:
            pole[x + 1][y - 4] = 3
        if x != 4 and y > 4 and pole[x][y - 3] == 2 and pole[x][y - 4] == 2 and pole[x][y - 5] == 2 and pole[x + 1][y - 5] == 1:
            pole[x + 1][y - 5] = 3
        # if x != 0 and y != 5 and pole[x - 1][y + 1] == 2:
        #     pole[x - 1][y + 1] = 4
        if x != 0 and pole[x - 1][y] == 1:
            pole[x - 1][y] = 3
        if x != 0 and pole[x - 1][y - 1] == 1:
            pole[x - 1][y - 1] = 3
        if x != 0 and pole[x - 1][y - 2] == 1:
            pole[x - 1][y - 2] = 3
        # if x != 0 and y != 2 and pole[x - 1][y - 3] == 2:
        #     pole[x - 1][y - 3] = 4
        # if x != 4 and y != 5 and pole[x + 1][y + 1] == 2:
        #     pole[x + 1][y + 1] = 4
        if x != 4 and pole[x + 1][y] == 1:
            pole[x + 1][y] = 3
        if x != 4 and pole[x + 1][y - 1] == 1:
            pole[x + 1][y - 1] = 3
        if x != 4 and pole[x + 1][y - 2] == 1:
            pole[x + 1][y - 2] = 3
        # if x != 4 and y != 2 and pole[x + 1][y - 3] == 2:
        #     pole[x + 1][y - 3] = 4

    if (0 < y <= 4 and pole[x][y + 1] == 2 and pole[x][y - 1] == 2):
        vozmozhnost_zabrat = True
        if y != 4 and pole[x][y + 2] == 1:
            pole[x][y + 2] = 3
        if y != 1 and pole[x][y - 2] == 1:
            pole[x][y - 2] = 3
        # if x != 0 and y != 4 and pole[x - 1][y + 2] == 2:
        #     pole[x - 1][y + 2] = 4
        if x != 0 and pole[x - 1][y + 1] == 1:
            pole[x - 1][y + 1] = 3
        if x != 0 and pole[x - 1][y] == 1:
            pole[x - 1][y] = 3
        if x != 0 and pole[x - 1][y - 1] == 1:
            pole[x - 1][y - 1] = 3
        # if x != 0 and y != 1 and pole[x - 1][y - 2] == 2:
        #     pole[x - 1][y - 2] = 4
        # if x != 4 and y != 4 and pole[x + 1][y + 2] == 2:
        #     pole[x + 1][y + 2] = 4
        if x != 4 and pole[x + 1][y + 1] == 1:
            pole[x + 1][y + 1] = 3
        if x != 4 and pole[x + 1][y] == 1:
            pole[x + 1][y] = 3
        if x != 4 and pole[x + 1][y - 1] == 1:
            pole[x + 1][y - 1] = 3
        # if x != 4 and y != 1 and pole[x + 1][y - 2] == 2:
        #     pole[x + 1][y - 2] = 4


def vozmozhnost_hodit(x, y):
    global vozmozhnost_shodit
    global prev_coord_x
    global prev_coord_y
    if (Stage_1 == False and Stage_2 == True and pole[y][x]) != 0:
        if (pole[y][x] == 0) or (y < 4 and pole[y + 1][x] == 0) or (y > 0 and pole[y - 1][x] == 0) or (x < 5 and pole[y][x + 1] == 0) or (x > 0 and pole[y][x - 1] == 0):
            vozmozhnost_shodit = True
        else:
            vozmozhnost_shodit = False
        prev_coord_x = x
        prev_coord_y = y


def click_event(event):
    global blue_count
    global green_count
    global hod_igroka
    global blue
    global green
    global pole
    global tri_v_ryad_sinih
    global tri_v_ryad_zelenih
    global chetire_v_ryad_sinih
    global Stage_1
    global Stage_2
    global vozmozhnost_shodit
    global vozmozhnost_zabrat
    global prev_coord_x
    global prev_coord_y
    global winner

    if 0 < event.x <= 595:  # Если кликнули на доске
        x = event.x // 100
        y = event.y // 100
        ryad_sinih(x, y)
        ryad_zelenih(x, y)
        if tri_v_ryad_sinih == True and hod_igroka == True and Stage_1 == True and pole[y][x] == 0:
            messagebox.showinfo(title='Предупреждение', message='Нельзя ставить 3 фигуры в ряд на первой стадии игры.',
                                icon='info')
        elif tri_v_ryad_zelenih == True and hod_igroka == False and Stage_1 == True and pole[y][x] == 0:
            messagebox.showinfo(title='Предупреждение', message='Нельзя ставить 3 фигуры в ряд на первой стадии игры.',
                                icon='info')
        if blue_count != 12 and hod_igroka == True and Stage_1 == True and Stage_2 == False and tri_v_ryad_sinih != True:  # Если остались доступные синие фигуры и наш ход и первая стадия игры
            if pole[y][x] != 1 and pole[y][x] != 2:  # Если клетка не занята
                board.create_image(event.x // 100 * 100, event.y // 100 * 100, anchor=NW,
                                   image=figuri[1])  # Определеям место клика и рисуем синюю фигуру
                blue_count += 1  # Вычитаем из кол-ва доступных фигур
                pole[y][x] = 1  # Определяем клетку как занятую синей фигурой
                blue += 1  # Пока не сделаем 2 хода

                if blue == 2:
                    hod_igroka = False
                    blue = 0
                    if AI:
                        for k in range(2):
                            if green_count != 12:
                                while True:
                                    i = random.randint(0, 4)
                                    j = random.randint(0, 5)
                                    if pole[i][j] == 0:
                                        ryad_zelenih(j,i)
                                        if tri_v_ryad_zelenih == False:# чтобы ИИ не ставил 3 зелёные в ряд
                                            pole[i][j] = 2
                                            green_count += 1
                                            green += 1
                                            vivod(-1, -1)
                                            if green == 2:
                                                green = 0
                                                hod_igroka = True
                                            break
                            else:
                                if blue_count == green_count == 12:
                                    Stage_1 = False
                                    Stage_2 = True
                                    vivod(-1,-1)
                vivod(-1,-1)

        elif green_count != 12 and hod_igroka == False and Stage_1 == True and tri_v_ryad_zelenih != True and AI == False:  # Если
            # остались доступные зелёные фигуры и наш ход и первая стадия игры
            if pole[y][x] != 1 and pole[y][x] != 2:  # Если клетка не занята
                board.create_image(event.x // 100 * 100, event.y // 100 * 100, anchor=NW, image=figuri[2])
                green_count += 1  # Вычитаем из кол-ва доступных фигур
                pole[y][x] = 2  # Определяем клетку как занятую зелёной фигурой
                green += 1  # Пока не сделаем 2 хода
                if green == 2:
                    hod_igroka = True
                    green = 0
                vivod(-1,-1)

        if blue_count == green_count == 12:
            Stage_1 = False
            Stage_2 = True
            vivod(-1,-1)

        if Stage_1 == False and Stage_2 == True and hod_igroka == True:
            vozmozhnost_hodit(x, y)
            vivod(-1,- 1)
            if pole[y][x] == 1:
                if x > 0 and pole[y][x - 1] == 0 and vozmozhnost_zabrat == False:
                    board.create_rectangle(x * 100, y * 100 + 100, x * 100 - 100, y * 100, width=4, outline="Green")
                if x < 5 and pole[y][x + 1] == 0 and vozmozhnost_zabrat == False:
                    board.create_rectangle(x * 100 + 200, y * 100 + 100, x * 100 + 100, y * 100, width=4, outline="Green")
                if y > 0 and pole[y - 1][x] == 0 and vozmozhnost_zabrat == False:
                    board.create_rectangle(x * 100 + 100, y * 100 - 100, x * 100, y * 100, width=4, outline="Green")
                if y < 4 and pole[y + 1][x] == 0 and vozmozhnost_zabrat == False:
                    board.create_rectangle(x * 100 + 100, y * 100 + 200, x * 100, y * 100 + 100, width=4, outline="Green")
                board.create_rectangle(x * 100 + 100, y * 100 + 100, x * 100, y * 100, width=4, outline="Blue")

            if (pole[prev_coord_y][prev_coord_x] != 0 and prev_coord_x + 1 == x and prev_coord_y == y) or (
                    prev_coord_x - 1 == x and prev_coord_y == y) or (
                    prev_coord_y + 1 == y and prev_coord_x == x) or (
                    prev_coord_y - 1 == y and prev_coord_x == x):  # Проверяем, сходили ли мы на одну клетку
                # вертикально или горизонтально
                if vozmozhnost_shodit == True and pole[y][x] == 0 and hod_igroka == True:
                    vivod(-1, -1)

                    if pole[prev_coord_y][prev_coord_x] == 1:
                        pole[y][x] = 1
                        pole[prev_coord_y][prev_coord_x] = 0
                        proverka_sinie(x, y)
                        vivod(-1, -1)  # рисуем игровое поле
                        if str(pole).count('4') == 0:
                            vozmozhnost_shodit = False
                            hod_igroka = False
                            vivod(-1,-1)
                            if AI:
                                prev_x = 0
                                prev_y = 0
                                xx,yy = 0,0
                                while vozmozhnost_shodit != True:
                                    c= 0
                                    l = random.randint(1, str(pole).count('2'))
                                    for i in range(5):
                                        for j in range(6):
                                            if pole[i][j] == 2 and c != l:
                                                c += 1
                                                if c == l:
                                                    prev_x = i
                                                    prev_y = j
                                                    vozmozhnost_hodit(prev_y,prev_x)

                                    if vozmozhnost_shodit:
                                        if (prev_x > 0 and prev_y < 4 and pole[prev_x - 1][prev_y] == 0 and pole[prev_x - 1][prev_y + 1] == 2 and pole[prev_x - 1][prev_y + 2] == 2) or (0 < prev_y < 5 and prev_x > 0 and pole[prev_x - 1][prev_y] == 0 and pole[prev_x - 1][prev_y - 1] == 2 and pole[prev_x - 1][prev_y + 1] == 2) or (prev_x > 0 and prev_y > 1 and pole[prev_x - 1][prev_y] == 0 and pole[prev_x - 1][prev_y - 1] == 2 and pole[prev_x - 1][prev_y - 2] == 2) or (prev_x > 2 and pole[prev_x- 1][prev_y] == 0 and pole[prev_x - 2][prev_y] == 2 and pole[prev_x - 3][prev_y] == 2):
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x - 1][prev_y] = 2
                                            xx = prev_x - 1
                                            yy = prev_y
                                        elif (prev_x < 4 and prev_y < 4 and pole[prev_x + 1][prev_y] == 0 and pole[prev_x + 1][prev_y + 1] == 2 and pole[prev_x + 1][prev_y + 2] == 2) or (0 < prev_y < 5 and prev_x < 4 and pole[prev_x + 1][prev_y] == 0 and pole[prev_x + 1][prev_y - 1] == 2 and pole[prev_x + 1][prev_y + 1] == 2) or (prev_x < 4 and prev_y > 1 and pole[prev_x + 1][prev_y] == 0 and pole[prev_x + 1][prev_y - 1] == 2 and pole[prev_x + 1][prev_y - 2] == 2) or (prev_x < 2 and pole[prev_x + 1][prev_y] == 0 and pole[prev_x + 2][prev_y] == 2 and pole[prev_x + 3][prev_y] == 2):
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x + 1][prev_y] = 2
                                            xx = prev_x + 1
                                            yy = prev_y
                                        elif (prev_y > 2 and pole[prev_x][prev_y - 1] == 0 and pole[prev_x][prev_y - 2] == 2 and pole[prev_x][prev_y - 3] == 2) or (prev_y > 0 and prev_x > 1 and pole[prev_x - 1][prev_y - 1] == 2 and pole[prev_x][prev_y - 1] == 0 and pole[prev_x - 2][prev_y - 1] == 2) or (prev_y > 0 and prev_x < 3 and pole[prev_x + 1][prev_y - 1] == 2 and pole[prev_x][prev_y - 1] == 0 and pole[prev_x + 2][prev_y - 1] == 2) or (prev_x > 0 and prev_x < 4 and prev_y > 0 and pole[prev_x][prev_y - 1] == 0 and pole[prev_x - 1][prev_y - 1] == 2 and pole[prev_x + 1][prev_y - 1] == 2):
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x][prev_y - 1] = 2
                                            xx = prev_x
                                            yy = prev_y - 1
                                        elif (prev_y < 3 and pole[prev_x][prev_y + 1] == 0 and pole[prev_x][prev_y + 2] == 2 and pole[prev_x][prev_y + 3] == 2) or (prev_y < 5 and prev_x > 1 and pole[prev_x - 1][prev_y + 1] == 2 and pole[prev_x][prev_y + 1] == 0 and pole[prev_x - 2][prev_y + 1] == 2) or (prev_y < 5 and prev_x < 3 and pole[prev_x + 1][prev_y + 1] == 2 and pole[prev_x][prev_y + 1] == 0 and pole[prev_x + 2][prev_y + 1] == 2) or (prev_x > 0 and prev_x < 4 and prev_y < 5 and pole[prev_x][prev_y + 1] == 0 and pole[prev_x - 1][prev_y + 1] == 2 and pole[prev_x + 1][prev_y + 1] == 2):
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x][prev_y + 1] = 2
                                            xx = prev_x
                                            yy = prev_y + 1
                                        elif prev_y < 5 and pole[prev_x][prev_y + 1] == 0 and pole[prev_x][prev_y] == 2:
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x][prev_y + 1] = 2
                                            xx = prev_x
                                            yy = prev_y + 1
                                        elif prev_y > 0 and pole[prev_x][prev_y - 1] == 0 and pole[prev_x][prev_y] == 2:
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x][prev_y - 1] = 2
                                            xx = prev_x
                                            yy = prev_y - 1
                                        elif prev_x < 4 and pole[prev_x + 1][prev_y] == 0 and pole[prev_x][prev_y] == 2:
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x + 1][prev_y] = 2
                                            xx = prev_x + 1
                                            yy = prev_y
                                        elif prev_x > 0 and pole[prev_x - 1][prev_y] == 0 and pole[prev_x][prev_y] == 2:
                                            pole[prev_x][prev_y] = 0
                                            pole[prev_x - 1][prev_y] = 2
                                            xx = prev_x - 1
                                            yy = prev_y
                                        proverka_zelenie(yy,xx)
                                        vivod(-1,-1)
                                        hod_igroka = True
                                        vivod(-1, -1)
                                        if str(pole).count('3') == 0:
                                            vozmozhnost_shodit = False
                                            hod_igroka = True
                                            vivod(-1, -1)
                                        if str(pole).count('3') > 0 and vozmozhnost_zabrat:
                                            vozmozhnost_shodit = False
                                            c = 0
                                            k = random.randint(1, str(pole).count('3'))
                                            for i in range(5):
                                                for j in range(6):
                                                    if pole[i][j] == 3 and c != k:
                                                        c += 1
                                                        if c == k:
                                                            prev_x = i
                                                            prev_y = j
                                            if pole[prev_x][prev_y] == 3:
                                                pole[prev_x][prev_y] = 0
                                                blue_count -= 1
                                                for y in range(5):
                                                    for x in range(6):
                                                        if pole[y][x] == 3:
                                                            pole[y][x] = 1
                                                vivod(-1, -1)
                                                vozmozhnost_zabrat = False
                                                if blue_count == 2:
                                                    messagebox.showinfo(title='Победа зеленых', message='Победили зеленые.',
                                                                        icon='info')
                                                    winner = "Зеленые"
                                                    Start_new()
                                                    hod_igroka = True
                                                hod_igroka = True
                                        break

        if vozmozhnost_zabrat and hod_igroka and str(pole).count('4') > 0:
            vozmozhnost_shodit = False
            if pole[y][x] == 4:
                pole[y][x] = 0
                green_count -= 1
                for y in range(5):
                    for x in range(6):
                        if pole[y][x] == 4:
                            pole[y][x] = 2
                vivod(-1, -1)
                vozmozhnost_zabrat = False
                if green_count == 2:
                    messagebox.showinfo(title='Победа синих', message='Победили синие.', icon='info')
                    winner = "Синие"
                    Start_new()
                    hod_igroka = True
                vivod(-1,-1)
                if AI:
                    vozmozhnost_shodit = False
                    prev_x = 0
                    prev_y = 0
                    xx, yy = 0, 0
                    while vozmozhnost_shodit != True:
                        c = 0
                        l = random.randint(1, str(pole).count('2'))
                        for i in range(5):
                            for j in range(6):
                                if pole[i][j] == 2 and c != l:
                                    c += 1
                                    if c == l:
                                        prev_x = i
                                        prev_y = j
                                        vozmozhnost_hodit(prev_y, prev_x)

                        if vozmozhnost_shodit:
                            if prev_y < 5 and pole[prev_x][prev_y + 1] == 0 and pole[prev_x][prev_y] == 2:
                                pole[prev_x][prev_y] = 0
                                pole[prev_x][prev_y + 1] = 2
                                xx = prev_x
                                yy = prev_y + 1
                            elif prev_y > 0 and pole[prev_x][prev_y - 1] == 0 and pole[prev_x][prev_y] == 2:
                                pole[prev_x][prev_y] = 0
                                pole[prev_x][prev_y - 1] = 2
                                xx = prev_x
                                yy = prev_y - 1
                            elif prev_x < 4 and pole[prev_x + 1][prev_y] == 0 and pole[prev_x][prev_y] == 2:
                                pole[prev_x][prev_y] = 0
                                pole[prev_x + 1][prev_y] = 2
                                xx = prev_x + 1
                                yy = prev_y
                            elif prev_x > 0 and pole[prev_x - 1][prev_y] == 0 and pole[prev_x][prev_y] == 2:
                                pole[prev_x][prev_y] = 0
                                pole[prev_x - 1][prev_y] = 2
                                xx = prev_x - 1
                                yy = prev_y
                            proverka_zelenie(yy, xx)
                            vivod(-1, -1)
                            hod_igroka = True
                            vivod(-1, -1)
                            if str(pole).count('3') == 0:
                                vozmozhnost_shodit = False
                                hod_igroka = True
                                vivod(-1, -1)
                            if str(pole).count('3') > 0 and vozmozhnost_zabrat:
                                vozmozhnost_shodit = False
                                c = 0
                                k = random.randint(1, str(pole).count('3'))
                                for i in range(5):
                                    for j in range(6):
                                        if pole[i][j] == 3 and c != k:
                                            c += 1
                                            if c == k:
                                                prev_x = i
                                                prev_y = j
                                if pole[prev_x][prev_y] == 3:
                                    pole[prev_x][prev_y] = 0
                                    blue_count -= 1
                                    for y in range(5):
                                        for x in range(6):
                                            if pole[y][x] == 3:
                                                pole[y][x] = 1
                                    vivod(-1, -1)
                                    vozmozhnost_zabrat = False
                                    if blue_count == 2:
                                        messagebox.showinfo(title='Победа зеленых', message='Победили зеленые.',
                                                            icon='info')
                                        winner = "Зеленые"
                                        Start_new()
                                        hod_igroka = True
                                    hod_igroka = True
                            break

        elif Stage_1 == False and Stage_2 == True and hod_igroka == False and AI == False:
            vozmozhnost_hodit(x, y)
            if (prev_coord_x + 1 == x and prev_coord_y == y) or (prev_coord_x - 1 == x and prev_coord_y == y) or (
                    prev_coord_y + 1 == y and prev_coord_x == x) or (
                    prev_coord_y - 1 == y and prev_coord_x == x):  # Проверяем, сходили ли мы на одну клетку
                # вертикально или горизонтально
                if vozmozhnost_shodit == True and pole[y][x] == 0 and hod_igroka == False:
                    if pole[prev_coord_y][prev_coord_x] == 2:
                        pole[y][x] = 2
                        pole[prev_coord_y][prev_coord_x] = 0
                        proverka_zelenie(x, y)
                        vivod(-1, -1)  # рисуем игровое поле
                        if str(pole).count('3') == 0:
                            vozmozhnost_shodit = False
                            hod_igroka = True
                            vivod(-1,-1)

        if vozmozhnost_zabrat and hod_igroka == False and str(pole).count('3') > 0 and AI == False:
            vozmozhnost_shodit = False
            if pole[y][x] == 3:
                pole[y][x] = 0
                blue_count -= 1
                for y in range(5):
                    for x in range(6):
                        if pole[y][x] == 3:
                            pole[y][x] = 1
                vivod(-1, -1)
                vozmozhnost_zabrat = False
                if blue_count == 2:
                    messagebox.showinfo(title='Победа зелёных', message='Победили зелёные.', icon='info')
                    winner = "Зеленые"
                    Start_new()
                hod_igroka = True


class Ui_LoginForm(object):

    def Close(self):
        exit()
    def Correct(self):

        u_ind = 0
        p_ind = 0
        cipher = ''
        for letter in self.lineEdit.text():
            if letter != ' ':
                try:
                    cipher += MORSE_CODE_DICT[letter] + ' '
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введены некорректные символы")
                    msg.setWindowTitle("Неправильные символы")
                    msg.exec_()
                    break;
            else:

                try:
                    cipher += ' '
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введены некорректные символы")
                    msg.setWindowTitle("Неправильные символы")
                    msg.exec_()
                    break;
        word = cipher

        with open(r'username.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                line = ('\n'.join(filter(bool, line.split('\n'))))
                u_ind +=1
                if (word == line):
                    self.u_ind = u_ind
                    break;
                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Поле Username или Password не может быть пустым")
                    msg.setWindowTitle("Пустое поле")
                    msg.exec_()
                    break;

        p_cipher = ''
        for p_letter in self.lineEdit_2.text():
            if p_letter != ' ':
                try:
                    p_cipher += MORSE_CODE_DICT[p_letter] + ' '
                except:

                    break;
            else:
                try:
                    p_cipher += ' '
                except:
                    break;
        p_word = p_cipher


        with open(r'password.txt', 'r') as fp:
            # read all lines in a list
            p_lines = fp.readlines()
            for p_line in p_lines:
                p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                p_ind +=1
                if (p_word == p_line):
                    self.p_ind = p_ind

                    if self.p_ind == self.u_ind:
                        break


                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    break;

        try:
            if (p_word == p_line) and (word == line):
                pass
        except:
            line = ""
            p_line = ""
        if (p_word == p_line) and (word == line):
            if ((p_ind == u_ind) and ((p_ind or u_ind) != 0)):
                global Username
                Username = cipher
                LoginForm.close()
                PersonalAccount.show()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.instance = Ui_PersonalAccount()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Вы успешно вошли.")
                msg.setWindowTitle("Успешный вход")
                msg.exec_()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Такой Username или Password не существует")
                msg.setWindowTitle("Неправильные данные")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Такой Username или Password не существует")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()



    def encryptUser(self):

        cipher = ''
        for letter in self.lineEdit.text():
            if letter != ' ':
                try:
                    cipher += MORSE_CODE_DICT[letter] + ' '
                except:
                    break;
            else:
                # 1 пробел для разделения букв
                # 2 пробела для разделения слов
                try:
                    cipher += ' '
                except:
                    break;
        word = cipher
        def english(string):
                for char in string:
                    if (ord(char) <= 122 and ord(char) >= 65):
                        return True
                        break
                return False

        result = english(self.lineEdit.text())
        with open(r'username.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                line = ('\n'.join(filter(bool, line.split('\n'))))
                if word == line or word == "" or (self.lineEdit_2.text() == "" or result == True):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введены неправильные данные либо данные уже существуют. Разрешён ввод только русских букв, цифр и некоторых знаков препинания")
                    msg.setWindowTitle("Неправильные данные")
                    msg.exec_()
                    break;
            else:

                with open("username.txt", 'a', encoding='utf-8') as file:
                            file.write(f'{cipher}\n')
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Вы успешно зарегистрировались")
                            msg.setWindowTitle("Успешная регистрация")
                            msg.exec_()


        p_cipher = ''
        for p_letter in self.lineEdit_2.text():
            if p_letter != ' ':
                try:
                    p_cipher += MORSE_CODE_DICT[p_letter] + ' '
                except:
                    break;
            else:
                # 1 пробел для разделения букв
                # 2 пробела для разделения слов
                try:
                    p_cipher += ' '
                except:
                    break;
        p_word = p_cipher
        with open(r'password.txt', 'r') as fp_file:
            # read all lines in a list
            p_lines = fp_file.readlines()
            for p_line in p_lines:
                p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                if word == line or word == "" or self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                    break;
            else:

                with open("password.txt", 'a', encoding='utf-8') as p_file:
                    p_file.write(f'{p_cipher}\n')
        return cipher


    def setupUi(self, LoginForm):

        LoginForm.setObjectName("LoginForm")
        LoginForm.setWindowIcon(QtGui.QIcon('verify.png'))
        LoginForm.resize(450, 550)
        LoginForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(LoginForm)
        self.widget.setGeometry(QtCore.QRect(20, 20, 370, 480))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("background-image: url(background.jpeg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 140, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118. 132, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 210, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118. 132, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 280, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(61, 169, 208, 255), stop: 1 rgba(78, 73, 197, 255));\n"
"    color: rgba(255, 255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
#################################Button Event#######################

        self.pushButton.clicked.connect(self.Correct)
####################################################################
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"    color: rgb(255, 255,255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{    \n"
"    background-color: rgb(255,0,0);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-top:5px;\n"
"    background-color: rgb(155,0,40);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
#################################Button Event#######################
        self.pushButton_2.clicked.connect(self.Close)
####################################################################
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 320, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(61, 169, 208, 255), stop: 1 rgba(78, 73, 197, 255));\n"
"    color: rgba(255, 255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_4:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
##########################################################
        self.pushButton_4.clicked.connect(self.encryptUser)
##########################################################

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)




    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Авторизация"))
        self.label_2.setText(_translate("LoginForm", "Login"))
        self.lineEdit.setPlaceholderText(_translate("LoginForm", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("LoginForm", "Password"))
        self.pushButton.setText(_translate("LoginForm", "Войти"))
        self.pushButton_2.setText(_translate("LoginForm", "X"))
        self.pushButton_4.setText(_translate("LoginForm", "Зарегистрироваться"))
#import res_rc


#################################################################################################################################################################################
##################################################################################################################################################################################
###################################################################################################################################################################################

class Ui_PersonalAccount(object):
    def Play(self):
        global running
        running = True
        tk.deiconify()
        PersonalAccount.hide()
        izobrazheniya_figur()  # здесь загружаем изображения пешек
        novaya_igra()  # начинаем новую игру
        vivod(-1, -1)  # рисуем игровое поле
        board.bind("<Button-1>", click_event)  # нажатие левой кнопки
        tk.protocol("WM_DELETE_WINDOW", on_closing)
        mainloop()
    def ToLoginForm(self):
        PersonalAccount.close()
        LoginForm.show()

    def setupUi(self, PersonalAccount):
        PersonalAccount.setObjectName("PersonalAccount")
        PersonalAccount.setWindowIcon(QtGui.QIcon('avatar.png'))
        PersonalAccount.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        PersonalAccount.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        PersonalAccount.resize(643, 655)
        self.widget_10 = QtWidgets.QWidget(PersonalAccount)
        self.widget_10.setGeometry(QtCore.QRect(30, 30, 571, 591))
        self.widget_10.setObjectName("widget_10")
        self.label_11 = QtWidgets.QLabel(self.widget_10)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 461, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("background-image: url(backgrnd.jpg);\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 50px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.widget_10)
        self.label_10.setGeometry(QtCore.QRect(200, 0, 401, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255,255,255);")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.widget_10)
        self.label_12.setGeometry(QtCore.QRect(190, 100, 500, 351))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255,255,255);")

        self.label_12.setObjectName("label_12")

        self.pushButton_10 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton#pushButton_10{\n"
"    color: rgb(255, 255,255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_10:hover{    \n"
"    background-color: rgb(255,0,0);\n"
"}\n"
"QPushButton#pushButton_10:pressed{\n"
"    padding-top:5px;\n"
"    background-color: rgb(155,0,40);\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
#######################################################################################################################################
        self.pushButton_10.clicked.connect(self.ToLoginForm)
######################################################################################################################################

        self.pushButton_11 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 460, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11{\n"
"    background-color: rgba(255,80,80,240);\n"
"    color: rgba(0, 0,0,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_11:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton_11:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
#####################################################################################
        self.pushButton_11.clicked.connect(self.Play)
#####################################################################################
######################################################################


        self.retranslateUi(PersonalAccount)
        QtCore.QMetaObject.connectSlotsByName(PersonalAccount)


    def retranslateUi(self, PersonalAccount):


        _translate = QtCore.QCoreApplication.translate
        PersonalAccount.setWindowTitle(_translate("PersonalAccount", "Личный кабинет"))
        self.label_10.setText(_translate("PersonalAccount", "Статистика"))
        self.label_12.setText(_translate("PersonalAccount", "Последний результат:" ))
        self.pushButton_10.setText(_translate("PersonalAccount", "Выйти"))
        self.pushButton_11.setText(_translate("PersonalAccount", "Играть"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    PersonalAccount = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    qi = Ui_PersonalAccount()
    ui.setupUi(LoginForm)
    qi.setupUi(PersonalAccount)
    LoginForm.show()
    sys.exit(app.exec_())
