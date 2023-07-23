from tkinter import *
import random

word_list = ["You must understand the whole of life, not just one part of it. That is why you must read, that is why "
             "you must look at the skies, why you must sing, dance and write poems, and suffer, and understand, "
             "for all that is life.", "All great things start on a small scale, all great movements begin with "
                                      "individuals, and if we wait for collective action, such action if it takes "
                                      "place at all is destructive and conducive to further misery. So revolution "
                                      "must begin with you and me.", "The more you know yourself, the more clarity "
                                                                     "there is. Self-knowledge has no end – you don't "
                                                                     "achieve, you don’t come to a conclusion. It is "
                                                                     "an endless river.When death comes, it does not "
                                                                     "ask your permission; it comes and takes you, "
                                                                     "it destroys you on the spot."]


##THIS CREATES THE CLASS FOR THE WINDOW AND METHODS
class Speed_test:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('700x700')
        self.canvas = Canvas(self.window, width=500, height=300, bg="#D9EEF3")
        self.canvas.pack(fill=BOTH, pady=5, ipady=5, ipadx=5)
        self.time_label = Label(self.canvas, text='01:00', font=('Courier', 15, 'bold'))
        self.time_label.pack(pady=3)
        self.start_button = Button(self.canvas, text='Start', width=8, height=1, font=('Arial', 15, 'bold'),
                                   command=lambda: self.count_down(60),
                                   bg='light blue')
        self.word_text = word_list[random.randint(0, 2)]
        self.instruction_label = Label(self.canvas, text='Start your typing test:', font=('Arial', 15, 'bold'))
        self.instruction_label.pack(pady=3)
        self.start_button.pack(pady=3, side=TOP)
        self.text_label = Message(self.canvas, text=self.word_text, font=('Helvetica', 15, 'bold'), bg='#D8FEF3',
                                  width=500)
        self.text_label.pack(pady=5)
        self.t = Text(self.canvas, width=70, height=15, state=DISABLED)
        self.t.pack(pady=5)
        self.response_label = Label(self.canvas, text=f'Your typing speed is:', font=('Arial', 15, 'bold'))
        self.response_label.pack(pady=5)
        self.window.mainloop()

    ##THIS METHOD IS NEEDED WHEN THE TEST FINISHES, IT CREATES A NEW WINDOW WHEN THE RESTART BUTTON IS CLICKED
    def clear_text(self):
        self.window.destroy()
        create_game()

    ##THIS IS RESPONSIBLE FOR THE TIMER,IT STOPS THE RESTART BUTTON AND BRINGS THE TEXT WIDGET TO LIFE
    def count_down(self, count):
        self.t.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        if count >= 11:
            self.time_label.config(text=f'00:{count - 1}', bg='light blue')
            # #THE WINDOW.AFTER METHOD TAKES IN 3 ARGUMENTS, THE FIRST IS THE TIME IN MILLISECONDS AND THE SECOND IS
            # THE FUNCTION TO WORK WITH AND ITS ARGUMENT
            self.window.after(1000, self.count_down, count - 1)
        elif 0 < count <= 10:
            self.time_label.config(text=f'00:0{count - 1}', bg="firebrick1")
            self.window.after(1000, self.count_down, count - 1)
        else:
            self.t.config(state=DISABLED)
            self.typing_speed()
            self.start_button.config(text='Restart', command=self.clear_text, state=NORMAL)

    ##THIS IS RESPONSIBLE FOR THE MATH OF THE SPEED
    def typing_speed(self):
        error = 0
        self.text = self.t.get(1.0, END)
        self.text = self.text.split()
        self.word_text = self.word_text.split()
        for n in range(len(self.text)):
            if self.text[n] != self.word_text[n]:
                error += 1
        speed = (int(len(self.text)) - error / 5)
        self.response_label.config(text=f'Your typing speed is:{speed} words per minutes\nYou had {error} errors')


##THIS INITIALIZES THE CLASS AND CREATES THE OBJECT
def create_game():
    Speed_test()


create_game()
