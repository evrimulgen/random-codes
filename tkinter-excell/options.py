from tkinter import *
from tkinter import ttk
import xlsxwriter
from datetime import date

plakavar = StringVar()
ilk_kmvar = StringVar()
son_kmvar = StringVar()
ilk_calisma_saativar = StringVar()
son_calisma_saativar = StringVar()
m3var = StringVar()
operatorvar = StringVar()

win = Tk()
win.title('bir seyler yazma makinesi')

mainframe = ttk.Frame(win, padding="5 5")
mainframe.grid(column=0, row=0)

today = date.today()
strvar = StringVar()

workbook = xlsxwriter.Workbook('/home/mirkan/Desktop/tkinter-excell/tk_arac.xlsx')
worksheet = workbook.add_worksheet()
center = workbook.add_format({'align': 'center'})



plaka = ttk.Combobox(mainframe, values=('35 FY 004', '35 HB 5633', '35 HC 0969'), width=10)
plaka.current(0)
plaka.grid(column=0, row=0)

tarih = ttk.Combobox(win, values=('01.{}.{}'.format(today.month, today.year),'02.{}.{}'.format(today.month, today.year),
										'03.{}.{}'.format(today.month, today.year),'04.{}.{}'.format(today.month, today.year),
										'05.{}.{}'.format(today.month, today.year),'06.{}.{}'.format(today.month, today.year),
										'07.{}.{}'.format(today.month, today.year),'08.{}.{}'.format(today.month, today.year),
										'09.{}.{}'.format(today.month, today.year),'10.{}.{}'.format(today.month, today.year),
										'11.{}.{}'.format(today.month, today.year),'12.{}.{}'.format(today.month, today.year),
										'13.{}.{}'.format(today.month, today.year),'14.{}.{}'.format(today.month, today.year),
										'15.{}.{}'.format(today.month, today.year),'16.{}.{}'.format(today.month, today.year),
										'17.{}.{}'.format(today.month, today.year),'18.{}.{}'.format(today.month, today.year),
										'19.{}.{}'.format(today.month, today.year),'20.{}.{}'.format(today.month, today.year),
										'21.{}.{}'.format(today.month, today.year),'22.{}.{}'.format(today.month, today.year),
										'23.{}.{}'.format(today.month, today.year),'24.{}.{}'.format(today.month, today.year),
										'25.{}.{}'.format(today.month, today.year),'26.{}.{}'.format(today.month, today.year),
										'27.{}.{}'.format(today.month, today.year),'28.{}.{}'.format(today.month, today.year),
										'29.{}.{}'.format(today.month, today.year),'30.{}.{}'.format(today.month, today.year)), width=10)
tarih.current(0)
tarih.grid(column=1, row=1)

plaka_yaz = ttk.Entry(mainframe, textvariable=plakavar, width=10)
plaka_yaz.grid(column=0, row=2)

plaka_button = Button(mainframe, command=plakayi_yaz, text='Plakayi yaz')
plaka_button.grid(column=0, row=3)

tarih_button = Button(mainframe, command=tarih_gir, text='TARIH')
tarih_button.grid(column=0, row=4)

worksheet_ekle = Button(mainframe, command=worksheet_add, text='worksheet ekle')
worksheet_ekle.grid(column=1, row=4)

tarih_label = Label(mainframe, text='Tarih', width=10)
tarih_label.grid(column=1, row=0)

ilk_km = Label(mainframe, text='İlk_km', width=10)
ilk_km.grid(column=2, row=0)
ilk_km_gir = ttk.Entry(mainframe, textvariable=ilk_kmvar, width=10)
ilk_km_gir.grid(column=2, row=1)

son_km = Label(mainframe, text='Son_km', width=10)
son_km.grid(column=3, row=0)
son_km_gir = ttk.Entry(mainframe, textvariable=son_kmvar, width=10)
son_km_gir.grid(column=3, row=1)

ilk_calisma_saati = Label(mainframe, text='I.Çalisma', width=10)
ilk_calisma_saati.grid(column=4, row=0)
ilk_calisma_saati_gir = ttk.Entry(mainframe, textvariable=ilk_calisma_saativar, width=10)
ilk_calisma_saati_gir.grid(column=4, row=1)

son_calisma_saati = Label(mainframe, text='S.Çalisma', width=10)
son_calisma_saati.grid(column=5, row=0)
son_calisma_saati_gir = ttk.Entry(mainframe, textvariable=son_calisma_saativar, width=10)
son_calisma_saati_gir.grid(column=5, row=1)

M3 = Label(mainframe, text='M3', width=10)
M3.grid(column=6, row=0)
M3_gir = ttk.Entry(mainframe, textvariable=m3var, width=10)
M3_gir.grid(column=6, row=1)

Operator = Label(mainframe, text='Operator', width=10)
Operator.grid(column=7, row=0)
Operator_gir = ttk.Entry(mainframe, textvariable=operatorvar, width=10)
Operator_gir.grid(column=7, row=1)



#plaka_label = Label(mainframe, textvariable=strvar).grid(column=0, row=1)


win.protocol('WM_DELETE_WINDOW', exit)
win.mainloop()
