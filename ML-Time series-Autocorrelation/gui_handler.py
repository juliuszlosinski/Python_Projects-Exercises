import tkinter as tk
from tkinter import ttk
import time_series_handler as tsh

"""
GPUGUI is used for creating GUI for handling user input (showing charts, prediction).
"""


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

    def calc_predicted_values(self) -> None:
        """
        Calculating predicted values.
        """
        if self.checkbox_opengl_value.get():
            opengl_values = list(range(0, int(self.selected_time_range.get())))
            predicted_opengl_values = self.opengl_time_series_analyzer.predict_values(0, len(opengl_values))
            print(predicted_opengl_values)
            self.output_opengl_predicted_values.delete(1.0, tk.END)
            self.output_opengl_predicted_values.insert(tk.END, predicted_opengl_values)
        if self.checkbox_directX_value.get():
            directX12_values = list(range(0, int(self.selected_time_range.get())))
            predicted_directX12_values = self.directx12_time_series_analyzer.predict_values(0, len(directX12_values))
            print(predicted_directX12_values)
            self.output_directx12_predicted_values.delete(1.0, tk.END)
            self.output_directx12_predicted_values.insert(tk.END, predicted_directX12_values)

    def show_plots(self) -> None:
        """
        Showing selected plots.
        """
        if self.show_default_fps_plot.get() and self.checkbox_directX_value.get():
            self.directx12_time_series_analyzer.draw_default_fps_plot()
        if self.show_differential_fps_plot.get() and self.checkbox_directX_value.get():
            self.directx12_time_series_analyzer.draw_differential_fps_plot()
        if self.show_decomposed_plots.get() and self.checkbox_directX_value.get():
            self.directx12_time_series_analyzer.draw_decomposed_plots()
        if self.show_predicted_values_plot.get() and self.checkbox_directX_value.get():
            self.directx12_time_series_analyzer.draw_predicted_values_plot()

        if self.show_default_fps_plot.get() and self.checkbox_opengl_value.get():
            self.opengl_time_series_analyzer.draw_default_fps_plot()
        if self.show_differential_fps_plot.get() and self.checkbox_opengl_value.get():
            self.opengl_time_series_analyzer.draw_differential_fps_plot()
        if self.show_decomposed_plots.get() and self.checkbox_opengl_value.get():
            self.opengl_time_series_analyzer.draw_decomposed_plots()
        if self.show_predicted_values_plot.get() and self.checkbox_opengl_value.get():
            self.opengl_time_series_analyzer.draw_predicted_values_plot()

    def __init__(self):
        """
        Creating and initializing context of the window.
        """
        self.directx12_time_series_analyzer = tsh.TimeSeriesHandler(
            name="DirectX12",
            path_to_results="directx12_results.csv",
            number_of_lags=10,
            number_of_periods=4
        )
        self.opengl_time_series_analyzer = tsh.TimeSeriesHandler(
            name="OpenGL",
            path_to_results="opengl_results.csv",
            number_of_lags=10,
            number_of_periods=4
        )

        self.window = tk.Tk()
        icon = tk.PhotoImage(file='icon.png')
        background_image = tk.PhotoImage(file='background.png')

        self.window.iconphoto(False, icon)
        self.window.title("GPU FPS Analyzer")
        self.window.geometry("300x680")
        self.window.resizable(False, False)

        background = tk.Label(self.window, image=background_image)
        background.place(x=0, y=0)
        left_frame = tk.Frame(master=self.window, width=300, height=680, bg='', bd=5)
        left_frame.grid(row=0, column=0, padx=1, pady=1)
        left_frame.grid_propagate(False)
        left_frame.grid_columnconfigure(0, weight=1)

        row_index = 0

        tk.Label(left_frame, text="Select graphics API:", relief=tk.RAISED).grid(row=row_index, column=0, padx=5,
                                                                                 pady=5)
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

        tk.Label(left_frame, text="Select plots:", relief=tk.RAISED).grid(row=row_index, column=0, padx=5, pady=5)
        row_index += 1

        self.show_default_fps_plot = tk.IntVar()
        self.checkbox_show_default_fps_plot = tk.Checkbutton(
            left_frame,
            text="Default FPS plot",
            variable=self.show_default_fps_plot,
            onvalue=1,
            offvalue=0
        )
        self.checkbox_show_default_fps_plot.select()
        self.checkbox_show_default_fps_plot.grid(row=row_index, column=0, padx=5, pady=5)
        row_index += 1

        self.show_differential_fps_plot = tk.IntVar()
        self.checkbox_show_differential_fps_plot = tk.Checkbutton(
            left_frame,
            text="Differential FPS plot",
            variable=self.show_differential_fps_plot,
            onvalue=1,
            offvalue=0
        )
        self.checkbox_show_differential_fps_plot.select()
        self.checkbox_show_differential_fps_plot.grid(row=row_index, column=0, padx=5, pady=5)
        row_index += 1

        self.show_decomposed_plots = tk.IntVar()
        self.checkbox_show_decomposed_plots = tk.Checkbutton(
            left_frame,
            text="Decomposed FPS plots",
            variable=self.show_decomposed_plots,
            onvalue=1,
            offvalue=0
        )
        self.checkbox_show_decomposed_plots.select()
        self.checkbox_show_decomposed_plots.grid(row=row_index, column=0, padx=5, pady=5)
        row_index += 1

        self.show_predicted_values_plot = tk.IntVar()
        self.checkbox_show_predicted_values_plot = tk.Checkbutton(
            left_frame,
            text="Predicted FPS plot",
            variable=self.show_predicted_values_plot,
            onvalue=1,
            offvalue=0
        )
        self.checkbox_show_predicted_values_plot.select()
        self.checkbox_show_predicted_values_plot.grid(row=row_index, column=0, padx=5, pady=5)
        row_index += 1

        self.button_show_plots = tk.Button(
            master=left_frame,
            text="Show FPS plots",
            command=self.show_plots,
            bg='#FFFF00'
        )
        self.button_show_plots.grid(row=row_index, column=0, padx=0, pady=7)
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


if __name__ == "__main__":
    gpu_gui = GPUGUI()
