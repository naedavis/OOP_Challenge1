#Naeemah Davis
import datetime
# import tkinter
from tkinter import *
# x= datetime.datetime.today()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
#
# y=datetime.datetime.now()
# print(y.time())

#Exercise1
#10 consecutive dates, 1 week apart
# todays date
from tkinter import messagebox

td = datetime.datetime.today()
#for loop to allow the calculation to run 10 times to display 10 different dates
for i in range(10):
    answer = td + datetime.timedelta(days=7)
    #td is like the counter so it just takes the last answer and makes it today and then
    td = answer
    print(answer.date())


#exercise 2
#print your current age
#my birthdate is 2001, 02, 09
birth = datetime.datetime(2001, 2, 9)
#getting todays date
tdate = datetime.datetime.today()
#age is equal to todays year, minus my birth year
age = tdate.year - birth.year
print("My age is " + str(age))

#exercise3
#tkinter class calculating the area of a circle

# window = tkinter.Tk()
# window.geometry("400x400")
# window.title("Area of a Circle")
# window.config(bg= "light green")
# lbl1 = Label(window, text="Enter radius", font= "Arial 15")
# lbl1.place(x=50, y=50)
# entry1 = Entry(window)
# entry1.place(x=200, y=50)
# btn1 = Button(window, text="Calculate", font="Arial 15", command= self.area)
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         area = math.pi*self.radius**2
#         print("The area of a circle " + str(area))
# objCircle = Circle(entry1.get())
# objCircle.area()
# window.mainloop()

class Circle:
    def __init__(self, window):
        self.window = window
        window.title("Area of a Circle")

        self.label = Label(window, text="Enter radius")
        self.label.place(x=50, y=50)

        self.calculate = Button(window, text="Calculate", command=self.area)
        self.calculate.place(x= 150, y=150)

        self.entry1 = Entry(window)
        self.entry1.place(x= 200, y=50)

    def area(self):
        try:
            radius = 3.14*int(self.entry1.get())*int(self.entry1.get())
            messagebox.showinfo("Area of circle is: ", str(radius))

        except ValueError:
            messagebox.showinfo("Error", "Input proper value")
top = Tk()
top.geometry("400x400")
objCircle = Circle(top)
top.mainloop()

