import tkinter as tk
import math

prev_selected_index0 = None
prev_selected_index = None
last_clicked_button = None
chosen_button_name = None
priladka = 0

def show_buttons():
    for i, button1 in enumerate(initial_buttons):
        button1 = tk.Button(root, text=button1, command=lambda name=button1: (on_button_click(name), print(name)))
        button1.pack()
        button1.place(x=200, y=70 + i * 20, width=200, height=20)
        buttons.append(button1)
    for i, (lamination_name, lamination_dict) in enumerate(laminations.items()):
        button2 = tk.Button(root, text=lamination_name)
        button2.pack()
        button2.place(x=1100, y=70 + i * 20, width=200, height=20)
        buttons.append(button2)
        button2.configure(
            command=lambda lamination_name=lamination_name, lamination_dict=lamination_dict, my_button=button2: (
                print(lamination_name), button_click(int(tirazh_entry.get()), lamination_dict, my_button)))

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
    for i, color in enumerate(prices_color.keys()):
        button = tk.Button(root, text=color)
        button.pack()
        button.place(x=430, y=70 + i * 20, width=240, height=20)
        color_buttons.append(button)
        button.bind('<Button-1>', lambda event, c=color: on_button_click_color(c))

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
    global price3, last_clicked_button
    global lamination_name
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
            print(price2)
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
        print(f"{quantity}-quantity")
        print(f"{total}-total")
        print(f"{result}-result")
        print(f"{total}-total")
        quantity_entry.delete(0, tk.END)  # очищаем поле
        quantity_entry.insert(0, result)  # вставляем значение
        tirazh_entry.delete(0, tk.END)
        tirazh_entry.insert(0, result)
        label_result.config(
            text=f'Результат: \nИзделий на 1 А3- {total} , \nТираж- {quantity}, \nКоличество А3 - '
                 f'{result}',
            justify='left')
    except ValueError:
        label_result.config(text='Не выбрали Тираж')


def calculate2():
    try:
        global price3
        print(f"{quantity}-quantity")
        print(f"{price3}-price3")
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


def toggle_priladka():
    global priladka
    priladka = 15
    priladka_button.config(bg="gray", state=tk.DISABLED)


def copy_text():
    root.clipboard_clear()  # Очищаем буфер обмена
    root.clipboard_append(label_result2['text'])  # Копируем текст в буфер обмена


root = tk.Tk()
root.title("Просчет для фирмы Яскравий друк")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

