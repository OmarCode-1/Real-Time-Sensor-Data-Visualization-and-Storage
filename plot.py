import excelSheet as excel
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime 
from time import *
from tkinter import messagebox
import serial
import threading
import sys
from dataBase import *

# Global variables
stop_thread = False
read = ""

# Function to establish a connection to the serial port
def connection_to_port(port_name, baud_rate):
    try:
        ser = serial.Serial(port_name, baudrate=baud_rate, timeout=1)
        sleep(2)
        return ser
    except:
        messagebox.showerror("Error", "Error when open port.")
        sys.exit()


# Function to read data from the serial port
def reading(ser):
    global read
    while not stop_thread:
        try:
            read = ser.readline().decode('utf-8').strip()
        except:
            messagebox.showerror("Error", "Error when open port.")
            sys.exit()

def get(port_name, baud_rate, record_name):
    """
    Function to show the graph
    """
    
    # Create object (the graph)
    fig = plt.figure()
    # Choose type of graph
    ax = fig.add_subplot(111)
    # x axis array
    xs = []
    # y axis array
    ys = []
    # first line record 
    first_line = []
    # second line record
    second_line = []
    # arrays to store the information 
    time_list, sub_times, dates = [], [], []
    # Get the real time
    start_time = time()

    # Get the time now
    start_time_string = strftime("%I:%M:%S %p")

    ser = connection_to_port(port_name, baud_rate)
    if ser != None :

        # Create and start the reading thread
        global stop_thread
        t1 = threading.Thread(target=reading, args=(ser,))
        t1.daemon = True
        t1.start()

        def chooseColor(read : int):
            if read > 800:
                return "red"
            elif read < 300 :
                return "blue"
            elif read < 800 and read > 700 :
                return "yellow"
            else :
                return "#1f77b4"

        def animate(i, xs, ys, first_line, second_line):
            """
            Function to create the graph live
            """
            
            # Add x and y to lists
            xs.append(len(xs) + 1)  # time (Seconds)
            
            ys.append(int(read))  # values

            first_line.append(800)
            second_line.append(250)

            time_list.append(strftime("%I:%M:%S %p")) # time
            sub_times.append(time() - start_time) # sub time every record
            dates.append(datetime.now().date().strftime('%d-%m-%Y')) # date for every record
            
            # Adjust the x-axis limits to keep recent data centered
            if len(xs) > 0:
                ax.set_xlim(max(0, (len(xs) + 1) - 5), (len(xs) + 1) + 5)  # Center the last value

            # Limit x and y lists
            if len(ys) > 100:
                ys = ys[-150:]
                xs = xs[-150:]

            # Draw x and y lists
            ax.clear()
            ax.plot(ys, color=chooseColor(int(read)))
            ax.plot(first_line, color = "green")
            ax.plot(second_line, color="green")
            ax.set_ylim([0, 1200])

            ax.grid(True)

            # Titles
            plt.title('Time')
            plt.ylabel('Sensor read value')

        # Set up plot to call animate() function periodically
        ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(xs, ys, first_line, second_line), interval=100)

        # Function to be called when the plot window is closed
        def on_close(event):
            global stop_thread
            # set The stop thread flag to true .
            stop_thread = True

            # Get the length of records
            records = len(xs)

            # calculate the date :
            date = datetime.now().date()
            # get the time now :
            end_time_string = strftime("%I:%M:%S %p")
            # get the time :
            end_time = time()
            # calculate the duration :
            duration = end_time - start_time

            addRecordInDataBase(record_name, start_time_string, end_time_string, date, duration, records, port_name, baud_rate, xs, ys, time_list, sub_times, dates)

            dictionary = excel.getDictionary(xs, ys, time_list, sub_times, dates)

            # Export excel sheet automatically . 
            excel.exportExcelSheet(record_name, dictionary, xs, ys, port_name, baud_rate, start_time_string, records, date, end_time_string, duration)
            
            # turn of the thread .
            t1.join()
        # Connect the on_close function to the close event of the plot window
        fig.canvas.mpl_connect('close_event', on_close)

        # Show the graph 
        plt.show()
        plt.pause(0.2)
