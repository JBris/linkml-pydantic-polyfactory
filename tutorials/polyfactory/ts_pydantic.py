from pydantic import BaseModel
from typing import List
from polyfactory.factories.pydantic_factory import ModelFactory
import numpy as np

class TimeSeries(BaseModel):
    timestamps: List[str]
    values: List[float]


def generate_seasonal_autocorrelated_series(
    n: int = 100,
    alpha: float = 0.8,
    noise_std: float = 1.0,
    season_amplitude: float = 5.0,
    season_period: int = 20,
) -> np.ndarray:
    values = [np.random.randn()]
    for t in range(1, n):
        seasonal_component = season_amplitude * np.sin(2 * np.pi * t / season_period)
        ar_component = alpha * values[-1]
        noise = np.random.normal(0, noise_std)
        values.append(seasonal_component + ar_component + noise)
    return np.array(values)

def generate_autocorrelated_series(n: int = 100, alpha: float = 0.8, noise_std: float = 1.0):
    values = [np.random.randn()]
    for _ in range(1, n):
        next_val = alpha * values[-1] + np.random.normal(0, noise_std)
        values.append(next_val)
    return values

class TimeSeriesFactory(ModelFactory[TimeSeries]):
    __model__ = TimeSeries

    @classmethod
    def timestamps(cls) -> str:
        return [f"2025-01-01T00:{i:02}:00Z" for i in range(100)]
    
    @classmethod
    def values(cls) -> str:
        return generate_seasonal_autocorrelated_series()
    
ts = TimeSeriesFactory.build()
print(ts)

ts_batch = [
    TimeSeriesFactory.build()
    for _ in range(5)
]
print(ts_batch)