root.resizable(False, False)
buttons = []
color_buttons = []
buttons_cut = {}
initial_buttons = {
    "офсетная 80 г/м2 (SR АЗ/А3}": 1,
    "офсетная SR АЗ 120 г/м2": 1.50,
    "офсетная 190 г/м2 (SR АЗ / АЗ)": 2.50,
    "мункен белый/кремовый 90 г/м2": 1.50,
    "мункен кремовый 150 г/м2": 2.60,
    "мелованная 130 г/м2": 1.65,
    "мелованная 150 г/м2": 1.90,
    "мелованная 170 г/м2": 2.15,
    "мелованная 200 г/м2": 2.60,
    "мелованная 250 г/м2": 3.20,
    "мелованная 300 г/м2": 3.80,
    "мелованная 350 г/м2": 4.50,
    "Самоклейка бумага": 4.5,
    "Самоклейка бумага усиленная ": 5.5,
    "пленка Вйгата матовая": 22.0,
    "Самоклейка пленка JАС": 24.0,
    "Офсетный Лен 235 г/м2": 9.0,
    "Дизайнерский Лен 250 г/м2": 30.0,
    "Маджестик 290 г/м2": 45.0,
    "Колотех 300-350 г/м2": 17.0,
    "tintoretto": 30.0,
    "Sirio Tella Bruno": 35.0,
    "картон 280 г/м2": 5.3,
    "Plike-Ispira 330 г/м2": 60.0,
    "Creative Board 270 г/м2": 30.0,
    "Creative Board Black 120 г/м2": 8.5,
}
cutting = {
    "Без порезки": 0,
    "Порезка за изделие, минимально 15 грн": 0.1,
    # "Биговка за изделие, минимально 15 грн": 0.5,
    # "Перфорация за изделие, минимально 25 грн": 0.7,
    # "Переплет на скобы за 1 скобу, минимально 15,00 грн": 1.0,
    # "Склейка на 2-х сторонний скотч (клапан до 6 см)": 1.0,
    # "Склейка на 2-х сторонний скотч (клапан более 6 см)": 1.75,
    # "Склейка на 2-х сторонний скотч усиленный 1 клапан": 4.0,
    # "Пересборка меню(разобрать+собрать на болты)": 25.0,
    # Пересборка брошюры (замена пружины, скобы и т.д.)": 20.0,
    # "Фальцовка за изделие, минимально 10 грн": 0.2,
    # "Листоподборка за изделие": 0.15,
    # Дырокол ручной за каждое отверстие": 0.40,
    # Пробойник Европетля": 0.75,
    # "Болт или кольцо до 40мм с учетом сверления": 15.0,
    # "Ригель с учетом пробоя": 15.0,
}
prices_color = {
    "цветная односторонняя (4+0)": {
        "1-4": 15,
        "5-9": 10,
        "10-24": 7,
        "25-49": 6.50,
        "50-99": 6,
        "100-199": 5.0,
        "200-299": 4.75,
        "300-500": 4.50,
        "500-1000": 4,
        "1000-10000": 3.5,
    },
    "цветная двусторонняя (4+4)": {
        "1-4": 30,
        "5-9": 20,
        "10-24": 14,
        "25-49": 13,
        "50-99": 12,
        "100-199": 10,
        "200-299": 9.5,
        "300-500": 9,
        "500-1000": 8,
        "1000-10000": 7,
    },
    "черно белая односторонняя SPAЗ (1+0)": {
        "1-4": 8,
        "5-9": 5,
        "10-24": 3.5,
        "25-49": 3,
        "50-99": 2.5,
        "100-199": 2.25,
        "200-299": 2,
        "300-500": 2,
        "500-1000": 2,
        "1000-10000": 1.5,
    },
    "черно белая двусторонняя SPA (1+1)": {
        "1-4": 16,
        "5-9": 10,
        "10-24": 7,
        "25-49": 6,
        "50-99": 5,
        "100-199": 4.5,
        "200-299": 4,
        "300-500": 4,
        "500-1000": 4,
        "1000-10000": 3,
    }
}
laminations = {
    "Без ламинации": {
        "1-5": 0,
        "6-20": 0,
        "21-50": 0,
        "51-100": 0,
        "101-200": 0,
        "200-300": 0,
        "300-1000": 0,
    },
    "Глянцевая 25мк(1+0)": {
        "1-5": 50,
        "6-20": 7,
        "21-50": 5.5,
        "51-100": 4.50,
        "101-200": 4,
        "200-300": 3.8,
        "300-1000": 3.6,
    },
    "Матовая 25мк(1+0)": {
        "1-5": 60,
        "6-20": 8,
        "21-50": 6.2,
        "51-100": 5.0,
        "101-200": 4.5,
        "200-300": 4.2,
        "300-1000": 4.0,
    },
    "Soft Touch 28мк(1+0)": {
        "1-5": 70,
        "6-20": 11,
        "21-50": 10.5,
        "51-100": 10,
        "101-200": 9.5,
        "200-300": 9.25,
        "300-1000": 9,
    },
    "Матовая 31мк Antiscuff(1+0)": {
        "1-5": 70,
        "6-20": 10,
        "21-50": 8.5,
        "51-100": 7.5,
        "101-200": 6.5,
        "200-300": 6.25,
        "300-1000": 6,
    },
}
result = 0
back_button = tk.Button(root, text="Назад", width=20, height=0)
back_button.pack()
back_button.place(x=1600, y=0, anchor="ne")

label_w = tk.Label(root, text='Введите размер мм:')
label_w.pack()
label_w.place(x=10, y=10, anchor="w")

entry_w = tk.Entry(root)
entry_w.pack()
entry_w.place(x=150, y=20, anchor="ne")

label_h = tk.Label(root, text='Введите размер в мм:')
label_h.pack()
label_h.place(x=10, y=60, anchor="w")

entry_h = tk.Entry(root)
entry_h.pack()
entry_h.place(x=150, y=70, anchor="ne")

quantity = tk.Label(root, text='Ввердите Тираж:')
quantity.pack()
quantity.place(x=10, y=110, anchor="w")

entry_quantity = tk.Entry(root)
entry_quantity.pack()
entry_quantity.place(x=150, y=120, anchor="ne")

button_calc = tk.Button(root, text='Рассчитать Количество А3', command=calculate)
button_calc.pack()
button_calc.place(x=170, y=150, anchor="ne")

label_result = tk.Label(root, text='')
label_result.pack()
label_result.place(x=20, y=230, anchor="w")

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

# Создаем поле ввода количества
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
priladka_button.place(x=700, y=150, anchor="w")

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

show_buttons()
root.mainloop()