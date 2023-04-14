import serial
import matplotlib.pyplot as plt
import ctypes as ctype
import numpy as np

"""
PortHandler is a class for handling COM ports.
"""
class PortHandler:

    def __init__(self, port: str, baudrate: int = 115200, timeout: int = 0.2) -> None:
        """
        Initializing PortHandler instance.
        :param port: Port id like COM6, COM7 etc.
        :param baudrate: Baud rate such as 9600 or 115200 etc.
        :param timeout: Read timeout value in seconds.
        """
        # Connecting with port
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

        # Setting up flag about being connected.
        self.connected = False
        if self.ser.name != "":
            print(f"{port} is connected!")
            self.connected = True

        # Getting config.
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    def print_config(self) -> None:
        """
        Printing current configuration of port handler.
        """
        print(f"CONNECTED: {self.connected}\n"
              f"PORT NAME: {self.ser.name}\n"
              f"BAUDRATE: {self.baudrate}\n"
              f"TIMEOUT: {self.timeout}\n")

    def ping(self) -> None:
        """
        Pinging the device.
        """
        self.flush()
        print(self.exec("ping", 10))

    def exec(self, command: str = "", bytes_to_read: int = 10) -> str:
        """
        Executing the command.
        """
        self.flush()
        self.ser.write(bytes(command, 'ascii'))
        readed = self.ser.read(bytes_to_read)
        return str(readed, "ascii")

    def exec_bytes(self, command: str = "", bytes_to_read: int = 10):
        """
        Executing the command.
        """
        self.flush()
        self.ser.write(bytes(command, 'ascii'))
        readed = self.ser.read(bytes_to_read)
        return readed

    def flush(self) -> None:
        """
        Flushing the IO buffer.
        """
        self.ser.flushInput()
        self.ser.flushOutput()

    def list_files(self) -> None:
        """
        List all files.
        """
        self.flush()
        print(self.exec("file list", 10000000))

    def file_cache(self) -> None:
        """
        File cache.
        """
        self.flush()
        print(self.exec("file cache 2"), 100000)

    def file_rand(self) -> None:
        self.flush()
        print(self.exec("file rand", 10000))

    def file_load(self) -> None:
        self.flush()
        file = open("cipher.txt", "+w")
        n = 50
        x_axis = list(range(1, n))
        y_axis_data = []
        for i in range(1, n):
            decoded = self.exec_bytes(f"file load 4 {i*4}", 100)
            decoded = int.from_bytes(decoded, byteorder="big")
            y_axis_data.append(decoded)
        file.close()
        plt.plot(x_axis, y_axis_data, marker='o', color='r')
        plt.title("f(x)")
        plt.ylabel("f(x)")
        plt.xlabel("x")
        plt.grid(True)
        plt.savefig('f_od_x.png')
        plt.show()
        plt.close()


pH = PortHandler("COM6")
pH.print_config()
pH.ping()
pH.list_files()

pH.file_rand()
pH.file_cache()
pH.file_load()
