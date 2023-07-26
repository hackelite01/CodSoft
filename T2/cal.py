import math
from tkinter import *

expression = "" 


# in the text entry box 
def press(num): 
	global expression 

	expression = expression + str(num) 

	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	try: 

		global expression 

		total = str(eval(expression)) 

		equation.set(total) 

		# initialze the expression variable 
		# by empty string 
		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 


# Function to clear the contents 
def clear(): 
	global expression 
	expression = "" 
	equation.set("")
#calculating the fac
def root():
    ans=float(equation.get())**(0.5)
    
    equation.set(str(ans))

    
    
	
# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 
	gui.configure(background="white") 
	gui.title("Simple Calculator") 
	gui.geometry("351x400") 
	equation = StringVar() 
	expression_field = Entry(gui,relief=RIDGE,textvariable=equation,bg="powderblue",bd=30)
	expression_field.grid(columnspan=8, ipadx=60,ipady=30) 
	equation.set(' ') 

	# create a Buttons and place at a particular
	button1 = Button(gui, text=' 1 ', fg='black', bg='white', 
					command=lambda: press(1), height=2, width=9).grid(row=3, column=0) 

	button2 = Button(gui, text=' 2 ', fg='black', bg='white', 
					command=lambda: press(2), height=2, width=9) 
	button2.grid(row=3, column=1) 

	button3 = Button(gui, text=' 3 ', fg='black', bg='white', 
					command=lambda: press(3), height=2, width=9) 
	button3.grid(row=3, column=2) 

	button4 = Button(gui, text=' 4 ', fg='black', bg='white', 
					command=lambda: press(4), height=2, width=9) 
	button4.grid(row=4, column=0) 

	button5 = Button(gui, text=' 5 ', fg='black', bg='white', 
					command=lambda: press(5), height=2, width=9) 
	button5.grid(row=4, column=1) 

	button6 = Button(gui, text=' 6 ', fg='black', bg='white', 
					command=lambda: press(6), height=2, width=9) 
	button6.grid(row=4, column=2) 

	button7 = Button(gui, text=' 7 ', fg='black', bg='white', 
					command=lambda: press(7), height=2, width=9) 
	button7.grid(row=5, column=0) 

	button8 = Button(gui, text=' 8 ', fg='black', bg='white', 
					command=lambda: press(8), height=2, width=9) 
	button8.grid(row=5, column=1) 

	button9 = Button(gui, text=' 9 ', fg='black', bg='white', 
					command=lambda: press(9), height=2, width=9) 
	button9.grid(row=5, column=2) 

	button0 = Button(gui, text=' 0 ', fg='black', bg='white', 
					command=lambda: press(0), height=2, width=9) 
	button0.grid(row=6, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='white', 
				command=lambda: press("+"), height=2, width=9) 
	plus.grid(row=7, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='white', 
				command=lambda: press("-"), height=2, width=9) 
	minus.grid(row=6, column=3) 

	multiply = Button(gui, text=' x ', fg='black', bg='white', 
					command=lambda: press("*"), height=2, width=9) 
	multiply.grid(row=5, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='white', 
					command=lambda: press("/"), height=2, width=9) 
	divide.grid(row=4, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='white', 
				command=equalpress, height=2, width=9) 
	equal.grid(row=6, column=2) 

	clear = Button(gui, text='[X]', fg='black', bg='red', 
				command=clear, height=2, width=9) 
	clear.grid(row=3, column='3') 

	Decimal= Button(gui, text='.', fg='black', bg='white', 
					command=lambda: press('.'), height=2, width=9) 
	Decimal.grid(row=7, column=0)
	
	squre=Button(gui,text="^",fg='black',bg='white',command=lambda: press('**'),height=2,width=9)
	
	squre.grid(row=7,column=2)

	coma=Button(gui,text=',',fg='black',bg='white',command=lambda: press(','),height=2,width=9)

	coma.grid(row=7,column=1)

	per=Button(gui,text='%',fg="black",bg='white',command=lambda: press('%'),height=2,width=9)

	per.grid(row=6,column=1)

	root=Button(gui,text=u"\u221A",fg="black",bg="white",command=root,height=2,width=9).grid(row=8,column=0)
	
	fact=Button(gui,text='!',fg='black',bg='white',command=lambda :press('!'),height=2,width=9).grid(row=8,column=1)
	bracket=Button(gui,text='(',fg='black',bg='white',command=lambda: press('('),height=2,width=9).grid(row=8,column=2)
	bracket1=Button(gui,text=')',fg='black',bg='white',command=lambda: press(')'),height=2,width=9).grid(row=8,column=3)
	
	# start the GUI 
	gui.mainloop() 
                 
