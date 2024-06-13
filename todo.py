from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do-list")
        self.root.geometry("650x450+300+150")

        self.label = Label(self.root, text="To-Do-list-App",
                           font=("Arial", 25, "bold"),
                           width=20,
                           bd=5,
                           bg="orange",
                           fg="black")
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text="Add task",
                            font=("Arial", 18, "bold"),
                            width=9,
                            bd=5,
                            bg="orange",
                            fg="black")
        self.label2.place(x=20, y=54)

        self.label3 = Label(self.root, text="Tasks",
                            font=("Arial", 18, "bold"),
                            width=10,
                            bd=5,
                            bg="orange",
                            fg="black")
        self.label3.place(x=326, y=54)

        self.main_text = Listbox(self.root,
                                 height=10,
                                 bd=5,
                                 width=26,
                                 font=("Arial", 20, "bold italic"))
        self.main_text.place(x=200, y=100)

        self.text = Text(self.root,
                         bd=5,
                         height=2,
                         width=20,
                         font=("Arial", 10, "bold"))
        self.text.place(x=20, y=120)

        self.text2 = Text(self.root,
                         bd=5,
                         height=2,
                         width=20,
                         font=("Arial", 10, "bold"))
        self.text2.place(x=20, y=330)
        #---------------add task -------------------#
        def add():
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)
                with open("data.txt", 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)

        def delete():
            selected_task_index = self.main_text.curselection()
            if not selected_task_index:
                return
            selected_task = self.main_text.get(selected_task_index)
            self.main_text.delete(selected_task_index)
            with open("data.txt", 'r') as file:
                lines = file.readlines()
            with open("data.txt", 'w') as file:
                for line in lines:
                    if line.strip("\n") != selected_task:
                        file.write(line)

            with open("data.txt", 'r') as file:
                read = file.readlines()
                for task in read:
                    self.main_text.insert(END, task.strip())
                    
                    
        def update():
            selected_task_index = self.main_text.curselection()
            if not selected_task_index:
                return
            selected_task = self.main_text.get(selected_task_index)
            self.main_text.delete(selected_task_index)
            with open("data.txt", 'r') as file:
                lines = file.readlines()
            with open("data.txt", 'w') as file:
                for line in lines:
                    if line.strip("\n") != selected_task:
                        file.write(line)
                        
            content = self.text2.get(1.0, END).strip()
            if content:
                self.main_text.insert(END, content)
                with open("data.txt", 'a') as file:
                    file.write(content + '\n')
                self.text2.delete(1.0, END)

        self.button = Button(self.root, text="Add",
                             font=("Arial", 20, "bold italic"),
                             width=8,
                             bd=5,
                             bg="orange",
                             fg="black",
                             command=add)
        self.button.place(x=15, y=180)

        self.button2 = Button(self.root, text="Delete",
                              font=("Arial", 20, "bold italic"),
                              width=8,
                              bd=5,
                              bg="orange",
                              fg="black",
                              command=delete)
        self.button2.place(x=15, y=250)
        
        
        self.button3 = Button(self.root, text="Update",
                              font=("Arial", 20, "bold italic"),
                              width=8,
                              bd=5,
                              bg="orange",
                              fg="black",
                              command=update)
        self.button3.place(x=15, y=380)


def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()