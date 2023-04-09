import datetime
import matplotlib.pyplot as plt
from database import Database
import db_configuration as db_conf

"""
RecordDataIoT is a wrapper for data/ measurement record.
"""


class RecordDataIoT:
    def __init__(self, id_sample: int, time_sample: datetime.datetime, temperature: float, humidity: float,
                 voltage: float):
        """
        Creating record data IoT based on sent data.
        """
        self.id_sample: int = id_sample
        self.time_sample: datetime.datetime = time_sample
        self.temperature: float = temperature
        self.humidity: float = humidity
        self.voltage: float = voltage

    def __str__(self):
        """
        Overloading the string method.
        """
        return f"id_sample: {self.id_sample}, time_sample: {self.time_sample}, " \
               f"temperature: {self.temperature}, humidity: {self.humidity}, " \
               f"voltage: {self.voltage}"

    def __repr__(self):
        """
        Overloading the printable version of the object.
        """
        return str(self)


"""
DataReaderWrapperIoT is class for reading data/ measurements from iot database.
"""


class DataReaderWrapperIoT:
    def __init__(self):
        """
        Creating DataReaderWrapper
        """
        self.conn = Database(
            host=db_conf.HOST,
            user=db_conf.USER,
            password=db_conf.PASSWORD
        )
        self.conn.db = db_conf.DB_NAME

    def read_all_data(self, start_time: str = None, end_time: str = None, show_temperature=False, show_humidity=False,
                      show_voltage=False):
        # 1. Reading data from database.
        sql = f"SELECT time, temperature, humidity, voltage " \
              "FROM data " \
              f"WHERE device_id = {db_conf.DEVICE_ID} " \
              f"AND time > '{start_time}'" \
              f"AND time < '{end_time}'"
        print(sql)
        array = self.conn.getArray(sql)

        # 2. Converting readed data to "RecordDataIoT" format.
        records_iot: list = []

        for record, i in zip(array, range(len(array))):
            records_iot.append(RecordDataIoT(i, record[0], record[1], record[2], record[3]))

        print(records_iot)

        # 3. Creating buffers with specified data.
        id_samples, time_samples, temperatures, humidities, voltages = [], [], [], [], []

        for record in records_iot:
            id_samples.append(record.id_sample)
            time_samples.append(record.time_sample)
            temperatures.append(record.temperature)
            humidities.append(record.humidity)
            voltages.append(record.voltage)

        if show_temperature:
            # 4. Creating plots for visualization purposes.
            plt.plot(id_samples, temperatures, marker='o', color='r')
            plt.title("Temperature (sample of time)")
            plt.ylabel("Temperature [Celsius]")
            plt.xlabel("Sample of time [-]")
            plt.grid(True)
            plt.savefig('Temperature (sample of time).png')
            plt.show()
            plt.close()

        if show_humidity:
            plt.plot(id_samples, humidities, marker='x', color='b')
            plt.title("Humidity (sample of time)")
            plt.xlabel("Sample of time [-]")
            plt.ylabel("Humidity [%]")
            plt.grid(True)
            plt.savefig("Humidity (sample of time).png")
            plt.show()
            plt.close()

        if show_voltage:
            plt.plot(id_samples, voltages, marker='o', color='g')
            plt.title("Voltage (sample of time)")
            plt.xlabel("Sample of time [-]")
            plt.ylabel("Voltage [v]")
            plt.grid(True)
            plt.savefig("Voltage (sample of time).png")
            plt.show()
            plt.close()

        if show_humidity and show_voltage and show_temperature:
            fig, axs = plt.subplots(3)
            fig.suptitle('Measurements of temperature, humidity and voltage in time')
            axs[0].plot(id_samples, temperatures, marker='o', color='r')
            axs[0].grid(True)
            axs[0].set(ylabel='Temperature [Celsius]')
            axs[1].plot(id_samples, humidities, marker='x', color='b')
            axs[1].grid(True)
            axs[1].set(ylabel='Humidity [%]')
            axs[2].plot(id_samples, voltages, marker='o', color='g')
            axs[2].grid(True)
            axs[2].set(xlabel='Sample of time [-]', ylabel='Voltage [v]')
            plt.savefig("Measurements of temperature, humidity and voltage in time.png")
            plt.show()
            plt.close()
