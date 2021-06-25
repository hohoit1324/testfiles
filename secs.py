from tkinter import *
from tkinter import messagebox
import webbrowser
import time

window = Tk()
window.title('sex머신')

window.geometry('300x100')

a = 0


def secs2():
    messagebox.showwarning("아몰랑", "아몰랑 작동할거임")

def secs():
        msg1 = messagebox.askquestion("응애", '야스머신을 작동하시겠습니까?')
        if msg1 == 'yes':
            while True:
                webbrowser.open("https://www.youtube.com/watch?v=s4H-EYdXLtI&ab_channel=DOITYOURSELF")
                time.sleep(2)
        if msg1 == 'no':
            secs2()
            while True:
                webbrowser.open("https://www.youtube.com/watch?v=s4H-EYdXLtI&ab_channel=DOITYOURSELF")
                time.sleep(2)



button = Button(window, text="야스머신 작동시키기", command=secs)
button.pack()



window.mainloop()

