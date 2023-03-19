# 1
# Напишите программу, которая считывает N значений от пользователя в поле Entry, 
# после ввода значений необходимо посчитать сред. арифметическое по нажатию на кнопку 
# и вывести в поле Label
# 1 2 3 4 5

# 2
# Игра - угадай число. 
# В программе задано число, пользователь должен его угадать
# Если введенное число > чем загаданное, то просим уменьшить введеное число
# Если введенное число < чем загаданное, то просим увеличить введеное число

# 3
# Пользователь вводит строку из нескольких слов
# Необходимо отобразить 2е слово введенное пользователем на кнопке

# 3*
# Необходимо поочередно выводить каждое слово, написанное пользователем, когда слова закончились, 
# то меняем цвет кнопки на красный и вводим Слова закончились
# Если пользователь изменил введеную строку, то начинаем сначала

# 4
# Необходимо написать программу для генерации пароля из целых чисел и 
# символов алфавита (английский, буквы заглавные и/или прописные)
# Пользовать при этом вводит размер пароля (n - мерный пароль)
# Поля для ввода размера пароля, поле для вывода пароля и кнопка для генерации

# 5
# Необходимо написать программу для генерирования множества случайных фигур на хосте
# Фигуры должны иметь разную заливку - filln (choise(list))
# Фигуры рисуются по нажатию на кнопку
# Фигура за холст не должна выходить
# lst = ['w', 'b', 'g']
# choice(lst)
# randint(1, 5)

# 6
# Необходимо написать программу для рисования произвольного рисунка по N точек (вершин)
# Количество точек вводит пользователь, но не более 20
# Рисунок за холст не должен выходить
# В программе должно присутствовать поле для ввода N точек и кнопка
# При вводе новых значений, холст должен очищаться.

'''x = randint()
y = randint()

tmpx = x
tmpy = y

lastx = 0
lasty = 0

for i in range(5):
  xnext = randint()
  ynext = randint()
  create_line(tmpx, tmpy, xnext, ynext)
  tmpx = xnext
  tmpy = ynext
  lastx = xnext
  lasty = ynext
create_line(x, y, lastx, lasty)'''

# 7
# Напишите программу, в которой определенный символ в тексте будет заменять 
# с одного на другой. Текст пользователь пишет в виджете Text, так же у пользователя
# должна быть возможность выбрать с какого на какой символ он хочет поменять.
# Символы должны заменять по нажатию на кнопку.

# 8 
# Пользователь записывает текст в текстовом поле. 
# Нажав на кнопку, текст в поле выстраивается в обратном порядке.

#'ab c d' -> 'd c ba'

# 8 *
# Только слова должны встать в обратном порядке.

# 9
# Программа должна рисовать столбчатую диаграмму в зависимости от слов в абзаце.
# Т.е. есть виджет Text, в котором пользователь пишет текст с абзацами,
# высота прямоугольника в диаграмме зависит от количества слов,
# подсчет итоговой диаграммы происходит по нажатию на кнопку. 

'''from tkinter import *
from tkinter import messagebox
import random

tap = 0

def click():
  global tap
  tap += 1
  if tap > 20:
    messagebox.showinfo('End leve', 'You win!')
    button.config(state = 'disabled')
  else:
    button.place(x = random.randint(0, 500), y = random.randint(0, 300))

root = Tk()
root.geometry('600x400')
root.resizable(False, False)

button = Button(
  text = 'Click',
  width = 10,
  height = 2,
  command = click
)
button.pack()
 
root.mainloop()'''

# Необходимо дописать действия C, DEL, X^2

'''from tkinter import *
from functools import partial

primer = ''  # a += 1  -> a = a + 1

def click(nameB):
  global primer
  if nameB == '=':
    primer = str(eval(primer))
  elif nameB == 'C':
    primer = ''
  elif nameB == 'DEL':
    primer = primer[:-1]
  elif nameB == 'DEL':
    primer += '**2'
  else:
    primer += nameB
  label.config(text = primer)

root = Tk()
root.config(bg = "black")
root.geometry("485x550")
root.title("Калькулятор")
root.resizable(False, False)

label = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
label.place(x = 10, y = 50)

buttonNames = [
"C", "DEL", "*", "=",
"1", "2", "3", "/",
"4", "5", "6", "+", 
"7", "8", "9", "-",
"(", "0", ")", "X^2"
]

# '3 + (2 * 2) **2'

x = 10
y = 140

for i in buttonNames:
  Button(
    text = i,
    bg="white",
    font=("Consolas", 15),
    command = partial(click, i)
    ).place(
      x = x, 
      y = y,
      width = 115,
      height = 79)
  x += 117
  if x > 400:
      x = 10
      y += 81

root.mainloop()'''

'''from tkinter import *

def click():
  s = text.get('1.0', 'end')
  ns = ''
  for i in s:
    if i != entry1.get():
      ns += i
    else:
      ns += entry2.get()
  text.delete('1.0', 'end')
  text.insert('1.0', ns)


window = Tk()

text = Text(
  font = ('Arial', 20),
  wrap = WORD
)
text.pack()

entry1 = Entry()
entry1.pack()

entry2 = Entry()
entry2.pack()

button = Button(
  text = 'Click',
  command = click
)
button.pack()

window.mainloop()'''


'''from tkinter import *

windows = Tk()
windows.geometry('600x400')
#windows.resizable(True, False)

button = Button(
    text = 'Click',
    bg = 'yellow'
)

button.place(
    relx = 0.5,
    rely = 0.5,
    anchor = CENTER,
    relwidth = 0.9,
    relheight = 0.5
)

windows.mainloop()'''


'''
rim = { 1 : 'I', 5 : 'V'}

def rom_to_int(num):
    return rim.get(num)

def int_to_rom(num):
    res = ''
    for key, value in rim.items():
        if value == num:
            res = key
            break
    return res'''



import csv

lines = [
    ['Alexander Melnikov', '31', 'm'],
    ['Mihail Tolstoy', '28', 'm'],
]

with open('data.csv', 'w', newline = '') as f:
    crs = csv.writer(f)
    crs.writerows(lines)

# Необходимо написать код для дозаписи списка в файл
a = ['Alexander Melnikov', '31', 'm']

with open('data.csv', 'a', newline = '') as f:
    crs = csv.writer(f)
    crs.writerow(a)

with open('data.csv', 'r') as f:
    crs = csv.reader(f)
    for i in crs:
        print(i)