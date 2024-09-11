from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detailspage as dp
import seaborn as sns
class Comparision2Class:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("Car Price Predictor")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        # self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')


        carsize_w=w1
        carsize_h=h1
        self.carimg1 = ImageTk.PhotoImage(Image.open("myapp_images//redcar.jpg").resize((carsize_w,carsize_h)))
        self.carimglbl = Label(self.window,image=self.carimg1,background=dp.pagebkcolor)
        self.carimglbl.place(x=0,y=0)


        # ----------------- widgets -----------------------------------------------------
        self.window.config(background=dp.pagebkcolor)
        self.headlbl = Label(self.window, text="Analysis ",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)
        self.headlbl.place(x=0, y=0,width=w1,height=70)

        self.l1 = Label(self.window, text="Univariate analysis",font=('Century', 20, 'bold'),
                        foreground=dp.textcolor,background=dp.pagebkcolor)
        self.l1.place(x=40,y=100)

        x1=40
        y1=200
        x_dif=510
        car_data = pd.read_csv('car data.csv')

        figure1 = plt.Figure(figsize=(5, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        # ------------ background ------------------------------
        figure1.patch.set_facecolor('black')
        ax1.set_facecolor(dp.headbkcolor)
        ax1.xaxis.label.set_color(dp.headcolor)
        ax1.yaxis.label.set_color(dp.headcolor)
        ax1.tick_params(axis='x', colors=dp.headcolor)
        ax1.tick_params(axis='y', colors=dp.headcolor)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*0,y=y1)
        ax1.set_title('About Fuel Type', color=dp.headcolor)
        car_fuel_data = car_data.Fuel_Type.value_counts()
        # car_fuel_data.plot(kind='bar', ax=ax1,x='Fuel Type',color='orchid', legend=True,rot=0)
        car_fuel_data.plot(kind='bar', ax=ax1,x='Fuel Type',color=dp.diagram_color ,rot=0)
        fuel_count = list(car_fuel_data)
        for i in range(len(fuel_count)):
            ax1.text(i, fuel_count[i]+2,fuel_count[i],color=dp.headcolor)


        figure2 = plt.Figure(figsize=(5,5), dpi=100)
        ax2 = figure2.add_subplot(111)
        # ------------ background ------------------------------
        figure2.patch.set_facecolor('black')
        ax2.set_facecolor(dp.headbkcolor)
        ax2.xaxis.label.set_color(dp.headcolor)
        ax2.yaxis.label.set_color(dp.headcolor)
        ax2.tick_params(axis='x', colors=dp.headcolor)
        ax2.tick_params(axis='y', colors=dp.headcolor)

        diagram = FigureCanvasTkAgg(figure2, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*1+10,y=y1)
        ax2.set_title('About Seller Type', color=dp.headcolor)
        car_seller_data = car_data.Seller_Type.value_counts()
        car_seller_data.plot(kind='bar', ax=ax2,x='Seller Type',color=dp.diagram_color ,rot=0)
        seller_count = list(car_seller_data)
        for i in range(len(seller_count)):
            ax2.text(i, seller_count[i]+2, seller_count[i],color=dp.headcolor)



        figure3 = plt.Figure(figsize=(5,5), dpi=100)
        ax3 = figure3.add_subplot(111)
        # ------------ background ------------------------------
        figure3.patch.set_facecolor('black')
        ax3.set_facecolor(dp.headbkcolor)
        ax3.xaxis.label.set_color(dp.headcolor)
        ax3.yaxis.label.set_color(dp.headcolor)
        ax3.tick_params(axis='x', colors=dp.headcolor)
        ax3.tick_params(axis='y', colors=dp.headcolor)
        diagram = FigureCanvasTkAgg(figure3, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*2+20,y=y1)
        ax3.set_title('About Transmission', color=dp.headcolor)
        car_transmission_data=car_data.Transmission.value_counts()
        car_data.Transmission.value_counts().plot(kind='bar', ax=ax3,x='Transmission',color=dp.diagram_color ,rot=0)
        transmission_count = list(car_transmission_data)
        for i in range(len(transmission_count)):
            ax3.text(i , transmission_count[i]+2, transmission_count[i],color=dp.headcolor)
        self.window.mainloop()


if __name__ == '__main__':
    dummy=Tk()
    obj = Comparision2Class(dummy)
    dummy.mainloop()
