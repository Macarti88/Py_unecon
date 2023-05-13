import tkinter as tk
from tkinter import messagebox
import time
from tkinter import filedialog

def begin_Auction():
	global name_entry
	global description_entry
	global area_entry
	global price_entry
	global tax_value_entry
	global step_entry
	global add_image_button
	timer_running = True
	a = tk.Toplevel()
	a.grab_set()
	a.title("Аукцион")

	this_name_label = tk.Label(a, text="Название:")
	this_description_label = tk.Label(a, text="Описание:")
	this_area_label = tk.Label(a, text="Площадь:")
	this_price_label = tk.Label(a, text="Цена:")
	this_tax_value_label = tk.Label(a, text="Начальная цена:")
	this_step_label = tk.Label(a, text="Шаг:")

	# Создаем метки для полей
	this_name_entry = tk.Label(a, text=name_entry.get())
	this_description_entry = tk.Label(a, text=description_entry.get())
	this_area_entry = tk.Label(a, text=area_entry.get())
	this_price_entry = tk.Label(a, text=price_entry.get())
	this_tax_value_entry = tk.Label(a, text=tax_value_entry.get())
	this_step_entry = tk.Label(a, text=step_entry.get())

	# Создаем поле для фото
	photo_image = tk.PhotoImage(file="test.png")
	photo_label = tk.Label(a, image=photo_image)

	# Создаем кнопки
	start_auction_button = tk.Button(a, text="Начать аукцион")
	stop_auction_button = tk.Button(a, text="Остановить аукцион")
	change_image_button = tk.Button(a, text="Изменить изображение")
	add_bid_button = tk.Button(a, text="Добавить ставку")

	# Создаем функцию для изменения изображения
	def change_image():
		filename = filedialog.askopenfilename(filetypes=[("PNG файлы", "*.png")])
		if filename:
			new_image = tk.PhotoImage(file=filename)
			photo_label.config(image=new_image)
			photo_label.image = new_image

	# Добавляем метки и поля в окно
	this_name_label.grid(row=0, column=1)
	this_name_entry.grid(row=0, column=2)

	this_description_label.grid(row=1, column=1)
	this_description_entry.grid(row=1, column=2)

	this_area_label.grid(row=2, column=1)
	this_area_entry.grid(row=2, column=2)

	this_price_label.grid(row=3, column=1)
	this_price_entry.grid(row=3, column=2)

	this_tax_value_label.grid(row=4, column=1)
	this_tax_value_entry.grid(row=4, column=2)

	this_step_label.grid(row=5, column=1)
	this_step_entry.grid(row=5, column=2)

	photo_label.grid(row=0, column=0, rowspan=6)

	# Добавляем кнопки в окно
	start_auction_button.grid(row=7, column=1)
	stop_auction_button.grid(row=7, column=2)
	change_image_button.grid(row=7, column=0)
	add_bid_button.grid(row=10, column=3)

	# Создаем функцию для таймера
	def start_timer():
		nonlocal timer_running
		timer_running = True
		start_time = time.time()
		update_timer(start_time)

	def update_timer(start_time):
		if timer_running:
			elapsed_time = time.time() - start_time
			minutes = int(elapsed_time // 60)
			seconds = int(elapsed_time % 60)
			timer_label.config(text="Времени прошло: {:02d}:{:02d}".format(minutes, seconds))
			if elapsed_time >= 100000:
				stop_timer()
				show_winner()
			else:
				a.after(1000, update_timer, start_time)

	# Создание функции для остановки таймера
	def stop_timer():
		nonlocal timer_running
		timer_running = False
		show_winner()

	# Создание функции для показа победителя
	def show_winner():
		winner_id = highest_bidder
		winner_bid = highest_bid
		messagebox.showinfo("Auction Winner",
							"Победитель аукциона ID:{} Ежемесячная плата за объект составит: {}$/мес.".format(winner_id,
																											  winner_bid))

	# Создание функции для добавления ставки
	bids = {}
	highest_bid = int(tax_value_entry.get())
	highest_bidder = ""

	def add_bid():
		nonlocal highest_bid
		nonlocal highest_bidder
		bidder_id = id_entry.get()

		if amount_entry.get() == "":
			bid_amount = highest_bid + int(step_entry.get())
		else:
			bid_amount = int(amount_entry.get())
		if bid_amount >= highest_bid + int(step_entry.get()):
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
	timer_label = tk.Label(a, text="Прошло времени: 00:00", font=("Arial", 12))
	current_bid_label = tk.Label(a, text="Высшая ставка: \n ID \t Ставка", font=("Arial", 12, ))
	timer_label.grid(row=8, column=1, columnspan=2)
	current_bid_label.grid(row=9, column=1, columnspan=2)

	# Create entry fields for bids
	id_entry = tk.Entry(a)
	id_entry.grid(row=10, column=1)

	amount_entry = tk.Entry(a)
	amount_entry.grid(row=10, column=2)


# Создаем окно
window = tk.Tk()
window.title("Информация об Аукционе")

window.update_idletasks()
s = window.geometry()
s = s.split('+')
s = s[0].split('x')
width_window = int(s[0])
height_window = int(s[1])

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_window // 2
h = h - height_window // 2
window.geometry('+{}+{}'.format(w, h))

# Создаем метки для полей
name_label = tk.Label(window, text="Название")
description_label = tk.Label(window, text="Описание")
area_label = tk.Label(window, text="Площадь")
price_label = tk.Label(window, text="Цена")
tax_value_label = tk.Label(window, text="Начальная цена")
step_label = tk.Label(window, text="Шаг")

# Создаем поля ввода
name_entry = tk.Entry(window)
description_entry = tk.Entry(window)
area_entry = tk.Entry(window)
price_entry = tk.Entry(window)
tax_value_entry = tk.Entry(window)
step_entry = tk.Entry(window)

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


add_info_button = tk.Button(window, text="Добавить", command=begin_Auction)
add_info_button.grid(row=6, column=1)

window.mainloop()
