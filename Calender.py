from tkinter import *
import calendar

#function to display clander
def Display_year_Calendar():
  newRoot = Tk()
  newRoot.title('Year Calendar Screen')
  newRoot.config(bg='#c2d4dd')
  newRoot.geometry('600x600')
  actualyear = int(yearEntry.get())
  calendarContent = calendar.calendar(actualyear)
  lblNew = Label(newRoot, text=calendarContent, font='Consolas 10 bold')
  lblNew.grid(row=0,column=0,padx=30,pady=30)
  newRoot.mainloop()

def Display_month_Calendar():
  newRoot2 = Tk()
  newRoot2.title('Month Calendar Screen')
  newRoot2.config(bg='#c2d4dd')
  newRoot2.geometry('400x400')
  yr = int(yearEntry.get())
  month = int(ent_month.get())
  cal = calendar.month(yr, month)
  lblNew = Label(newRoot2, text=cal, font='Consolas 10 bold')
  lblNew.grid(row=0,column=0,padx=30,pady=30)
  newRoot2.mainloop()

#designing first window
root = Tk()
root.config(bg='#b2c2bf')
root.title('Calendar App')
root.geometry("400x400")



header = Label(root, text= 'CALENDAR', bg='#eaece5', fg='#3b3a30', font=('Georgia',32,'bold'))
header.grid(row=0, column=0, padx=25, pady=25)

lbl = Label(root, text='Enter the year: ', bg= '#eaece5', fg='#3b3a30', font= ('Monaco', 12))
lbl.grid(row=1, column=0, padx=25)

yearEntry = Entry(root, width=5)
yearEntry.grid(row=2, column=0, padx=25, pady=10)

showcalendar = Button(root, text='Show Year Calendar', fg= '#3b3a30', command=Display_year_Calendar)
showcalendar.grid(row=3, column=0, padx=25, pady=10)

lbl_month = Label(root, text='Enter month (1-12):', bg= '#eaece5', fg='#3b3a30', font= ('Monaco', 12))
lbl_month.grid(row=4, column=0, padx=25, pady=10), 

ent_month = Entry(root, width= 5)
ent_month.grid(row=5, column=0, padx=25, pady=10)

showcalendar2 = Button(root, text='Show Month Calendar', fg= '#3b3a30', command=Display_month_Calendar)
showcalendar2.grid(row=6, column=0, padx=25)

root.mainloop()



