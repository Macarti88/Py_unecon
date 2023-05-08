import tkinter as tk
from tkinter import messagebox
import time

# Создаем окно
window = tk.Tk()
window.title("Аукцион")

# Создаем метки для полей
name_label = tk.Label(window, text="Название")
description_label = tk.Label(window, text="Описание")
area_label = tk.Label(window, text="Площадь")
price_label = tk.Label(window, text="Цена")
tax_value_label = tk.Label(window, text="Начальная ставка")
step_label = tk.Label(window, text="Шаг")

# Создаем поля ввода
name_entry = tk.Entry(window)
description_entry = tk.Entry(window)
area_entry = tk.Entry(window)
price_entry = tk.Entry(window)
tax_value_entry = tk.Entry(window)
step_entry = tk.Entry(window)

# Создаем поле для фото
photo_image = tk.PhotoImage(file="test.png")
photo_label = tk.Label(window, image=photo_image)

# Создаем кнопки
start_auction_button = tk.Button(window, text="Начать аукцион")
stop_auction_button = tk.Button(window, text="Остановить аукцион")
change_image_button = tk.Button(window, text="Изменить изображение")
add_bid_button = tk.Button(window, text="Добавить ставку")


from tkinter import filedialog

# Создаем функцию для изменения изображения
def change_image():
    filename = filedialog.askopenfilename(filetypes=[("PNG файлы", "*.png")])
    if filename:
        new_image = tk.PhotoImage(file=filename)
        photo_label.config(image=new_image)
        photo_label.image = new_image


# Добавляем метки и поля в окно
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

description_label.grid(row=1, column=0)
description_entry.grid(row=1, column=1)

area_label.grid(row=2, column=0)
area_entry.grid(row=2, column=1)

price_label.grid(row=3, column=0)
price_entry.grid(row=3, column=1)

tax_value_label.grid(row=4, column=0)
tax_value_entry.grid(row=4, column=1)

step_label.grid(row=5, column=0)
step_entry.grid(row=5, column=1)

photo_label.grid(row=0, column=2, rowspan=6)

# Добавляем кнопки в окно
start_auction_button.grid(row=6, column=0)
stop_auction_button.grid(row=6, column=1)
change_image_button.grid(row=7, column=2)
add_bid_button.grid(row=10, column=2)



# Создаем функцию для таймера
def start_timer():
    global timer_running
    timer_running = True
    start_time = time.time()
    update_timer(start_time)

def update_timer(start_time):
    if timer_running:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        timer_label.config(text="Времени прошло: {:02d}:{:02d}".format(minutes, seconds))
        if elapsed_time >= 10:
            stop_timer()
            show_winner()
        else:
            window.after(1000, update_timer, start_time)



# Создание функции для остановки таймера
def stop_timer():
    global timer_running
    timer_running = False
    show_winner()


# Создание функции для показа победителя
def show_winner():
    winner_id = highest_bidder
    winner_bid = highest_bid
    messagebox.showinfo("Auction Winner",
                        "The winner of the auction {} with a bid of {}.".format(winner_id, winner_bid))


# Создание функции для добавления ставки
bids = {}
highest_bid = 0
highest_bidder = ""


def add_bid():
    global highest_bid
    global highest_bidder
    bidder_id = id_entry.get()
    bid_amount = int(amount_entry.get())
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder_id
        current_bid_label.config(text="Текущая ставка - ID: {} - {}$".format(highest_bidder, highest_bid))
    bids[bidder_id] = bid_amount


# Add functionality to buttons
start_auction_button.config(command=start_timer)
stop_auction_button.config(command=stop_timer)
change_image_button.config(command=change_image)
add_bid_button.config(command=add_bid)

# Create labels for timer and current bid
timer_label = tk.Label(window, text="Прошло времени: 00:00")
current_bid_label = tk.Label(window, text="Высшая ставка: \n ID \t Ставка")
timer_label.grid(row=8, column=0, columnspan=2)
current_bid_label.grid(row=9, column=0, columnspan=2)

# Create entry fields for bids
id_entry = tk.Entry(window)
id_entry.grid(row=10, column=0)

amount_entry = tk.Entry(window)
amount_entry.grid(row=10, column=1)

# Run the window
window.mainloop()
