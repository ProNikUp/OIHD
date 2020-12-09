import csv
import sqlite3
from tkinter import *
import tkinter as tk

conn_t = sqlite3.connect('prais_t.csv')
conn_v = sqlite3.connect('prais_v.csv')
conn_d = sqlite3.connect('prais_d.csv')

sql_t = conn_t.cursor()
sql_v = conn_v.cursor()
sql_d = conn_d.cursor()


sql_t.execute("""CREATE TABLE IF NOT EXISTS prais_t (
	            ID_prais integer NOT NULL,
	            Kod_m integer,
	            Name_m text,
	            Name_t text,
	            quantity integer
            )""")       

sql_v.execute("""CREATE TABLE IF NOT EXISTS prais_v (
	            ID_prais integer NOT NULL,
	            Kod_m integer,
	            Name_m text,
	            Name_t text,
	            quantity integer,
                many integer
            )""")       





root = tk.Tk()
root.wm_title("Manager")

def butclick1 ():

    I_t = ID_t.get()
    K_t = Kod_t.get()
    NM_t = NameM_t.get()
    NT_t = NameT_t.get()
    Q_t = quantity_t.get()
    sql_t.execute( 'insert into prais_t VALUES(?,?,?,?,?)', (I_t, K_t, NM_t, NT_t, Q_t,))
    conn_t.commit()
def butclick2 ():
    I_v = ID_v.get()
    K_v = Kod_v.get()
    NM_v = NameM_v.get()
    NT_v = NameT_v.get()
    Q_v = quantity_v.get()
    M = many.get()
    sql_v.execute( 'insert into prais_v VALUES(?,?,?,?,?,?)', (I_v, K_v, NM_v, NT_v, Q_v, M,))
    conn_v.commit()

sql_d.execute("""SELECT ID_prais FROM prais_d """)
I_d = sql_d.fetchone()
sql_d.execute("""SELECT Kod_m FROM prais_d """)
K_d = sql_d.fetchone()
sql_d.execute("""SELECT Name_m FROM prais_d """)
NM_d = sql_d.fetchone()
sql_d.execute("""SELECT Name_t FROM prais_d """)
NT_d = sql_d.fetchone()
sql_d.execute("""SELECT quantity FROM prais_d """)
Q_d = sql_d.fetchone()

tk.Label(text="Прайс на товар", fg="black", font=("Arial", 12)) \
	.grid(row=0, column=0, padx=0, pady=2)
tk.Label(text="ID прайса:", fg="black", font=("Arial", 12)) \
	.grid(row=2, column=0, padx=0, pady=2)
ID_t=tk.Entry(width=30, font=("Arial", 10)) 
ID_t.grid(row=2, column=1, columnspan=3)
tk.Label(text="Код магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=3, column=0, padx=0, pady=2)
Kod_t=tk.Entry(width=30, font=("Arial", 10))
Kod_t.grid(row=3, column=1, columnspan=3)
tk.Label(text="Название магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=4, column=0, padx=0, pady=2)
NameM_t=tk.Entry(width=30, font=("Arial", 10)) 
NameM_t.grid(row=4, column=1, columnspan=3)
tk.Label(text="Название товара:", fg="black", font=("Arial", 12)) \
	.grid(row=5, column=0, padx=0, pady=2)
NameT_t=tk.Entry(width=30, font=("Arial", 10)) 
NameT_t.grid(row=5, column=1, columnspan=3)
tk.Label(text="Количество:", fg="black", font=("Arial", 12)) \
	.grid(row=6, column=0, padx=0, pady=2)
quantity_t=tk.Entry(width=30, font=("Arial", 10))
quantity_t.grid(row=6, column=1, columnspan=3)
tk.Button(text="Отправить", font=("Arial", 12), command=butclick1).grid(row=7, column=2)

tk.Label(text="Прайс на возврат товара", fg="black", font=("Arial", 12)) \
	.grid(row=0, column=5, padx=0, pady=2)
tk.Label(text="ID прайса:", fg="black", font=("Arial", 12)) \
	.grid(row=2, column=5, padx=0, pady=2)
ID_v=tk.Entry(width=30, font=("Arial", 10))
ID_v.grid(row=2, column=6, columnspan=3)
tk.Label(text="Код магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=3, column=5, padx=0, pady=2)
Kod_v=tk.Entry(width=30, font=("Arial", 10))
Kod_v.grid(row=3, column=6, columnspan=3)
tk.Label(text="Название магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=4, column=5, padx=0, pady=2)
NameM_v=tk.Entry(width=30, font=("Arial", 10))
NameM_v.grid(row=4, column=6, columnspan=3)
tk.Label(text="Название товара:", fg="black", font=("Arial", 12)) \
	.grid(row=5, column=5, padx=0, pady=2)
NameT_v=tk.Entry(width=30, font=("Arial", 10))
NameT_v.grid(row=5, column=6, columnspan=3)
tk.Label(text="Количество:", fg="black", font=("Arial", 12)) \
	.grid(row=6, column=5, padx=0, pady=2)
quantity_v=tk.Entry(width=30, font=("Arial", 10)) 
quantity_v.grid(row=6, column=6, columnspan=3)
tk.Label(text="Цена:", fg="black", font=("Arial", 12)) \
	.grid(row=7, column=5, padx=0, pady=2)
many=tk.Entry(width=30, font=("Arial", 10)) 
many.grid(row=7, column=6, columnspan=3)
tk.Button(text="Отправить", font=("Arial", 12), command=butclick2).grid(row=8, column=7)

tk.Label(text="Получение товара", fg="black", font=("Arial", 12)) \
	.grid(row=0, column=10, padx=0, pady=2)
tk.Label(text="ID прайса:", fg="black", font=("Arial", 12)) \
	.grid(row=2, column=10, padx=0, pady=2)
tk.Label(text=I_d, fg="black", font=("Arial", 10)) \
    .grid(row=2, column=11, columnspan=3)
tk.Label(text="Код магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=3, column=10, padx=0, pady=2)
tk.Label(text=K_d, fg="black", font=("Arial", 10)) \
    .grid(row=3, column=11, columnspan=3)
tk.Label(text="Название магазина:", fg="black", font=("Arial", 12)) \
	.grid(row=4, column=10, padx=0, pady=2)
tk.Label(text=NM_d, fg="black", font=("Arial", 10)) \
    .grid(row=4, column=11, columnspan=3)
tk.Label(text="Название товара:", fg="black", font=("Arial", 12)) \
	.grid(row=5, column=10, padx=0, pady=2)
tk.Label(text=NT_d, fg="black", font=("Arial", 10)) \
    .grid(row=5, column=11, columnspan=3)
tk.Label(text="Количество:", fg="black", font=("Arial", 12)) \
	.grid(row=6, column=10, padx=0, pady=2)
tk.Label(text=Q_d, fg="black", font=("Arial", 10)) \
    .grid(row=6, column=11, columnspan=3)
tk.Button(text="Обновить список", font=("Arial", 12)).grid(row=8, column=10)
tk.Button(text="Подтвердить получение", font=("Arial", 12)).grid(row=8, column=12)







root.mainloop() 