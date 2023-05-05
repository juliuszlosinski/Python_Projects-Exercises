import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
import decimal

"""
TimeSeriesHandler is a class used to analyzing time series for FPS benchmark (DirectX 12 and OpenGL).
"""


class TimeSeriesHandler:
    def __init__(self, name="Default", fps_data: list = [],
                 time_data: list = [],
                 number_of_lags: int = 10,
                 number_of_periods: int = 1):
        """
        Reading and formatting data for future displaying.
        """
        # 1. Reading data from source file.
        self.results_data_frame = pd.DataFrame({
            "time": time_data,
            "fps": fps_data
        })
        self.time = self.results_data_frame["time"].values
        self.fps = self.results_data_frame["fps"].values
        self.fps_diff = self.results_data_frame["fps"].diff().values
        self.name = name

        # 2. Getting auto correlation.
        self.number_of_lags = number_of_lags
        self.auto_correlation = sm.tsa.acf(self.fps, nlags=self.number_of_lags)

        # 3. Decomposing.
        self.period = number_of_periods
        self.decomposed_fps = sm.tsa.seasonal_decompose(self.fps, model="multiplicable", period=self.period)
        self.fps_trend = list(self.decomposed_fps.trend)
        self.fps_seasonal = list(self.decomposed_fps.seasonal)
        self.fps_observed = list(self.decomposed_fps.observed)
        self.fps_residual = list(self.decomposed_fps.resid)

        # 4. Learning AI model.
        arima_model = ARIMA(self.fps, order=(1, 2, 2))
        self.arima_model = arima_model.fit()

    def __init__(self,name="DirectX12", path_to_results: str = "directx12_results.csv",
                 number_of_lags: int = 10,
                 number_of_periods: int = 1):
        """
        Reading and formatting data for future displaying.
        """
        # 1. Reading data from source file.
        self.results_data_frame = pd.read_csv(f"{path_to_results}")
        self.time = self.results_data_frame["time"].values
        self.fps = self.results_data_frame["fps"].values
        self.fps_diff = self.results_data_frame["fps"].diff().values
        self.name = name

        # 2. Getting auto correlation.
        self.number_of_lags = number_of_lags
        self.auto_correlation = sm.tsa.acf(self.fps, nlags=self.number_of_lags)

        # 3. Decomposing.
        self.period = number_of_periods
        self.decomposed_fps = sm.tsa.seasonal_decompose(self.fps, model="multiplicable", period=self.period)
        self.fps_trend = list(self.decomposed_fps.trend)
        self.fps_seasonal = list(self.decomposed_fps.seasonal)
        self.fps_observed = list(self.decomposed_fps.observed)
        self.fps_residual = list(self.decomposed_fps.resid)

        # 4. Learning AI model.
        arima_model = ARIMA(self.fps, order=(1, 2, 2))
        self.arima_model = arima_model.fit()

    def predict_values(self, start: int = 0, end: int = 100) -> list:
        """
        Predicting values.
        :param start: Starting number/ range ~ Left bound.
        :param end: Final number/ range ~ Right bound.
        :return:
        """
        original_data = self.arima_model.predict(start, end)
        formatted_data = []
        for i in original_data:
            formatted_data.append(round(i, 2))
        return formatted_data

    def draw_predicted_values_plot(self) -> None:
        """
        Drawing predicted values plot.
        """
        predicted_values = self.predict_values(start=0, end=len(self.time) - 1)
        plt.plot(self.time, predicted_values, color="blue", marker="o", label="Predicted FPS")
        plt.plot(self.time, self.fps, color="black", marker="x", label="Real FPS values")
        plt.title(f"{self.name} - Predicted and Real FPS values (time)")
        plt.xlabel("Time [s]")
        plt.ylabel("FPS [-]")
        plt.grid(True)
        plt.legend()
        plt.savefig(f"{self.name} - Predicted and Real FPS values (time).png")
        plt.show()

    def draw_decomposed_trend_plot(self) -> None:
        """
        Drawing decomposed trend plot.
        """
        plt.plot(self.time, self.fps_trend, color="green", marker="o")
        plt.title(f"{self.name} - FPS trend (time) for period = {self.period}")
        plt.ylabel("FPS trend [-]")
        plt.xlabel("Time [s]")
        plt.grid(True)
        plt.savefig(f"{self.name} - FPS trend (time) for period = {self.period}.png")
        plt.show()

    def draw_decomposed_seasonal_plot(self) -> None:
        """
        Drawing decomposed seasonal plot.
        """
        plt.plot(self.time, self.fps_seasonal, color="blue", marker="o")
        plt.title(f"{self.name} - FPS seasonal (time) for period = {self.period}")
        plt.ylabel("FPS seasonal [-]")
        plt.xlabel("Time [s]")
        plt.grid(True)
        plt.savefig(f"{self.name} - FPS seasonal (time) for period = {self.period}.png")
        plt.show()

    def draw_decomposed_observed_plot(self) -> None:
        """
        Drawing decomposed observed plot.
        """
        plt.plot(self.time, self.fps_observed, color="black", marker="o")
        plt.title(f"{self.name} - FPS observed (time) for period = {self.period}")
        plt.ylabel("FPS observed [-]")
        plt.xlabel("Time [s]")
        plt.grid(True)
        plt.savefig(f"{self.name} - FPS observed (time) for period = {self.period}.png")
        plt.show()

    def draw_decomposed_residual_plot(self) -> None:
        """
        Drawing decomposed residual plot.
        """
        plt.plot(self.time, self.fps_residual, color="orange", marker="o")
        plt.title(f"{self.name} - FPS residual (time) for period = {self.period}")
        plt.ylabel("FPS residual [-]")
        plt.xlabel("Time [s]")
        plt.grid(True)
        plt.savefig(f"{self.name} - FPS residual (time) for period = {self.period}.png")
        plt.show()

    def draw_decomposed_plots(self) -> None:
        """
        Drawing decomposed plots:
        - trend,
        - seasonal,
        - observed,
        - residual,
        """

        self.draw_decomposed_trend_plot()
        self.draw_decomposed_seasonal_plot()
        self.draw_decomposed_observed_plot()
        self.draw_decomposed_residual_plot()

        plt.plot(self.time, self.fps_trend, color="green", marker="o", label="FPS trend")
        plt.plot(self.time, self.fps_observed, color="black", marker="o", label="FPS observed")
        plt.title(f"{self.name} - FPS (time)")
        plt.xlabel("Time [s]")
        plt.ylabel("FPS [-]")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{self.name} - FPS (time).png")
        plt.show()

    def draw_differential_fps_plot(self) -> None:
        """
        Drawing differential FPS plot.
        """
        plt.plot(self.time, self.fps_diff, color="red", marker="o")
        plt.title(f"{self.name} - Differentiation - FPS (time)")
        plt.xlabel("Time [s]")
        plt.ylabel("FPS [-]")
        plt.grid(True)
        plt.savefig(f"{self.name} - Differentiation - FPS (time).png")
        plt.show()

    def draw_default_fps_plot(self) -> None:
        """
        Drawing default FPS plot.
        """
        plt.plot(self.time, self.fps, color="red", marker="o")
        plt.title(f"{self.name} - FPS (time)")
        plt.xlabel("Time [s]")
        plt.ylabel("FPS [-]")
        plt.grid(True)
        plt.savefig(f"{self.name} - FPS (time).png")
        plt.show()

    def print_data(self) -> None:
        """
        Printing all readed and formatted data.
        """
        print(f"Time: \n{self.time}")
        print(f"FPS: \n{self.fps}")
        print(f"FPS differentiation: \n{self.fps_diff}")


if __name__ == "__main__":
    # Testing.
    time_series_handler = TimeSeriesHandler(
        name="DirectX12",
        path_to_results="directx12_results.csv",
        number_of_lags=10,
        number_of_periods=4
    )
    time_series_handler.print_data()
    time_series_handler.draw_default_fps_plot()
    time_series_handler.draw_differential_fps_plot()
    time_series_handler.draw_decomposed_plots()
    time_series_handler.draw_predicted_values_plot()
