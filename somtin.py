import tkinter as tk

class facedrawer:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=300, bg='white')
        self.canvas.pack()
        self.draw_face()
    def draw_face(self):
        self.canvas.create_oval(50, 50, 250, 250, fill='yellow', outline='black', width=2)
        self.canvas.create_oval(100, 110, 130, 140, fill='white', outline='black')
        self.canvas.create_oval(170, 110, 200, 140, fill='white', outline='black')
        self.canvas.create_oval(115, 125, 125, 135, fill='black')
        self.canvas.create_oval(185, 125, 195, 135, fill='black')
        self.canvas.create_arc(110, 170, 190, 220, start=0, extent=180, fill='', outline='black', width=2)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("face drawer")
    face = facedrawer(root)
    root.mainloop()