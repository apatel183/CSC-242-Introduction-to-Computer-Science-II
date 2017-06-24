# Calculator.py
'''
Calculator widget - to create a generic
widget, often you can subclass Frame

we will use grid layout
'''

from tkinter import *

class Calculator(Frame):

    # need init to build interface
    def __init__(self,parent=None):  # needs to have argument for the parent
        
        # extend, call parent constructor first
        Frame.__init__(self,parent)

        # Entry at top for results
        self.entry = Entry(self)
        self.entry.grid(row=0,column=0,columnspan=4)
        # layout buttons
        btns = "0123456789+-*/().%=C"
              
            
        for i in range(len(btns)):
            # custom function, needed for hw4, not for lab or midterm
            def cmd(key=btns[i]):
                #print( 'cmd' )
                self.click(key)
            b = Button(self,text=btns[i],command=cmd,width=5,height=2)
            b.grid(row=i//4+1,column=i%4)


    # trick, separate cmd functions will call this function
    def click(self,key):
        #print( 'click',key)
        if key=='C':
            self.entry.delete(0,END)
        elif key=='=':
            try:
                ans = eval(self.entry.get())
            except:
                ans = 'ERROR'
            self.entry.delete(0,END)
            self.entry.insert(END,ans)
            
        else:  # write key into display
            self.entry.insert(END,key)
        

    
            

#Calculator().pack()
#Calculator().pack()
#Calculator().pack()


root = Tk()
Calculator(root).pack()














        

        


