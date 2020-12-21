import csv
import sqlite3
from tkinter import *
import tkinter as tk

conn_t = sqlite3.connect('prais_t.csv')
conn_v = sqlite3.connect('prais_v.csv')
conn_d = sqlite3.connect('prais_d.csv')
conn_p = sqlite3.connect('prais_p.csv')
conn_pl = sqlite3.connect('prais_pl.csv')

sql_t = conn_t.cursor()
sql_v = conn_v.cursor()
sql_d = conn_d.cursor()
sql_p = conn_p.cursor()
sql_pl = conn_pl.cursor()


sql_d.execute("""CREATE TABLE IF NOT EXISTS prais_d (
	            ID_prais integer NOT NULL,
	            Kod_m integer,
	            Name_m text,
	            Name_t text,
	            quantity integer
            )""")       

sql_pl.execute("""CREATE TABLE IF NOT EXISTS prais_pl (
				com text
            )""")           





root = tk.Tk()
root.wm_title("Logist")

def butclick1 ():

    I_d = ID_d.get()
    K_d = Kod_d.get()
    NM_d = NameM_d.get()
    NT_d = NameT_d.get()
    Q_d = quantity_d.get()
    sql_d.execute( 'insert into prais_d VALUES(?,?,?,?,?)', (I_d, K_d, NM_d, NT_d, Q_d,))
    conn_d.commit()

def butclick2 ():
	com_pl=coml.get()
	sql_pl.execute( 'insert into prais_pl VALUES(?)', (com_pl,))
	conn_pl.commit()

sql_t.execute("""SELECT ID_prais FROM prais_t """)
I_t = sql_t.fetchone()
sql_t.execute("""SELECT Kod_m FROM prais_t """)
K_t = sql_t.fetchone()
sql_t.execute("""SELECT Name_m FROM prais_t """)
NM_t = sql_t.fetchone()
sql_t.execute("""SELECT Name_t FROM prais_t """)
NT_t = sql_t.fetchone()
sql_t.execute("""SELECT quantity FROM prais_t """)
Q_t = sql_t.fetchone()

sql_v.execute("""SELECT ID_prais FROM prais_v """)
I_v = sql_v.fetchone()
sql_v.execute("""SELECT Kod_m FROM prais_v """)
K_v = sql_v.fetchone()
sql_v.execute("""SELECT Name_m FROM prais_v """)
NM_v = sql_v.fetchone()
sql_v.execute("""SELECT Name_t FROM prais_v """)
NT_v = sql_v.fetchone()
sql_v.execute("""SELECT quantity FROM prais_v """)
Q_v = sql_v.fetchone()
sql_v.execute("""SELECT many FROM prais_v """)
M = sql_v.fetchone()

sql_p.execute("""SELECT com FROM prais_p """)
com = sql_p.fetchone()

tk.Label(text="Выдача товара", fg="black", font=("Arial", 12)) \
	.grid(row=0, column=0, padx=0, pady=2)
tk.Label(text="ID прайса:", fg="black", font=("Arial", 12)) \
	.grid(row=2, column=0, padx=0, pady=2)
