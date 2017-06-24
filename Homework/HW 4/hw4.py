##hw4,py### 
##Arpan Patel##

###Question 1##

def mask(wrd,letter):
    lst= ""
    for chars in wrd:
        if chars in letter:
         lst += chars
        else:
             lst+= "?"
    return lst

#TEST
'''
>>> mask('APPLE','AE')
'A???E'
>>> mask('APPLE','')
'?????'
>>> mask('APPLE','PLEASE')
'APPLE'
>>>
'''
##Question 2###
from tkinter import *
from tkinter.messagebox import showinfo

class hangman(Frame):

    def __init__(self, word, parent=None):

        Frame.__init__(self,parent)
        self.word = word.upper()
        masked= mask(self.word,'')

        ##we create all labels here##
        ##label for word##
        labelword = Label(self, text = 'Word:')
        labelword.grid(row=0,column=0, columnspan=1)

        ##label for right##
        labelright = Label(self, text = 'Right:')
        labelright.grid(row=1,column=0, columnspan=1)

        ##label for wrong##
        labelwrong = Label(self, text = 'Wrong:')
        labelwrong.grid(row=2,column=0, columnspan=1)
    
        ##we create all data entry###
        #data entry for word###
        self.maskedword= Entry(self)
        self.maskedword.grid(row=0,column=1, columnspan=4)
        self.maskedword.insert(END,masked)

        ## data entry for right##
        self.right= Entry(self)
        self.right.grid(row=1,column=1, columnspan=4)

        ## data entry for wrong###
        self.wrong= Entry (self)
        self.wrong.grid(row=2,column=1, columnspan=4)

        ##buttons###
        btns= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(btns)):
            def cmd(key= btns[i]):
                self.click(key)
            b= Button(self, text=btns[i], command=cmd, width=4, height=2)
            b.grid(row=i//6+3,column=i%6)

    ##this is click function##
    def click(self,key):
        if key in self.right.get() or key in self.wrong.get():
            pass
        elif key in self.word and key not in self.right.get():
            self.right.insert(END,key)
            masked= mask(self.word, self.right.get())
            self.maskedword.delete(0,END)
            self.maskedword.insert(END, masked)
            if '?' not in self.maskedword.get():
                showinfo ('hangman', 'YOU WIN!')
        elif key not in self.word and key not in self.wrong.get():
            self.wrong.insert(END,key)
            if len(self.wrong.get())== 6:
                showinfo('hangman', 'YOU LOSE!')
#TEST
'''
>>> root = Tk()
>>> hangman("APPLE",root).pack()  # will close when “X” cliced
'''
if __name__=='__main__':
    import doctest
    print(doctest.testfile('hw4TEST.py'))




    
