from tkinter import Label, Tk
import time

app_widow = Tk()
app_widow.title("Digital Clock")
app_widow.geometry("420x150")
app_widow.resizable(1,1)

text_font=("Boulder", 68, 'bold')
backround="#211C84"
foreground="#4D55CC"
border_width = 25

label=Label(app_widow,font=text_font,bg=backround,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)

digital_clock()
app_widow.mainloop()




