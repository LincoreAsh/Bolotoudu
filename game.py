from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *


tk = Tk()  # Создаём окно
tk.title('Болотуду')  # Заголовок окна
board = Canvas(tk, width=595, height=495, bg='#FFFFFF')
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

def Start_new():
    if askyesno("Игра закончена", "Хотите выйти?"):
        tk.destroy()
def izobrazheniya_figur():  # загружаем изображения фигур
    global figuri
    i1 = PhotoImage(file="res\\Blue.png")
    i2 = PhotoImage(file="res\\Green.png")
    i3 = PhotoImage(file="res\\BlueGray.png")
    i4 = PhotoImage(file="res\\GreenGray.png")
    figuri = [0, i1, i2, i3, i4]


def novaya_igra():  # начинаем новую игру
    global pole
    pole = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]


def vivod(x_poz_1, y_poz_1):  # рисуем игровое поле
    global figuri
    global pole
    k = 100
    x = 0
    board.delete('all')

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
                1 < x < 4 and (pole[x + 1][y] == 2 and pole[x - 1][y] == 2))) or (
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
        if y !=0 and y != 5 and pole[x + 1][y] == 1 and pole[x + 2][y] == 1 and pole[x+3][y] == 1:
            if pole[x + 3][y+1] == 2:
                pole[x + 3][y+1] = 4
            if pole[x+3][y-1] == 2:
                pole[x+3][y-1] = 4
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
        if y !=0 and y != 5 and pole[x - 1][y] == 1 and pole[x - 2][y] == 1 and pole[x-3][y] == 1:
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
            pole[x - 3][y - 1] = 4
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
            pole[x][y - 2] = 2
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
        if y != 0 and y != 5 and pole[x + 1][y] == 2 and pole[x + 2][y] == 2 and pole[x+3][y] == 2:
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
        if y != 0 and y != 5 and pole[x - 1][y] == 2 and pole[x - 2][y] == 2 and pole[x-3][y] == 2:
            if pole[x - 3][y+1] == 1:
                pole[x + 3][y+1] = 3
            if pole[x-3][y-1] == 1:
                pole[x-3][y-1] = 3
        if x == 4 and pole[x-1][y] == 2 and pole[x-2][y] == 2 and pole[x-3][y] == 2 and pole[x-4][y] == 1:
            pole[x-4][y] = 3
        if y != 0 and x > 2 and pole[x - 3][y] == 2 and pole[x - 3][y - 1] == 1:
            pole[x - 3][y - 1] = 3
        if y != 0 and x > 3 and pole[x - 3][y] == 2 and pole[x - 4][y] == 2 and pole[x - 4][y - 1] == 1:
            pole[x - 4][y - 1] = 3
        if y != 5 and x > 2 and pole[x - 3][y] == 2 and pole[x - 3][y + 1] == 1:
            pole[x - 3][y - 1] = 3
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
        if (pole[y][x] == 0 or y < 4 and pole[y + 1][x] == 0 or pole[y - 1][x] == 0 or x < 5 and pole[y][x + 1] == 0 or
                pole[y][x - 1] == 0):
            prev_coord_x = x
            prev_coord_y = y
            vozmozhnost_shodit = True
        else:
            vozmozhnost_shodit = False


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

    if 0 < event.x < 600:  # Если кликнули на доске
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

        elif green_count != 12 and hod_igroka == False and Stage_1 == True and tri_v_ryad_zelenih != True:  # Если
            # остались доступные зелёные фигуры и наш ход и первая стадия игры
            if pole[y][x] != 1 and pole[y][x] != 2:  # Если клетка не занята
                board.create_image(event.x // 100 * 100, event.y // 100 * 100, anchor=NW, image=figuri[2])
                green_count += 1  # Вычитаем из кол-ва доступных фигур
                pole[y][x] = 2  # Определяем клетку как занятую зелёной фигурой
                green += 1  # Пока не сделаем 2 хода
                if green == 2:
                    hod_igroka = True
                    green = 0

        if blue_count == green_count == 12:
            Stage_1 = False
            Stage_2 = True

        if Stage_1 == False and Stage_2 == True and hod_igroka == True:
            vozmozhnost_hodit(x, y)
            if (pole[prev_coord_y][prev_coord_x] != 0 and prev_coord_x + 1 == x and prev_coord_y == y) or (
                    prev_coord_x - 1 == x and prev_coord_y == y) or (
                    prev_coord_y + 1 == y and prev_coord_x == x) or (
                    prev_coord_y - 1 == y and prev_coord_x == x):  # Проверяем, сходили ли мы на одну клетку
                # вертикально или горизонтально
                if vozmozhnost_shodit == True and pole[y][x] == 0 and hod_igroka == True:
                    if pole[prev_coord_y][prev_coord_x] == 1:
                        pole[y][x] = 1
                        pole[prev_coord_y][prev_coord_x] = 0
                        proverka_sinie(x, y)
                        vivod(-1, -1)  # рисуем игровое поле
                        if str(pole).count('4') == 0:
                            vozmozhnost_shodit = False
                            hod_igroka = False

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
                    Start_new()
                hod_igroka = False

        elif Stage_1 == False and Stage_2 == True and hod_igroka == False:
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

        if vozmozhnost_zabrat and hod_igroka == False and str(pole).count('3') > 0:
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
                    Start_new()
                hod_igroka = True


izobrazheniya_figur()  # здесь загружаем изображения пешек
novaya_igra()  # начинаем новую игру
vivod(-1, -1)  # рисуем игровое поле
board.bind("<Button-1>", click_event)  # нажатие левой кнопки

mainloop()
