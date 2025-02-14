import customtkinter as tk2
import tkinter as tk
from tkinter import messagebox
from dataBase import *
from excelSheet import *

def recordInDataBase(root) :

    # Create a Listbox
    listbox = tk.Listbox(root, selectmode=tk.SINGLE,width=100, height=10)
    listbox.place(x=10, y = 80)

    def clearListBox():
        listbox.delete(0, tk.END)

    def insertItem(item):
        # clear the listbox :
        clearListBox()

        # Populate the Listbox with items
        listbox.insert(tk.END, item[1])
            
    def insertItems():
        # clear the listbox :
        clearListBox()

        # Populate the Listbox with items
        items = allRecords()
        for item in items:
            listbox.insert(tk.END, item[1])

    # Function to handle the selection
    def on_select(event=None):
        # Get the index of the selected item
        selected_index = listbox.curselection()
        if selected_index:
            # Retrieve the value of the selected item
            selected_value = listbox.get(selected_index)
        
        return selected_value

    def excelExport():
        name_of_record = on_select()
        record_information = getInformationAboutRecord(name_of_record) 
        # name, start_time, end_time, date, duration, len_records, port_name, baud_rate, records, _values, time, sub_time, dates
        # [1] ,     [2]   ,   [3]   ,  [4],    [5]  ,     [6]    ,   [7]    ,    [8]   ,    [9] ,   [10] , [11],    [12] , [13] 

        dictionary = getDictionary(record_information[9], record_information[10], record_information[11], record_information[12], record_information[13])
        # print(dictionary)
        # Export excel sheet automatically
        exportExcelSheet(record_information[1], dictionary, record_information[9], record_information[10], record_information[7], record_information[8], record_information[2], record_information[6], record_information[4], record_information[3], record_information[5])


    def deleteRecord():
        """
            this function to delete the record from data base.
        """
        # get the name of record :
        name_of_record = on_select()

        # delete it :
        delRecord(name_of_record)

        # refresh the items in list box :
        insertItems()

    # Enter name label
    name_label = tk2.CTkLabel(root, text="Name of Record", text_color="black")
    name_label.place(x=50, y=20)

    # name entry :
    name_entry = tk2.CTkEntry(root, width=150, height=10)
    name_entry.place(x=160, y=23)

    # # Search Button and his function 
    def findRecordBySearch():
        name_of_record = name_entry.get()

        if len(name_of_record) > 1:
            insertItem(getInformationAboutRecord(name_of_record))
        else :
            messagebox.showerror("Error", "Entry Field is empty")
    
    # search button :
    search_button = tk2.CTkButton(root, text="Search", command=findRecordBySearch, bg_color="white", fg_color="green", width=100)
    search_button.place(x=320, y=22)

    # re insert the plot:
    search_button = tk2.CTkButton(root, text="re", command=insertItems, bg_color="white", fg_color="gray", width=50)
    search_button.place(x=430, y=22)


    # Excel Button :
    excel_button = tk2.CTkButton(root, text="Excel", command=excelExport, bg_color="white")
    excel_button.place(x = 510, y = 10)

    def exportPlot():
        name_of_record = on_select()
        record_information = getInformationAboutRecord(name_of_record) 
        showGraph(record_information[12], record_information[10])

    # Export plot :
    plot_button = tk2.CTkButton(root, text="Export Plot", command=exportPlot, bg_color="white")
    plot_button.place(x = 510, y = 45)

    # Del Button:
    del_button = tk2.CTkButton(root, text="Delete", command=deleteRecord, bg_color="white")
    del_button.place(x = 510, y = 80)

    

    # Bind the selection event to the on_select function
    listbox.bind('<<ListboxSelect>>', on_select)
    root.bind('<Return>', findRecordBySearch)
    insertItems()
