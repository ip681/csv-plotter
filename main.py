import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_file = tk.Button(self)
        self.select_file["text"] = "Load CSV file"
        self.select_file["command"] = self.load_csv_file
        self.select_file.pack(side="top")

        self.quit = tk.Button(self, text="Close", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def load_csv_file(self):
        file_path = filedialog.askopenfilename(defaultextension='.csv')
        if file_path:
            df = pd.read_csv(file_path)
            fig, ax = plt.subplots()
            ax.plot(df['x'], df['y'])
            canvas = FigureCanvasTkAgg(fig, master=self.master)
            canvas.draw()
            canvas.get_tk_widget().pack()


root = tk.Tk()
root.title("CSV Plotter")
root.geometry("600x500")
app = Application(master=root)
app.mainloop()
