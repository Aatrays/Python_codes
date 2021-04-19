from tkinter import *

class Window(Frame):

    def __init__(self,master = None):

        Frame.__init__(self, master)
        
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Command-Line")

        self.pack(fill=BOTH, expand=1)

        # creating a menu instance

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object

        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        file.add_command(label='Exit', command=self.client_exit)

        # added file to our menu
        menu.add_cascade(label='File', menu = file)

        # create the file object

        edit = Menu(menu)

        edit.add_command(label="Undo")

        menu.add_cascade(label="Edit", menu=edit)

        options = Menu(menu)

        options.add_command(label='Configure', command=self.configure_text)

        menu.add_cascade(label="Options", menu = options)
        

    def client_exit(self):
        exit()

    def configure_text(self):
        print("Hi welcome to the Window")


root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()
