# Real-Time Sensor Data Visualization and Storage
This Python project allows you to read live sensor data from a serial port, visualize it in real-time using Matplotlib, and store the   
data in an SQLite database. You can also retrieve the stored data from the database and plot it for analysis..
# Features
- Real-time data visualization: Live graph plotting of sensor data using Matplotlib.

- Data storage: Store sensor data in an SQLite database for later retrieval.

- Data retrieval: Fetch stored data from the database and visualize it.

- Flexible and modular: Easily adaptable to work with any sensor or serial data source.

- Lightweight and efficient: Uses SQLite for local data storage and Matplotlib for visualization.

# How It Works
1- Read sensor data: The program reads data from a serial port (e.g., Arduino, Raspberry Pi, or any sensor connected via UART).

2- Live graph: The data is plotted in real-time using Matplotlib.

3- Store data: The sensor data is saved in an SQLite database for future use.

4- Retrieve and plot data: You can fetch the stored data from the database and plot it using Matplotlib.


# Requirements
* Python 
* Libraries:
  - pyserial (for reading serial data)
  - matplotlib (for real-time plotting)
  - sqlite3 (for database operations)

