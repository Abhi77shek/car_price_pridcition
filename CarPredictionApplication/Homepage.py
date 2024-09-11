from tkinter import *
from tkinter import messagebox
import detailspage as dp
from ComparisonPage1 import Comparision1Class
from ComparisonPage2 import Comparision2Class
from ComparisonPage3 import Comparision3Class
from ComparisonPage4 import Comparision4Class
from MyCarPredictor import CarPageClass
from PIL import ImageTk, Image
from reportPage import ViewReport3Class
class HomepageClass:
    def __init__(self):
        self.window = Tk()
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        # w1=int(self.w/2)
        # h1=int(self.h/2)+70
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2-100))
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,0,0))
        self.window.state('zoomed')
        self.window.title('Car Predictor')


        carsize_w=w1
        carsize_h=h1
        self.carimg1 = ImageTk.PhotoImage(Image.open("myapp_images//redcar.jpg").resize((carsize_w,carsize_h)))
        self.carimglbl = Label(self.window,image=self.carimg1,background=dp.pagebkcolor)
        self.carimglbl.place(x=0,y=0)


        self.headlbl = Label(self.window, text="Car Price Predictor ",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)

        self.window.config(background=dp.pagebkcolor)

        self.b1 = Button(self.window,text="Predict",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda : CarPageClass(self.window))
        self.b2 = Button(self.window,text="Univarate Analysis",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :Comparision2Class(self.window))
        self.b3 = Button(self.window,text="Bivarate Analysis",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :Comparision1Class(self.window))
        self.b4 = Button(self.window,text="Sale Report",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :ViewReport3Class(self.window))
        self.b5 = Button(self.window,text="Sale Report By Month",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :Comparision3Class(self.window))
        self.b6 = Button(self.window,text="Sale Analysis By Fuel",font=dp.headfont2,
                         foreground=dp.headcolor,background=dp.headbkcolor,command=lambda :Comparision4Class(self.window))
        self.b7 = Button(self.window,text="Close",font=dp.headfont2,foreground=dp.headcolor,background=dp.headbkcolor,command=self.quitter)



        b_width=250
        b_height=55
        x1 = int(w1/2-(b_width/2))
        y1=100
        y_diff=70


        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.b1.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b2.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b3.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b4.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b5.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b6.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff
        self.b7.place(x=x1,y=y1,width=b_width,height=b_height)
        y1+=y_diff


        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()

if __name__ == '__main__':
    HomepageClass()