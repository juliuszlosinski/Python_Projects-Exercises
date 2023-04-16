import tkinter as tk
from array import array
from tkinter import ttk
import numpy as np
import gpu_linear_regression
import gpu_linear_regression as gpu_lin_reg


class GPUGUI:

    def print_selected_graphics_api(self) -> None:
        """
        Printing currently selected graphics api (OpenGL, DirectX 12).
        """
        n = 32
        print(f"\n{n * '*'}")
        if self.checkbox_opengl_value.get():
            print("Checkbox OpenGL is selected!")
        else:
            print("Checkbox OpenGL is NOT selected!")
        if self.checkbox_directX_value.get():
            print("Checkbox DirectX 12 is selected!")
        else:
            print("Checkbox DirectX 12 is NOT selected!")
        print(f"{n * '*'}\n")

    def show_chart_button_handler(self):
        if self.checkbox_opengl_value.get():
            self.gpu_regres.draw_opengl_scatter_chart_with_trend_line()
            self.gpu_regres.draw_opengl_plot_chart_with_trend_line()
        if self.checkbox_directX_value.get():
            self.gpu_regres.draw_directx12_scatter_chart_with_trend_line()
            self.gpu_regres.draw_directx12_plot_chart_with_trend_line()

    def calc_predicted_values(self):
        if self.checkbox_opengl_value.get():
            opengl_values = list(range(0, int(self.selected_time_range.get())))
            predicted_opengl_values = self.gpu_regres.predict_opengl(np.array(opengl_values))
            print(predicted_opengl_values)
            self.output_opengl_predicted_values.delete(1.0, tk.END)
            self.output_opengl_predicted_values.insert(tk.END, predicted_opengl_values)
        if self.checkbox_directX_value.get():
            directX12_values = list(range(0, int(self.selected_time_range.get())))
            predicted_directX12_values = self.gpu_regres.predict_directx12(np.array(directX12_values))
            print(predicted_directX12_values)
            self.output_directx12_predicted_values.delete(1.0, tk.END)
            self.output_directx12_predicted_values.insert(tk.END, predicted_directX12_values)

    def __init__(self):
        self.gpu_regres = gpu_linear_regression.GraphicsAPIBenchmark()

        self.window = tk.Tk()

        icon = tk.PhotoImage(file='icon.png')
        background_image = tk.PhotoImage(file='background.png')

        self.window.iconphoto(False, icon)
        self.window.title("GPU Benchmark")
        self.window.geometry("300x500")
        self.window.resizable(False, False)

        background = tk.Label(self.window, image=background_image)
        background.place(x=0, y=0)
        left_frame = tk.Frame(master=self.window, width=300, height=500, bg='', bd=5)
        left_frame.grid(row=0, column=0, padx=1, pady=1)
        left_frame.grid_propagate(False)
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)
        tk.Label(left_frame, text="Select attributes:", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=5)

        row_index = 1
        tk.Label(left_frame, text="Select graphics API:", relief=tk.RAISED) \
            .grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        self.checkbox_opengl_value = tk.IntVar()
        self.checkbox_directX_value = tk.IntVar()

        self.checkbox_opengl = tk.Checkbutton(
            left_frame,
            text="OpenGL",
            variable=self.checkbox_opengl_value,
            onvalue=1,
            offvalue=0,
            command=self.print_selected_graphics_api
        )
        self.checkbox_opengl.select()
        self.checkbox_opengl.grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        self.checkbox_directX = tk.Checkbutton(
            left_frame,
            text="DirectX 12",
            variable=self.checkbox_directX_value,
            onvalue=1,
            offvalue=0,
            command=self.print_selected_graphics_api
        )
        self.checkbox_directX.select()
        self.checkbox_directX.grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        self.show_charts_button = tk.Button(
            master=left_frame,
            text="Show chart",
            command=self.show_chart_button_handler,
            bg='#FFFF00'
        )
        self.show_charts_button.grid(row=row_index, column=0, padx=0, pady=7)

        row_index += 1

        # Select range for prediction
        time_range = list(range(1, 1000))  # [s]
        self.selected_time_range = ttk.Combobox(
            master=left_frame,
            values=time_range,
            state="readonly",
            width=5
        )
        self.selected_time_range.current(60)
        self.selected_time_range.grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        self.predict_button = tk.Button(
            master=left_frame,
            text="Predict values",
            command=self.calc_predicted_values,
            bg='#FFFF00'
        )
        self.predict_button.grid(row=row_index, column=0, padx=0, pady=7)

        row_index += 1

        tk.Label(left_frame, text="OpenGL predicted values:", relief=tk.RAISED) \
            .grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        self.output_opengl_predicted_values = tk.Text(left_frame, height=6,
                                                      width=30,
                                                      bg="white")

        self.output_opengl_predicted_values.grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        tk.Label(left_frame, text="DirectX 12 predicted values:", relief=tk.RAISED) \
            .grid(row=row_index, column=0, padx=5, pady=5)

        row_index += 1

        self.output_directx12_predicted_values = tk.Text(left_frame, height=6,
                                                         width=30,
                                                         bg="white")

        self.output_directx12_predicted_values.grid(row=row_index, column=0, padx=5, pady=5)

        self.window.mainloop()


gui = GPUGUI()
