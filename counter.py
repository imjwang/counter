import tkinter as tk
from pynput import mouse, keyboard

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.clicks = 0
        self.keys = 0
        self.stats = tk.Label(
                            text="Clicks: {}\t Keys: {}".format(self.clicks, self.keys),
                            foreground="green",
                            background="black"
                            )
        self.stats.pack()
        self.set_up_clicks()
        self.set_up_keys()
        
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.clicks += 1
            self.stats.configure(text="Clicks: {}\t Keys: {}".format(self.clicks, self.keys))
            if self.clicks % 100 == 0 and self.clicks != 0:
                print("congrats!")
        

    def on_press(self, f):
        self.keys += 1
        self.stats.configure(text="Clicks: {}\t Keys: {}".format(self.clicks, self.keys))
        if self.keys % 1000 == 0 and self.keys != 0:
            print("congrats!")

    def set_up_clicks(self):
        listener = mouse.Listener(on_click=self.on_click)
        listener.start()

    def set_up_keys(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

root = tk.Tk()
app = Application(master=root)
app.master.title("Work Counter")
app.mainloop()