ID_d=tk.Entry(width=30, font=("Arial", 10)) 
ID_d.grid(row=2, column=1, columnspan=3)
tk.Label(text="Код магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=3, column=0, padx=0, pady=2)
Kod_d=tk.Entry(width=30, font=("Arial", 10))
Kod_d.grid(row=3, column=1, columnspan=3)
tk.Label(text="Название магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=4, column=0, padx=0, pady=2)
NameM_d=tk.Entry(width=30, font=("Arial", 10)) 
NameM_d.grid(row=4, column=1, columnspan=3)
tk.Label(text="Название товара:", fg="black", font=("Arial", 12)) \
	.grid(row=5, column=0, padx=0, pady=2)
NameT_d=tk.Entry(width=30, font=("Arial", 10)) 
NameT_d.grid(row=5, column=1, columnspan=3)
tk.Label(text="Количество:", fg="black", font=("Arial", 12)) \
	.grid(row=6, column=0, padx=0, pady=2)
quantity_d=tk.Entry(width=30, font=("Arial", 10))
quantity_d.grid(row=6, column=1, columnspan=3)
tk.Button(text="Отправить", font=("Arial", 12), command=butclick1).grid(row=7, column=2)

tk.Label(text="Прайс на товар", fg="black", font=("Arial", 12)) \
	.grid(row=0, column=5, padx=0, pady=2)
tk.Label(text="ID прайса:", fg="black", font=("Arial", 12)) \
	.grid(row=2, column=5, padx=0, pady=2)
tk.Label(text=I_t, fg="black", font=("Arial", 10)) \
    .grid(row=2, column=6, columnspan=3)
tk.Label(text="Код магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=3, column=5, padx=0, pady=2)
tk.Label(text=K_t, fg="black", font=("Arial", 10)) \
    .grid(row=3, column=6, columnspan=3)
tk.Label(text="Название магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=4, column=5, padx=0, pady=2)
tk.Label(text=NM_t, fg="black", font=("Arial", 10)) \
    .grid(row=4, column=6, columnspan=3)
tk.Label(text="Название товара:", fg="black", font=("Arial", 12)) \
	.grid(row=5, column=5, padx=0, pady=2)
tk.Label(text=NT_t, fg="black", font=("Arial", 10)) \
    .grid(row=5, column=6, columnspan=3)
tk.Label(text="Количество:", fg="black", font=("Arial", 12)) \
	.grid(row=6, column=5, padx=0, pady=2)
tk.Label(text=Q_t, fg="black", font=("Arial", 10)) \
    .grid(row=6, column=6, columnspan=3)
tk.Button(text="Обновить список", font=("Arial", 12)).grid(row=7, column=6)

tk.Label(text="Комментарий на получение:", fg="black", font=("Arial", 12)) \
	.grid(row=9, column=5, padx=0, pady=2)
tk.Label(text=com, fg="black", font=("Arial", 10)) \
    .grid(row=9, column=6, columnspan=3)

tk.Label(text="Возврат товара", fg="black", font=("Arial", 12)) \
	.grid(row=0, column=10, padx=0, pady=2)
tk.Label(text="ID прайса:", fg="black", font=("Arial", 12)) \
	.grid(row=2, column=10, padx=0, pady=2)
tk.Label(text=I_t, fg="black", font=("Arial", 10)) \
    .grid(row=2, column=11, columnspan=3)
tk.Label(text="Код магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=3, column=10, padx=0, pady=2)
tk.Label(text=K_v, fg="black", font=("Arial", 10)) \
    .grid(row=3, column=11, columnspan=3)
tk.Label(text="Название магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=4, column=10, padx=0, pady=2)
tk.Label(text=NM_v, fg="black", font=("Arial", 10)) \
    .grid(row=4, column=11, columnspan=3)
tk.Label(text="Название товара:", fg="black", font=("Arial", 12)) \
	.grid(row=5, column=10, padx=0, pady=2)
tk.Label(text=NT_v, fg="black", font=("Arial", 10)) \
    .grid(row=5, column=11, columnspan=3)
tk.Label(text="Количество:", fg="black", font=("Arial", 12)) \
	.grid(row=6, column=10, padx=0, pady=2)
tk.Label(text=Q_v, fg="black", font=("Arial", 10)) \
    .grid(row=6, column=11, columnspan=3)
tk.Label(text="Цена:", fg="black", font=("Arial", 12)) \
	.grid(row=7, column=10, padx=0, pady=2)
tk.Label(text=M,fg="black", font=("Arial", 10)) \
    .grid(row=7, column=11, columnspan=3)
tk.Button(text="Обновить список", font=("Arial", 12)).grid(row=8, column=10)


tk.Label(text="Коментарий к подтверждению:", fg="black", font=("Arial", 12)) \
	.grid(row=9, column=10, padx=0, pady=2)
coml=tk.Entry(width=30, font=("Arial", 10))
coml.grid(row=9, column=11, columnspan=3)
tk.Button(text="Подтвердить получение", font=("Arial", 12), command=butclick2).grid(row=10, column=11)





root.mainloop() 