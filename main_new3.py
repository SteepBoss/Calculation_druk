import tkinter as tk
import math
from tkinter import Canvas
from PIL import Image, ImageTk
from tkinter import NW
from paper_prices_dict import initial_buttons, cutting, prices_color,laminations
install_requires=['Pillow'],
prev_selected_index0 = None
prev_selected_index = None
last_clicked_button = None
chosen_button_name = None
priladka = 0
def show_buttons():
    for i, button1 in enumerate(initial_buttons):
        button1 = tk.Button(root, text=button1, command=lambda name=button1: (on_button_click(name),))
        button1.pack()
        button1.place(x=200, y=70 + i * 20, width=200, height=20)
        buttons.append(button1)
    on_button_click("мелованная 350 г/м2")
    for i, (lamination_name, lamination_dict) in enumerate(laminations.items()):
        button2 = tk.Button(root, text=lamination_name)
        button2.pack()
        button2.place(x=1100, y=70 + i * 20, width=200, height=20)
        buttons2.append(button2)
        button2.configure(
            command=lambda lamination_name=lamination_name, lamination_dict=lamination_dict, my_button=button2: (
                button_click(int(tirazh_entry.get()), lamination_dict, my_button)))
    button_click(int(tirazh_entry.get()), laminations["Без ламинации"], buttons2[0])
    for i, (service, price2) in enumerate(cutting.items()):
        btn = tk.Button(root, text=service, command=lambda p=price2, s=service, b=buttons_cut: change_price(p, s, b))
        btn.pack(anchor='w')
        btn.place(x=700, y=70 + i * 20, width=350, height=20)
        buttons_cut[service] = btn
        btn.bind('<Button-1>', lambda event, b=btn: change_color(b))

        def on_button_click2(price2, service):
            price_var.set(float(price2))
            price_label2.config(text=f"Выбрана услуга:\n{service}, \nцена: {price_var.get()} грн",
                                justify='left')

        btn.config(command=lambda p=price2, s=service: on_button_click2(p, s))
    buttons_cut["Порезка за изделие, минимально 15 грн"].invoke()
    change_color(buttons_cut["Порезка за изделие, минимально 15 грн"])
    for i, color in enumerate(prices_color.keys()):
        button = tk.Button(root, text=color)
        button.pack()
        button.place(x=430, y=70 + i * 20, width=240, height=20)
        color_buttons.append(button)
        button.bind('<Button-1>', lambda event, c=color: on_button_click_color(c))
    on_button_click_color("цветная односторонняя (4+0)")
def on_button_click(button_name):
    global price
    global prev_selected_index
    global chosen_button_name
    button_index = list(initial_buttons.keys()).index(button_name)
    price = initial_buttons[button_name]
    chosen_button_name = button_name
    button = buttons[button_index]
    if prev_selected_index is not None and prev_selected_index != button_index:
        prev_button = buttons[prev_selected_index]
        prev_button.configure(bg=root.cget("bg"))
    prev_selected_index = button_index
    if button["bg"] == "grey":
        button.configure(bg=root.cget("bg"))
    else:
        button.configure(bg="grey")
    update_price_label()

def button_click(quantity, lamination, my_button):
    global price3, last_clicked_button ,lamination_name
    lamination_name = my_button["text"]
    price3 = calculate_price2(quantity, lamination)
    price_label3.configure(text=f"Цена: {price3} грн")

    # Если последняя нажатая кнопка была, меняем ее цвет на стандартный
    if last_clicked_button is not None and last_clicked_button != my_button:
        last_clicked_button.configure(bg="SystemButtonFace")

    # Меняем цвет текущей кнопки
    if my_button is not None:
        my_button.configure(bg="gray")
        # Сохраняем ссылку на последнюю нажатую кнопку
        last_clicked_button = my_button

def change_color(btn):
    for button in buttons_cut.values():
        button.configure(bg=root.cget("bg"))  # изменяем цвет фона предыдущей нажатой кнопки на изначальный
    btn.configure(bg='grey')  # задаем серый цвет фона для выбранной кнопки

def change_price(new_price, service, label, buttons):
    label.config(text=f"{service}: {new_price} грн")
    for key, btn in buttons.items():
        if btn == tk.Button:
            btn.config(text=key)
    buttons[service].config(text=f"{service}: {new_price} грн")

def calculate_price(color, quantity):
    if color in prices_color:
        for k, v in prices_color[color].items():
            range_low, range_high = k.split("-")
            if quantity >= int(range_low) and quantity <= int(range_high):
                return v
    return None

