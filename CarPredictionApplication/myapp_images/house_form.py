from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import detailspage as dp
from tkinter.ttk import Combobox

class HomepageClass:
    def __init__(self):
        self.window = Tk()
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1 = self.w
        h1 = self.h
        self.window.minsize(w1, h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2-100))
        self.window.geometry("%dx%d+%d+%d" % (w1, h1, 0, 0))
        self.window.state('zoomed')
        self.window.title('Car Predictor')
        self.headlbl = Label(self.window, text="House Price Predictor ")
    #----------------------

        # ----------------- widgets -----------------------------------------------------
        self.window.config(background=dp.pagebkcolor)
        self.headlbl = Label(self.window, text="Predict Car Selling  Price ",
                             font=dp.headfont, foreground=dp.headcolor, background=dp.headbkcolor)

        self.l1 = Label(self.window, text="Year", font=dp.textfont, foreground=dp.textcolor,
                        background=dp.pagebkcolor)
        self.l2 = Label(self.window, text="Showroom Price (in lakh) ", font=dp.textfont,
                        foreground=dp.textcolor, background=dp.pagebkcolor)
        self.l3 = Label(self.window, text="Kilometers Drived ", font=dp.textfont, foreground=dp.textcolor,
                        background=dp.pagebkcolor)
        self.l4 = Label(self.window, text="Previous Owners", font=dp.textfont, foreground=dp.textcolor,
                        background=dp.pagebkcolor)
        self.l5 = Label(self.window, text="Fuel type", font=dp.textfont, foreground=dp.textcolor,
                        background=dp.pagebkcolor)
        self.l6 = Label(self.window, text="Seller Type ", font=dp.textfont, foreground=dp.textcolor,
                        background=dp.pagebkcolor)
        self.l7 = Label(self.window, text="Transmission Type", font=dp.textfont, foreground=dp.textcolor,
                        background=dp.pagebkcolor)
        self.l8 = Label(self.window, text=" - - - - - ", font=('Century', 14, 'bold'), foreground=dp.textcolor,
                        background=dp.pagebkcolor)

        self.t1 = Entry(self.window, font=dp.textfont, foreground=dp.textcolor)
        self.t2 = Entry(self.window, font=dp.textfont, foreground=dp.textcolor)
        self.t3 = Entry(self.window, font=dp.textfont, foreground=dp.textcolor)
        self.v1 = StringVar()
        self.c1 = Combobox(self.window, values=["No", "Second Hand"], textvariable=self.v1, state='readonly',
                           font=dp.textfont, foreground=dp.textcolor)
        self.v1.set("0")
        self.list1 = ["Petrol", "Diesel", "CNG"]
        self.v2 = StringVar()
        self.c2 = Combobox(self.window, values=self.list1, textvariable=self.v2, state='readonly',
                           font=dp.textfont, foreground=dp.textcolor)
        self.v2.set("Petrol")
        self.list2 = ["Dealer", "Individual"]
        self.v3 = StringVar()
        self.c3 = Combobox(self.window, values=self.list2, textvariable=self.v3, state='readonly',
                           font=dp.textfont, foreground=dp.textcolor)
        self.v3.set("Dealer")
        self.v4 = StringVar()
        self.c4 = Combobox(self.window, values=['Manual', "Automatic"], textvariable=self.v4, state='readonly',
                           font=dp.textfont, foreground=dp.textcolor)
        self.v4.set("Manual")
        self.btn1 = Button(self.window, text="Predict Price", font=dp.textfont,
                           foreground=dp.headcolor, background=dp.headbkcolor, command=self.predict)

        self.btn2 = Button(self.window, text="Reset", font=dp.textfont,
                           foreground=dp.headcolor, background=dp.headbkcolor, command=self.clearPage)
        self.btn3 = Button(self.window, text="Sale", font=dp.textfont,
                           foreground=dp.headcolor, background=dp.headbkcolor, command=self.saveData)

        self.ressize_w = 100
        self.ressize_h = 100
        self.responseimglbl = Label(self.window, background=dp.pagebkcolor)
        # carsize_w=500
        # carsize_h=200
        # self.carimg1 = ImageTk.PhotoImage(Image.open("myapp_images//car2.png").resize((carsize_w,carsize_h)))
        # self.carimglbl = Label(self.window,image=self.carimg1,background=dp.pagebkcolor)

        # ******** PLacing *************
        self.headlbl.place(x=0, y=0, width=w1, height=70)
        x1 = 40
        y1 = 100
        x_diff = 250
        y_diff = 50
        self.l1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff, y=y1)
        self.l8.place(x=x1 + x_diff + x_diff + 50, y=y1)
        y1 += y_diff
        self.l2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1)
        self.responseimglbl.place(x=x1 + x_diff * 3, y=y1, width=self.ressize_w, height=self.ressize_h)
        y1 += y_diff
        self.l3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l4.place(x=x1, y=y1)
        self.c1.place(x=x1 + x_diff, y=y1)
        # self.carimglbl.place(x=x1+x_diff*2,y=y1,width=carsize_w,height=carsize_h)
        y1 += y_diff
        self.l5.place(x=x1, y=y1)
        self.c2.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l6.place(x=x1, y=y1)
        self.c3.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.l7.place(x=x1, y=y1)
        self.c4.place(x=x1 + x_diff, y=y1)
        y1 += y_diff
        self.btn2.place(x=x1, y=y1, width=200, height=40)
        self.btn1.place(x=x1 + x_diff * 1, y=y1, width=200, height=40)
        self.btn3.place(x=x1 + x_diff * 2, y=y1, width=200, height=40)
        y1 += y_diff



        #-----------------------------------
        self.headlbl.place(x=0, y=0,width=300,height=70)

        self.b1 = Button(self.window,text="Predict")
        self.b1.place(x=10,y=100,width=200,height=50)

        self.window.mainloop()

if __name__ == '__main__':
    HomepageClass()