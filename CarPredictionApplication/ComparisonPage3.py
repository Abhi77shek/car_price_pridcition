from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt
import pymysql
from PIL import ImageTk,Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detailspage as dp
class Comparision3Class:
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
        self.headlbl = Label(self.window, text="Sale Report By Month",
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

        try:

            # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on
            qry = "SELECT Monthname(sold_on) FROM carsaletable"
            rowcount = self.curr.execute(qry)
            data = self.curr.fetchall()
            month_count={'January':0 ,'February':0 ,'March':0,'April':0,"May":0,"June":0,
                         "July":0,'August':0,'September':0,'October':0,'November':0,"December":0}
            sold_month_list = [ m[0] for m in data]
            for month in month_count.keys():
                c = sold_month_list.count(month)
                month_count.update({month: c})
        except Exception as e:
            messagebox.showerror("Query Error", "Error in Insertion : \n" + str(e), parent=self.window)

        # ------------ make diagram -----------------

        # student_names=["raman","gagan","aman","mohit","rohit"]
        # student_attendence = [120,111,90,378,77]
        # colors_list=['red','green','teal','gray','pink']

        # pie_labels = ["Petrol","Diesel","CNG"]
        # pie_values = [petrol_sale,diesel_sale,cng_sale]
        # pie_colors = ["plum","orchid","darkorchid"]
        #
        figure1 = plt.Figure(figsize=(15, 7), dpi=100)
        # figure1.subplots_adjust(left=0.02,right=0.99,  top=0.9,bottom=0.1)
        figure1.subplots_adjust(left=0.09,right=0.99,  top=0.9,bottom=0.1)
        ax1 = figure1.add_subplot(111)

        # ------------ background ------------------------------
        figure1.patch.set_facecolor('black')
        ax1.set_facecolor(dp.headbkcolor)
        ax1.xaxis.label.set_color(dp.headcolor)
        ax1.yaxis.label.set_color(dp.headcolor)
        ax1.tick_params(axis='x', colors=dp.headcolor)
        ax1.tick_params(axis='y', colors=dp.headcolor)

        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=20, y=80)
        max_tick = max(list(month_count.values()))+1
        # car_data.Fuel_Type.value_counts().plot(kind='bar', ax=ax1, x='Fuel Type', color='orchid', legend=True, rot=45)
        # plt.yticks( )
        ax1.set_xticks(range(1,max_tick))
        ax1.set_xlabel("Total Car Sold")
        ax1.set_ylabel("Months")
        ax1.barh(list(month_count.keys()) ,  list(month_count.values()) , color=dp.diagram_color)
        month_values =  list(month_count.values())
        for i, v in enumerate(month_values):
            ax1.text(v+0.1 , i - .15, str(v),color=dp.headcolor )

if __name__ == '__main__':
    dummy=Tk()
    obj = Comparision3Class(dummy)
    dummy.mainloop()