def calculate_price2(quantity, price_dict):
    if quantity < 1:
        return "Тираж меньше 1"
    for range_key, price2 in price_dict.items():
        range_start, range_end = range_key.split("-")
        if int(range_start) <= quantity <= int(range_end):
            return price2

def update_price_label():
    price_label.configure(text="Цена- " + str(price) + " грн.")

def on_button_click_color(color):
    global prev_selected_index0
    if prev_selected_index0 is not None:
        color_buttons[prev_selected_index0].configure(
            bg=root.cget("bg"))  # изменяем цвет фона предыдущей нажатой кнопки на изначальный
    prev_selected_index0 = list(prices_color.keys()).index(color)
    color_buttons[prev_selected_index0].configure(bg='grey')  # задаем серый цвет фона для выбранной кнопки
    quantity_str = quantity_entry.get().strip()
    global price2
    if quantity_str:
        try:
            quantity = int(quantity_str)
            price2 = calculate_price(color, quantity)
            if price2 is not None:
                result_label.config(text=f"Цена: {price2} грн.")
            else:
                result_label.config(text="Неверный ввод.")
        except ValueError:
            result_label.config(text="Неверный ввод.")
    else:
        result_label.config(text="Введите количество.")

def calculate():
    try:
        global result
        global quantity
        global total
        a3_w = 320
        a3_h = 450
        margin = 2
        w = int(entry_w.get()) + 2 * margin
        h = int(entry_h.get()) + 2 * margin
        rows = int((a3_h - margin) / h)
        cols = int((a3_w - margin) / w)
        rows1 = int((a3_h - margin) / w)
        cols1 = int((a3_w - margin) / h)
        total1 = int(rows * cols)
        total2 = int(rows1 * cols1)
        if total1 >= total2:
            total = total1
        if total2 >= total1:
            total = total2
        quantity = int(entry_quantity.get())
        result = math.ceil(quantity / total)
        label_result.config(
            text=f'Результат: \nИзделий на 1 А3- {total} , \nТираж- {quantity}, \nКоличество А3 - '
                 f'{result}',
            justify='left')
    except ValueError:
        label_result.config(text='Не выбрали Тираж')

def calculate2():
    try:
        global price3
        total_price = round(result * price, 1)
        total_price2 = round(result * price2, 2)
        price_var_str = price_var.get()
        price_var_float = float(price_var_str)
        cut_price = round(price_var_float * quantity, 2)
        lamination_price = float(price3 * result)
        total_pr = round((total_price + total_price2 + cut_price + priladka + lamination_price) * 1.5, 2)
        label_result2.config(
            text=f'Результат: \nИзделий на одном А3 - {total}шт. ,\nТираж- {quantity} шт. \nКоличество А3 -{result} шт.'
                 f'\nПриладка - {priladka}грн.\nПорезка - {cut_price} грн.,\nСтоимость Ламинации - {lamination_price} грн.'
                 f'\nТип Ламинации - {lamination_name}\nБумага - {chosen_button_name}\nСтоимость - {total_pr} грн.',
            justify='left')
    except ValueError:
        label_result2.config(text='Не выбрали Тираж')
    except NameError :
        label_result2.config(text='Выберите все поля')


def toggle_priladka():
    global priladka
    if priladka == 0:
        priladka = 15
        priladka_button.config(bg="gray")
    else:
        priladka = 0
        priladka_button.config(bg="white")

def copy_text():
    root.clipboard_clear()  # Очищаем буфер обмена
    root.clipboard_append(label_result2['text'])  # Копируем текст в буфер обмена

def button_clicked(height, width):
    entry_h.delete(0, tk.END) # очищаем содержимое Entry виджетов
    entry_w.delete(0, tk.END)
    entry_h.insert(0, height) # вставляем значения высоты и ширины в Entry виджеты
    entry_w.insert(0, width)

root = tk.Tk()
root.title("Просчет для фирмы Яскравий друк")
root.geometry("1400x800")
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry("{}x{}+{}+{}".format(width, height, x, y))
canvas = Canvas(root, width=2000, height=2000)
pil_image = Image.open("background_main.jpg")
tk_image = ImageTk.PhotoImage(pil_image)
canvas.create_image(0, 0, anchor=NW, image=tk_image)
root.resizable(True, True)

buttons = []
buttons2 = []
color_buttons = []
buttons_cut = {}

result = 0

label_w = tk.Label(root, text='Введите размер мм:')
label_w.pack()
label_w.place(x=10, y=10, anchor="w")

