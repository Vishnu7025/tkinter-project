from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("312x324")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("Calculator")

###################Starting with functions ####################
# 'btn_click' function : 
# This Function continuously updates the 
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'bt_clear' function :This is used to clear 
# the input field

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
# 'bt_equal':This method calculates the expression 
# present in input field
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
 
input_text = StringVar()
 
# Let us creating a frame for the input field
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#Let us create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#Let us creating another 'Frame' for the button below the 'input_frame'
 
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
# first row
 
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "cyan", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
 # fourth row
 
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()


















#second calculator


# # Python program to create a simple GUI
# # calculator using Tkinter
 
# # import everything from tkinter module
# from tkinter import *
 
# # globally declare the expression variable
# expression = ""
# expression.title("Calculator")
 
# # Function to update expression
# # in the text entry box
# def press(num):
#     # point out the global expression variable
#     global expression
 
#     # concatenation of string
#     expression = expression + str(num)
 
#     # update the expression by using set method
#     equation.set(expression)
 
 
# # Function to evaluate the final expression
# def equalpress():
#     # Try and except statement is used
#     # for handling the errors like zero
#     # division error etc.
 
#     # Put that code inside the try block
#     # which may generate the error
#     try:
 
#         global expression
 
#         # eval function evaluate the expression
#         # and str function convert the result
#         # into string
#         total = str(eval(expression))
 
#         equation.set(total)
 
#         # initialize the expression variable
#         # by empty string
#         expression = ""
 
#     # if error is generate then handle
#     # by the except block
#     except:
 
#         equation.set(" error ")
#         expression = ""
# # Function to clear the contents
# # of text entry box
# def clear():
#     global expression
#     expression = ""
#     equation.set("")
 
 
# # Driver code
# if __name__ == "__main__":
#     # create a GUI window
#     gui = Tk()
 
#     # set the background colour of GUI window
#     gui.configure(background="light green")
 
#     # set the title of GUI window
#     gui.title("Simple Calculator")
 
#     # set the configuration of GUI window
#     gui.geometry("270x150")
 
#     # StringVar() is the variable class
#     # we create an instance of this class
#     equation = StringVar()
 
#     # create the text entry box for
#     # showing the expression .
#     expression_field = Entry(gui, textvariable=equation)
 
#     # grid method is used for placing
#     # the widgets at respective positions
#     # in table like structure .
#     expression_field.grid(columnspan=4, ipadx=70)
 
#     # create a Buttons and place at a particular
#     # location inside the root window .
#     # when user press the button, the command or
#     # function affiliated to that button is executed .
#     button1 = Button(gui, text=' 1 ', fg='black', bg='red',
#                     command=lambda: press(1), height=1, width=7)
#     button1.grid(row=2, column=0)
 
#     button2 = Button(gui, text=' 2 ', fg='black', bg='red',
#                     command=lambda: press(2), height=1, width=7)
#     button2.grid(row=2, column=1)
 
#     button3 = Button(gui, text=' 3 ', fg='black', bg='red',
#                     command=lambda: press(3), height=1, width=7)
#     button3.grid(row=2, column=2)
 
#     button4 = Button(gui, text=' 4 ', fg='black', bg='red',
#                     command=lambda: press(4), height=1, width=7)
#     button4.grid(row=3, column=0)
 
#     button5 = Button(gui, text=' 5 ', fg='black', bg='red',
#                     command=lambda: press(5), height=1, width=7)
#     button5.grid(row=3, column=1)
 
#     button6 = Button(gui, text=' 6 ', fg='black', bg='red',
#                     command=lambda: press(6), height=1, width=7)
#     button6.grid(row=3, column=2)
 
#     button7 = Button(gui, text=' 7 ', fg='black', bg='red',
#                     command=lambda: press(7), height=1, width=7)
#     button7.grid(row=4, column=0)
 
#     button8 = Button(gui, text=' 8 ', fg='black', bg='red',
#                     command=lambda: press(8), height=1, width=7)
#     button8.grid(row=4, column=1)
 
#     button9 = Button(gui, text=' 9 ', fg='black', bg='red',
#                     command=lambda: press(9), height=1, width=7)
#     button9.grid(row=4, column=2)
 
#     button0 = Button(gui, text=' 0 ', fg='black', bg='red',
#                     command=lambda: press(0), height=1, width=7)
#     button0.grid(row=5, column=0)
 
#     plus = Button(gui, text=' + ', fg='black', bg='red',
#                 command=lambda: press("+"), height=1, width=7)
#     plus.grid(row=2, column=3)
 
#     minus = Button(gui, text=' - ', fg='black', bg='red',
#                 command=lambda: press("-"), height=1, width=7)
#     minus.grid(row=3, column=3)
 
#     multiply = Button(gui, text=' * ', fg='black', bg='red',
#                     command=lambda: press("*"), height=1, width=7)
#     multiply.grid(row=4, column=3)
 
#     divide = Button(gui, text=' / ', fg='black', bg='red',
#                     command=lambda: press("/"), height=1, width=7)
#     divide.grid(row=5, column=3)
 
#     equal = Button(gui, text=' = ', fg='black', bg='red',
#                 command=equalpress, height=1, width=7)
#     equal.grid(row=5, column=2)
 
#     clear = Button(gui, text='Clear', fg='black', bg='red',
#                 command=clear, height=1, width=7)
#     clear.grid(row=5, column='1')
 
#     Decimal= Button(gui, text='.', fg='black', bg='red',
#                     command=lambda: press('.'), height=1, width=7)
#     Decimal.grid(row=6, column=0)
#     # start the GUI
#     gui.mainloop()