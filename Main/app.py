try:
    import tkinter as tk                
    from tkinter import font as tkfont  
    from tkinter import *
except ImportError:
    import Tkinter as tk     
    import tkFont as tkfont  

import sqlite3

conn = sqlite3.connect('/home/alex/Visual Studio Code/Python/Application/database.db')

c = conn.cursor()



#c.execute("""CREATE TABLE data (
#        first_name text,
#        last_name text,
#       email text
#        )""")




class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=12)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible 
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pahv's Tkinter Test Application", font=controller.title_font, fg='black')
        label.pack(side="top", fill="x", pady=50)

        button1 = tk.Button(self, text="Continue",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Learn more...",
                            command=lambda: controller.show_frame("PageTwo"))
        #button3 = tk.Button(self, text="Learn more",
        #                    command=lambda: controller.show_frame("PageThree"))
        button1.pack(fill='x')
        button2.pack()
       # button3.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome, get started by pressing the 'Continue' button below.", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button3 = tk.Button(self, text="Continue",
                            command=lambda: controller.show_frame("PageThree"))
        button3.pack()
        
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This code was written by Pahv", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button3 = tk.Button(self, text="Learn more",
                          command=lambda: controller.show_frame("PageThree"))
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Enter your details", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        def submit_it():
         c.execute('INSERT INTO data(first_name, last_name, email)VALUES (%s, %s, %s)', (fn, ln, em)) # ERROR 
  # c.execute('INSERT INTO data(first_name, last_name, email)VALUES (%s, %s, %s)', (fn, ln, em)) 
  # sqlite3.OperationalError: near "%": syntax error
        
        
        l1 = tk.Label(self,text="Forename")
        l1.pack()

        entryfn = tk.Entry(self)
        entryfn.pack()

        l2 = tk.Label(self,text="Surname")
        l2.pack()

        entryln = tk.Entry(self)
        entryln.pack()

        l3 = tk.Label(self,text="Email")
        l3.pack()

        entryem = tk.Entry(self)
        entryem.pack()

        fn = entryfn.get()
        ln = entryln.get()
        em = entryem.get()

        submitfn = tk.Button(self, text = 'Submit', command = submit_it)
        submitfn.pack(fill='x')

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side='bottom',fill='x')


conn.commit()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
