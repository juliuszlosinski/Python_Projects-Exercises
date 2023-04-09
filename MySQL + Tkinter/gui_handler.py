import tkinter as tk
from tkinter import ttk

import database as db
import db_configuration as db_conf
from data_wrapper import DataReaderWrapperIoT

TEXT_TEMPERATURE_LABEL = "Temperature"
TEXT_HUMIDITY_LABEL = "Humidity"
TEXT_VOLTAGE_LABEL = "Voltage"

# 0. Setting up connection with database.
conn = db.Database(
    host=db_conf.HOST,
    user=db_conf.USER,
    password=db_conf.PASSWORD
)
conn.db = db_conf.DB_NAME


class IoTGUI:
    def print_current_selection(self):
        """
        Printing currently selected attribute of measurement.
        """
        if self.checkbox_temperature_value.get():
            print("Checkbox temperature is selected.")
        elif self.checkbox_humidity_value.get():
            print("Checkbox humidity is selected.")
        elif self.checkbox_voltage_value.get():
            print("Checkbox voltage is selected.")

    def show_chart_button_handler(self):
        """
        Getting all information from GUI and creating chart by using DataReaderWrapperIoT module.
        """
        current_config = "Config: \n" \
                         "Selected attribute: "
        if self.checkbox_temperature_value.get():
            current_config += "temperature"
        if self.checkbox_humidity_value.get():
            current_config += "humidity"
        if self.checkbox_voltage_value.get():
            current_config += "voltage"

        start_date = f"{self.combo_selected_start_year.get()}-{self.combo_selected_start_month.get()}-{self.combo_selected_start_day.get()}"
        start_date += " "
        start_date += f"{self.combo_selected_start_hour.get()}-{self.combo_selected_start_minute.get()}-{self.combo_selected_start_second.get()}"

        end_date = f"{self.combo_selected_end_year.get()}-{self.combo_selected_end_month.get()}-{self.combo_selected_end_day.get()}"
        end_date += " "
        end_date += f"{self.combo_selected_end_hour.get()}-{self.combo_selected_end_minute.get()}-{self.combo_selected_end_second.get()}"

        current_config += f"\nStart date: {start_date}\nEnd date: {end_date}\n"

        print(current_config)

        self.data_handler.read_all_data(
            start_time=start_date,
            end_time=end_date,
            show_voltage=self.checkbox_voltage_value.get(),
            show_humidity=self.checkbox_humidity_value.get(),
            show_temperature=self.checkbox_temperature_value.get()
        )

    def __init__(self):

        # Setting icon of master window
        self.data_handler = DataReaderWrapperIoT()
        self.window = tk.Tk()

        icon = tk.PhotoImage(file='icon.png')
        background_image = tk.PhotoImage(file='background.png')

        self.window.iconphoto(False, icon)
        self.window.title("IoT Application")
        self.window.geometry("300x400")
        self.window.resizable(False, False)

        # 1. Setting up checkboxes.
        self.checkbox_temperature_value = tk.IntVar()
        self.checkbox_humidity_value = tk.IntVar()
        self.checkbox_voltage_value = tk.IntVar()
        background = tk.Label(self.window, image=background_image)
        background.place(x=0, y=0)
        left_frame = tk.Frame(master=self.window, width=300, height=400, bg='', bd=5)
        left_frame.grid(row=0, column=0, padx=1, pady=1)
        left_frame.grid_propagate(False)
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)
        tk.Label(left_frame, text="Select attributes:", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=5)

        self.checkbox_temperature = tk.Checkbutton(
            left_frame,
            text=f"{TEXT_TEMPERATURE_LABEL}",
            variable=self.checkbox_temperature_value,
            onvalue=1,
            offvalue=0,
            command=self.print_current_selection
        )
        self.checkbox_temperature.select()
        self.checkbox_temperature.grid(row=1, column=0, padx=5, pady=5)

        self.checkbox_humidity = tk.Checkbutton(
            left_frame,
            text=f"{TEXT_HUMIDITY_LABEL}",
            variable=self.checkbox_humidity_value,
            onvalue=1,
            offvalue=0,
            command=self.print_current_selection
        )
        self.checkbox_humidity.select()
        self.checkbox_humidity.grid(row=2, column=0, padx=5, pady=5)

        self.checkbox_voltage = tk.Checkbutton(
            left_frame,
            text=f"{TEXT_VOLTAGE_LABEL}",
            variable=self.checkbox_voltage_value,
            onvalue=1,
            offvalue=0,
            command=self.print_current_selection
        )
        self.checkbox_voltage.select()
        self.checkbox_voltage.grid(row=3, column=0, padx=5, pady=5)

        tk.Label(left_frame, text="Select start date and time:", relief=tk.RAISED).grid(row=4, column=0, padx=5, pady=5)

        years = list(range(2000, 2031))
        months = list(range(1, 13))
        days = list(range(1, 31))
        hours = list(range(1, 24))
        minutes = list(range(1, 60))
        seconds = list(range(1, 60))

        # 1. Setting up widgets for start/ end date time.
        start_time_and_data_frame = tk.Frame(master=left_frame, width=600, height=400, bg='grey')
        start_time_and_data_frame.grid(row=5, column=0, padx=1, pady=1)

        self.combo_selected_start_year = ttk.Combobox(
            master=start_time_and_data_frame,
            values=years,
            state="readonly",
            width=5
        )
        self.combo_selected_start_year.current(0)
        self.combo_selected_start_year.grid(row=1, column=0, padx=0, pady=0)

        self.combo_selected_start_month = ttk.Combobox(
            master=start_time_and_data_frame,
            values=months,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_start_month.current(0)
        self.combo_selected_start_month.grid(row=1, column=1, padx=0, pady=0)

        self.combo_selected_start_day = ttk.Combobox(
            master=start_time_and_data_frame,
            values=days,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_start_day.current(0)
        self.combo_selected_start_day.grid(row=1, column=2, padx=0, pady=0)

        self.combo_selected_start_hour = ttk.Combobox(
            master=start_time_and_data_frame,
            values=hours,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_start_hour.current(0)
        self.combo_selected_start_hour.grid(row=2, column=0, padx=0, pady=0)

        self.combo_selected_start_minute = ttk.Combobox(
            master=start_time_and_data_frame,
            values=minutes,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_start_minute.current(0)
        self.combo_selected_start_minute.grid(row=2, column=1, padx=0, pady=0)

        self.combo_selected_start_second = ttk.Combobox(
            master=start_time_and_data_frame,
            values=seconds,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_start_second.current(0)
        self.combo_selected_start_second.grid(row=2, column=2, padx=0, pady=0)

        tk.Label(left_frame, text="Select end date and time:", relief=tk.RAISED).grid(row=7, column=0, padx=5, pady=5)

        end_time_and_data_frame = tk.Frame(master=left_frame, width=600, height=400, bg='grey')
        end_time_and_data_frame.grid(row=8, column=0, padx=1, pady=1)

        self.combo_selected_end_year = ttk.Combobox(
            master=end_time_and_data_frame,
            values=years,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_end_year.current(len(years) - 1)
        self.combo_selected_end_year.grid(row=1, column=0, padx=0, pady=0)

        self.combo_selected_end_month = ttk.Combobox(
            master=end_time_and_data_frame,
            values=months,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_end_month.current(len(months) - 1)
        self.combo_selected_end_month.grid(row=1, column=1, padx=0, pady=0)

        self.combo_selected_end_day = ttk.Combobox(
            master=end_time_and_data_frame,
            values=days,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_end_day.current(len(days) - 1)
        self.combo_selected_end_day.grid(row=1, column=2, padx=0, pady=0)

        self.combo_selected_end_hour = ttk.Combobox(
            master=end_time_and_data_frame,
            values=hours,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_end_hour.current(len(hours) - 1)
        self.combo_selected_end_hour.grid(row=2, column=0, padx=0, pady=0)

        self.combo_selected_end_minute = ttk.Combobox(
            master=end_time_and_data_frame,
            values=minutes,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_end_minute.current(len(minutes) - 1)
        self.combo_selected_end_minute.grid(row=2, column=1, padx=0, pady=0)

        self.combo_selected_end_second = ttk.Combobox(
            master=end_time_and_data_frame,
            values=seconds,
            state="readonly",
            width=5,
            justify='center'
        )
        self.combo_selected_end_second.current(len(seconds) - 1)
        self.combo_selected_end_second.grid(row=2, column=2, padx=0, pady=0)

        tk.Label(left_frame, text="Select device id:", relief=tk.RAISED).grid(row=9, column=0, padx=5, pady=5)

        # 3. Fetching all data from database.
        devices = conn.getArray("SELECT * FROM devices")
        self.device_ids: list = []
        for device in devices:
            self.device_ids.append(device[0])
        print(self.device_ids)

        # 4. Creating combobox gui widget.
        self.combo_selected_device_id = ttk.Combobox(
            master=left_frame,
            values=self.device_ids,
            state="readonly",
            justify='center'
        )
        self.combo_selected_device_id.current(0)
        self.combo_selected_device_id.grid(row=10, column=0, padx=0, pady=0)

        # 5. Creating start button.
        self.start_button = ttk.Button(
            master=left_frame,
            text="Show chart",
            command=self.show_chart_button_handler
        )
        self.start_button.grid(row=11, column=0, padx=0, pady=7)

        # 6. Starting the GUI application.
        self.window.mainloop()


# Launching the IoT application.
gui = IoTGUI()
