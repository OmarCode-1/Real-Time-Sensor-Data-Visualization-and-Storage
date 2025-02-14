import customtkinter as tk3
from tkinter import ttk
from DataBaseRecord import *
from liveRecord import *

main_program = tk3.CTk()
main_program.title("Record Analysis")
main_program.geometry("670x220")
main_program.iconbitmap("photos/signal-24.ico")

# Create a Notebook widget
notebook = ttk.Notebook(main_program, width=830, height=250)
notebook.pack()

# Create frames for the tabs
live_record_tab = ttk.Frame(notebook, width=700, height=80)
database_record_tab = ttk.Frame(notebook, width=550, height=200)

# Add the frames to the Notebook
notebook.add(live_record_tab, text="Live Records")
notebook.add(database_record_tab, text="Database Records")

recordInDataBase(database_record_tab)
liveRecord(live_record_tab)

main_program.mainloop()