import array

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

"""
GraphicsAPIBenchmark is a class for collecting data/ measurements from opengl and directx 12 files (.csv) .
"""


class GraphicsAPIBenchmark:

    def __init__(self, path_to_opengl_results: str = "opengl_results.csv",
                 path_to_directx12_results: str = "directx12_results.csv"):
        """
        Reading measurements from files and training linear regression models for this.
        :param path_to_opengl_results: Path to opengl results file (.csv).
        :param path_to_directx12_results: Path to DirectX 12 results file (.csv).
        """
        # 1. Reading data from opengl measurements to data frame.
        self.opengl_results_data_frame = pd.read_csv(f"{path_to_opengl_results}")
        self.time_opengl_results = self.opengl_results_data_frame["time"].values
        self.fps_opengl_results = self.opengl_results_data_frame["fps"].values

        # 2. Training model for prediction opengl FPS.
        self.opengl_model = LinearRegression()
        self.opengl_model.fit(X=self.time_opengl_results.reshape(-1, 1),  # X - Training data.
                              y=self.fps_opengl_results)  # y - Target values.

        self.opengl_intercept = round(float(self.opengl_model.intercept_), 2)
        self.opengl_coefficient = round(float(self.opengl_model.coef_), 2)
        # FPS(time) = self.opengl_coefficient * time + self.opengl_intercept.

        # 3. Reading data from DirectX 12 measurements to data frame.
        self.directx12_results_data_frame = pd.read_csv(f"{path_to_directx12_results}")
        self.time_directx12_results = self.directx12_results_data_frame["time"].values
        self.fps_directx12_results = self.directx12_results_data_frame["fps"].values

        # 4. Training model for prediction DirectX 12 FPS.
        self.directx12_model = LinearRegression()
        self.directx12_model.fit(X=self.time_directx12_results.reshape(-1, 1),  # X - Training data.
                                 y=self.fps_directx12_results)  # y - target values.

        self.directx12_intercept = round(float(self.directx12_model.intercept_), 2)
        self.directx12_coefficient = round(float(self.directx12_model.coef_), 2)
        # FPS(time) = self.directx12_coefficient * time + self.directx12_intercept

    def get_opengl_trend_line_formula(self) -> str:
        """
        Getting the OpenGL trend line formula like: f(x) = ax + b
        """
        return f"FPS(time) = {self.opengl_coefficient}*time + {self.opengl_intercept}"

    def get_directx12_trend_line_formula(self) -> str:
        """
        Getting the DirectX 12 trend line formula like: f(x) = ax + b
        """
        return f"FPS(time) = {self.directx12_coefficient}*time + {self.directx12_intercept}"

    def draw_opengl_scatter_chart_with_trend_line(self) -> None:
        """
        Drawing chart with OpenGL results (scatter) and trend line.
        """
        predicted_fps_values = self.opengl_model.predict(self.time_opengl_results.reshape(-1, 1))
        plt.plot(self.time_opengl_results, predicted_fps_values, color='red', label=f"{self.get_opengl_trend_line_formula()}")
        plt.scatter(self.time_opengl_results, self.fps_opengl_results, color='blue')
        plt.grid(True)
        plt.xlabel("Time [s]")
        plt.ylabel("Frame rate [-]")
        plt.legend()
        plt.title("OpenGL ~ Frame rate per second ~ FPS(Time)")
        plt.savefig("OpenGL_Scatter_Chart_With_Trend_Line.png")
        plt.show()

    def draw_directx12_scatter_chart_with_trend_line(self) -> None:
        """
        Drawing chart with DirectX 12 results (scatter) and trend line.
        """
        predicted_fps_values = self.directx12_model.predict(self.time_directx12_results.reshape(-1, 1))
        plt.plot(self.time_directx12_results, predicted_fps_values, color='red', label=f"{self.get_directx12_trend_line_formula()}")
        plt.scatter(self.time_directx12_results, self.fps_directx12_results, color='green')
        plt.grid(True)
        plt.xlabel("Time [s]")
        plt.ylabel("Frame rate [-]")
        plt.legend()
        plt.title("DirectX 12 ~ Frame rate per second ~ FPS(Time)")
        plt.savefig("DirectX12_Scatter_Chart_With_Trend_Line.png")
        plt.show()

    def draw_opengl_plot_chart_with_trend_line(self) -> None:
        """
        Drawing chart with OpenGL results (plot) and trend line.
        """
        predicted_fps_values = self.opengl_model.predict(self.time_opengl_results.reshape(-1, 1))
        plt.plot(self.time_opengl_results, predicted_fps_values, color='red', label=f"{self.get_opengl_trend_line_formula()}")
        plt.plot(self.time_opengl_results, self.fps_opengl_results, color='blue')
        plt.legend()
        plt.grid(True)
        plt.xlabel("Time [s]")
        plt.ylabel("Frame rate [-]")
        plt.title("OpenGL ~ Frame rate per second ~ FPS(Time)")
        plt.savefig("OpenGL_Plot_Chart_With_Trend_Line.png")
        plt.show()

    def draw_directx12_plot_chart_with_trend_line(self):
        """
        Drawing chart with DirectX 12 results (plot) and trend line.
        """
        predicted_fps_values = self.directx12_model.predict(self.time_directx12_results.reshape(-1, 1))
        plt.plot(self.time_directx12_results, predicted_fps_values, color='red', label=f"{self.get_directx12_trend_line_formula()}")
        plt.plot(self.time_directx12_results, self.fps_directx12_results, color='green')
        plt.grid(True)
        plt.xlabel("Time [s]")
        plt.ylabel("Frame rate [-]")
        plt.legend()
        plt.title("DirectX 12 ~ Frame rate per second ~ FPS(Time)")
        plt.savefig("DirectX12_Plot_Chart_With_Trend_Line.png")
        plt.show()

    def predict_opengl(self, values: array) -> list:
        """
        Predicting opengl values.
        :param values: Buffer with results.
        :return: List with predicted values.
        """
        return self.opengl_model.predict(values.reshape(-1, 1))

    def predict_directx12(self, values: array) -> list:
        """
        Predicting DirectX 12 values.
        :param values: Buffer with results.
        :return: List with predicted values.
        """
        return self.directx12_model.predict(values.reshape(-1, 1))

if __name__ == "__main__":
    # Testing.
    gapi = GraphicsAPIBenchmark(path_to_opengl_results="opengl_results.csv",
                                path_to_directx12_results="directx12_results.csv")
    print(f"OpenGL trend line formula: {gapi.get_opengl_trend_line_formula()}")
    print(f"DirectX 12 trend line formula: {gapi.get_directx12_trend_line_formula()}")
    gapi.draw_opengl_plot_chart_with_trend_line()
    gapi.draw_opengl_scatter_chart_with_trend_line()
    gapi.draw_directx12_plot_chart_with_trend_line()
    gapi.draw_directx12_scatter_chart_with_trend_line()
