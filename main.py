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

        #button to closa app - not nessesery
        # self.quit = tk.Button(self, text="Close", fg="black",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def load_csv_file(self):
        file_path = filedialog.askopenfilename(defaultextension='.csv')
        if file_path:
            # delete last chart if it exist
            if hasattr(self, 'canvas'):  # check is have chart
                self.canvas.get_tk_widget().destroy()  # if have chart destroy it

            # Load the new CSV and plot new chart
            df = pd.read_csv(file_path)

            df_grouped = df.groupby('x').sum().reset_index()  # sum y values for duplicated x values
            fig, ax = plt.subplots()
            ax.bar(df_grouped['x'], df_grouped['y'])  # plot bar chart
            ax.set_xlabel('Period')  # show x label
            ax.set_ylabel('Result')  # show Y label
            self.canvas = FigureCanvasTkAgg(fig, master=self.master)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()


root = tk.Tk()
root.title("CSV Plotter")
root.geometry("600x500")
root.configure(bg='#fff')
# root.iconbitmap('resources\icon.ico')
app = Application(master=root)
app.mainloop()
