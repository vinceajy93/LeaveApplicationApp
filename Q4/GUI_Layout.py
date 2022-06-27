# after importing tkinter, we will callit tk
import tkinter as tk
# import themed tk package
from tkinter import ttk 
from tkinter import scrolledtext
from QuestionBank import questionBank
from random import randint
class GUI_Layout:
    def __init__(self):
        '''Constructor that creates the window of the GUI for the elements to be filled in.'''
        self._win = tk.Tk() #window container
        self._win.title('Python Quiz - done by Vincent Ang')
        self._win.geometry('400x330')
        self._win.resizable(False, False)
        #variables
        self._questionsList = []
        self._correctAnsCounts = 0
        self._questionCounts = 1
        self._randNum = 0
        self.create_widgets()
        self._win.mainloop()
        

    def create_widgets(self):
        '''method creates the widgets needed for the GUI'''
        #top Frame 
        topFrame = ttk.Frame(self._win)
        topFrame.grid(row=0, column=0)
        #widgets inside topFrame
        self._start_btn = ttk.Button(topFrame, text='Start', command=self.startQuiz)
        self._questions_lbl = ttk.Label(topFrame, text='Questions will appear here')
        #radio button config
        self._radBool = tk.IntVar()
        self._true_rbtn = ttk.Radiobutton(topFrame,text='Option 1',variable=self._radBool, value=1)
        self._false_rbtn = ttk.Radiobutton(topFrame,text='Option 2',variable=self._radBool, value=2)
        self._radBool.set(0)

        #grid positiong top frame
        self._start_btn.grid(row=0, column=0, padx=4, pady=4) 
        self._questions_lbl.grid(row=1, column=0, padx=4, pady=4)
        self._true_rbtn.grid(row=2, column=0, padx=4, pady=4)
        self._false_rbtn.grid(row=3, column=0, padx=4, pady=4)
        

        #action frame containing the submit and next button
        actionFrame =ttk.Frame(topFrame)
        actionFrame.grid(row=4,column=0)

        #widgets inside actionFrame
        self._submit_btn = ttk.Button(actionFrame,text='Submit',command=self.submitQuiz)
        self._next_btn = ttk.Button(actionFrame,text='Next',command=self.nextQuiz)

        #widgets configurations action frame
        self._submit_btn.config(state=tk.DISABLED)
        self._next_btn.config(state=tk.DISABLED)

        #grid positioning action frame
        self._submit_btn.grid(row=4, column=0, padx=4, pady=4)
        self._next_btn.grid(row=4, column=1, padx=4, pady=4)
        
        #bottom frame
        bottomFrame = ttk.Frame(self._win)
        bottomFrame.grid(row=1, column=0)
        #widgets inside bottomFrame
        self._scrolltext = scrolledtext.ScrolledText(bottomFrame, width = 47,height = 10, wrap=tk.WORD)
        #widgets configurations action frame
        self._scrolltext.config(state=tk.DISABLED)
        #grid positioning bottom frame
        self._scrolltext.grid(row=0,column=0)

    def startQuiz(self):
        '''method starts the quiz with questions from the questionBank, player than choose either TRUE or FALSE radio buttont and press submit for the next question.'''
        #reset states to initial
        self._correctAnsCounts = 0
        self._questionCounts = 1
        self._questionsList = questionBank()


        self._start_btn.config(state=tk.DISABLED)
        self._true_rbtn.config(text='TRUE')
        self._false_rbtn.config(text='FALSE')
        self._scrolltext.config(state=tk.NORMAL)
        self._scrolltext.delete(1.0, tk.END)
        self._scrolltext.insert('end', "Select answer and click Submit.\n")
        self._scrolltext.config(state=tk.DISABLED)
        self._submit_btn.config(state=tk.NORMAL)

        #using random to randomly select a quiz question
        self._randNum = randint(0,len(self._questionsList)-1)
        self._questions_lbl.config(text=f"Q{self._questionCounts}. {self._questionsList[self._randNum][0]}")

    def submitQuiz(self):
        '''checks for the correct answer being submitted and adds its to the number of correct answers for display when last question is answered.'''
        #convert radio selection to true/false and print error message if invalid
        if self._radBool.get() == 0:
            self._scrolltext.config(state=tk.NORMAL)
            self._scrolltext.insert('end',f"Please select answer for question {self._questionCounts}\n")
            self._scrolltext.config(state=tk.DISABLED)
        elif self._radBool.get() == 1:
            selection = True
        else:
            selection = False
        try:
            if selection == self._questionsList[self._randNum][1]:
                self._scrolltext.config(state=tk.NORMAL)
                self._scrolltext.insert('end', f"Question {self._questionCounts} is correct!\n")
                self._scrolltext.config(state=tk.DISABLED)
                #increase no. of corrects 
                self._correctAnsCounts +=1
            else:
                self._scrolltext.config(state=tk.NORMAL)
                self._scrolltext.insert('end', f"Question {self._questionCounts} is incorrect!\n")
                self._scrolltext.config(state=tk.DISABLED)
        except Exception as e:
            print(e)
        else:
            self._submit_btn.config(state=tk.DISABLED)
            self._next_btn.config(state=tk.NORMAL)
            self._scrolltext.see('end')

    def nextQuiz(self):
        '''displays the next question, cleans off selection and increases question count by 1. check if there is any more questions, if not will display total score and enable start button'''
        self._questionCounts += 1
        self._questionsList.pop(self._randNum)
        #reset seleciton
        self._radBool.set(0)
        #get new question with random
        if self._questionCounts < 5:
            self._randNum = randint(0,len(self._questionsList)-1)
            self._questions_lbl.config(text=f"Q{self._questionCounts}. {self._questionsList[self._randNum][0]}")
            self._submit_btn.config(state=tk.NORMAL)
            self._next_btn.config(state=tk.DISABLED)
        else:  
            #reset states for new game and display score
            self._next_btn.config(state=tk.DISABLED)
            self._start_btn.config(state=tk.NORMAL)
            self._scrolltext.config(state=tk.NORMAL)
            self._questions_lbl.config(text='Questions will appear here')
            self._true_rbtn.config(text='Option 1')
            self._false_rbtn.config(text='Option 2')
            self._scrolltext.insert('end',f"Quiz complete. Total {self._correctAnsCounts} answers correct.\nClick start to attempt quiz again.\n")
            self._scrolltext.config(state=tk.DISABLED)
            self._scrolltext.see('end')
            