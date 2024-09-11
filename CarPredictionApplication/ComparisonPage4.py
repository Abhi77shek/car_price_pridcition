from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np
import pymysql
from PIL import ImageTk,Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detailspage as dp
class Comparision4Class:
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
        # self.window.config(background=dp.pagebkcolor)
        self.window.config(background='white')
        self.headlbl = Label(self.window, text="Sale Report By Fuel Type",
                             font=dp.headfont,foreground=dp.headcolor,background=dp.headbkcolor)
        self.headlbl.place(x=0, y=0,width=w1,height=70)


        self.databaseConnection()
        self.getData()
        self.window.mainloop()

    def databaseConnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='car_prediction_db', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)

    def getData(self):

        #------ get data from anywhere (database, user, calculations,random,csv,dataframe) ----
        try:

            # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on
            qry = " select * from carsaletable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            petrol_sale=0
            diesel_sale=0
            cng_sale=0
            for myrow in data:
                if myrow[5]=='Petrol':
                    petrol_sale+=1
                elif myrow[5]=='Diesel':
                    diesel_sale+=1
                else:
                    cng_sale+=1
        except Exception as e:
            messagebox.showerror("Query Error", "Error in Insertion : \n" + str(e), parent=self.window)

        # ------------ make diagram -----------------

        # student_names=["raman","gagan","aman","mohit","rohit"]
        # student_attendence = [120,111,90,378,77]
        # colors_list=['red','green','teal','gray','pink']

        pie_labels = ["Petrol","Diesel","CNG"]
        pie_values = [petrol_sale,diesel_sale,cng_sale]
        max_value = np.argmax(pie_values)
        explod_values = [ 0.05 if x==max_value else 0 for x in range(len(pie_values))]

        pie_colors = ["#922724","#800000","#C80F00"]


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
        diagram.get_tk_widget().place(x=500,y=200)
        # ax1.set_title('sale Record')
        ax1.pie(pie_values ,labels=pie_labels ,autopct='%.1f%%',colors=pie_colors, textprops={'color':"w"},explode=explod_values )
        # ax1.pie(pie_values ,labels=pie_labels ,autopct='%.1f%%',colors=["#C80F00","#C80F00","#C80F00"],
        #         textprops={'color':"w"}, hatch=['**O', '/', '.||.'])

if __name__ == '__main__':
    dummy=Tk()
    obj = Comparision4Class(dummy)
    dummy.mainloop()