entry_w = tk.Entry(root)
entry_w.insert(0,90)
entry_w.pack()
entry_w.place(x=75, y=20, anchor="ne",width=50, height=20)

label_h = tk.Label(root, text='Введите размер в мм:')
label_h.pack()
label_h.place(x=10, y=60, anchor="w")

entry_h = tk.Entry(root)
entry_h.insert(0,50)
entry_h.pack()
entry_h.place(x=75, y=70, anchor="ne",width=50, height=20)

quantity = tk.Label(root, text='Ввердите Тираж:')
quantity.pack()
quantity.place(x=10, y=110, anchor="w")

entry_quantity = tk.Entry(root)
entry_quantity.insert(0,100)
entry_quantity.pack()
entry_quantity.place(x=75, y=120, anchor="ne",width=50, height=20)

label_result = tk.Label(root, text='')
label_result.pack()
label_result.place(x=20, y=230, anchor="w")

button_calc = tk.Button(root, text='Рассчитать Количество А3', command=calculate)
button_calc.pack()
button_calc.place(x=170, y=150, anchor="ne")
button_calc.invoke()

choice_paper = tk.Label(root, text='Выберите бумагу :')
choice_paper.pack()
choice_paper.place(x=200, y=50, anchor="w")

price_label = tk.Label(root, text="Цена :0")
price_label.pack()
price_label.place(x=320, y=50, anchor="w")

price_var = tk.StringVar()
price_label2 = tk.Label(root, text="Выберите услугу")
price_label2.pack()
price_label2.place(x=700, y=30, anchor="w")

quantity_label = tk.Label
quantity_label = tk.Label(root)
quantity_label.pack()
quantity_label.place(x=450, y=10, anchor="w")

quantity_entry = tk.Entry(root)
quantity_entry.pack()
quantity_entry.place(x=530, y=50, anchor="w", width=30, height=20)
quantity_entry.insert(0, result)

result_label = tk.Label(root, text="")
result_label.pack()
result_label.place(x=590, y=50, anchor="w")

button_calc2 = tk.Button(root, text='Полный расчет', command=calculate2)
button_calc2.pack()
button_calc2.place(x=500, y=220, anchor="ne")


label_result2 = tk.Label(root, text='')
label_result2.pack()
label_result2.place(x=500, y=250, anchor="w")

priladka_button = tk.Button(root, text="+Приладка 15грн", command=toggle_priladka)
priladka_button.pack()
priladka_button.place(x=700, y=200, anchor="w")

tirazh_entry = tk.Entry(root)
tirazh_entry.pack()
tirazh_entry.place(x=1200, y=50, anchor="w", width=30, height=20)
tirazh_entry.insert(0, result)

price_label3 = tk.Label(root, text="Цена: ")
price_label3.pack()
price_label3.place(x=1250, y=50, anchor="w")

quantity_paper = tk.Label(root, text='Количество А3:')
quantity_paper.pack()
quantity_paper.place(x=430, y=50, anchor="w")

quantity_paper = tk.Label(root, text='Количество А3:')
quantity_paper.pack()
quantity_paper.place(x=1100, y=50, anchor="w")

button_copy = tk.Button(root, text='Копировать', command=copy_text)
button_copy.pack()
button_copy.place(x=410, y=270, anchor="w")

button_calc2 = tk.Button(root, text='Полный расчет', command=calculate2)
button_calc2.pack()
button_calc2.place(x=500, y=220, anchor="ne")

button_a3 = tk.Button(root, text="A3", command=lambda: button_clicked(297, 420))
button_a3.pack()
button_a3.place(x=200, y=20, anchor="w")

button_a4 = tk.Button(root, text="A4", command=lambda: button_clicked(210, 297))
button_a4.pack()
button_a4.place(x=230, y=20, anchor="w")

button_a5 = tk.Button(root, text="A5", command=lambda: button_clicked(148, 210))
button_a5.pack()
button_a5.place(x=260, y=20, anchor="w")

button_a6 = tk.Button(root, text="A6", command=lambda: button_clicked(105, 148))
button_a6.pack()
button_a6.place(x=290, y=20, anchor="w")

button_a7 = tk.Button(root, text="A7", command=lambda: button_clicked(74, 105))
button_a7.pack()
button_a7.place(x=320, y=20, anchor="w")

button_a8 = tk.Button(root, text="A8", command=lambda: button_clicked(52, 74))
button_a8.pack()
button_a8.place(x=350, y=20, anchor="w")
canvas.pack()

show_buttons()
root.mainloop()