# include libraries:
from plot import *
import customtkinter as tk
from tkinter import messagebox

def liveRecord(main_page):
    # ====================== Name ==============================

    record_label = tk.CTkLabel(main_page, text="Record Name", text_color="black")
    record_label.place(x= 12, y=0)

    record_name = tk.CTkEntry(main_page, width= 180)
    record_name.place(x= 10, y=23)

    # ====================== Port ==============================
    # names of ports
    ports_name = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"]

    # create variable to store the selected option
    port_name_value = tk.StringVar(main_page)
    # set the first name
    port_name_value.set("Select port")

    # create option menu to select the port
    port_option_menu = tk.CTkOptionMenu(main_page, font=("Times",15,"bold"), variable= port_name_value, values=ports_name,width=120, height=30)

    # optionmenu's placing
    port_option_menu.place(x= 200, y=20)

    # ====================== baud rates ==========================
    # names of ports
    baud_rates = ["4800", "9600", "19200", "38400", "57600", "115200", "230400", "460800", "921600"]
    # create variable to store the selected option
    baud_rate_value = tk.StringVar(main_page)
    # set the first name
    baud_rate_value.set("Select baud rate")

    # create option menu to select the baud rate
    baud_rate_options_menu = tk.CTkOptionMenu(main_page, font=("Times",15,"bold"), variable= baud_rate_value, values=baud_rates,width=120, height=30)

    # optionmenu's placing
    baud_rate_options_menu.place(x= 350, y=20)





    def start():
        """
            function to take action when the user push start    
        """
        #  get name of record :
        name_of_record = record_name.get()
        # get the port name :
        port_name = port_name_value.get()
        # get the baud rate :
        baud_rate = baud_rate_value.get()

        if len(name_of_record) > 1 and "Select baud rate" not in baud_rate and "Select port" not in port_name:
            # show the graph
            get(port_name, baud_rate, name_of_record)
        else :
            messagebox.showerror("Error", "You must choose a baud rate, port name and fill the record name .")

    # definition the button :
    start_button = tk.CTkButton(main_page, font=("Times",15,"bold"), text="Start", command=start)
    # button placing:
    start_button.place(x= 520, y=21)

