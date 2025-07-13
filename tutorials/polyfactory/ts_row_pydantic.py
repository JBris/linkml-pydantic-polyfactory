from pydantic import BaseModel
from datetime import datetime

class TimeSeriesPoint(BaseModel):
    timestamp: datetime
    value: float

import numpy as np
from datetime import datetime, timedelta
from polyfactory.factories.pydantic_factory import ModelFactory
from typing import List

class TimeSeriesFactory(ModelFactory[TimeSeriesPoint]):
    __model__ = TimeSeriesPoint

    @classmethod
    def generate_series(cls, n: int = 100, alpha: float = 0.8, noise_std: float = 1.0, start_time: datetime = None, freq: timedelta = None) -> List[TimeSeriesPoint]:
        start_time = start_time or datetime.now()
        freq = freq or timedelta(hours=1)

        values = [np.random.randn()]
        for _ in range(1, n):
            values.append(alpha * values[-1] + np.random.normal(0, noise_std))

        timestamps = [start_time + i * freq for i in range(n)]

        return [cls.build(timestamp=timestamps[i], value=values[i]) for i in range(n)]

series = TimeSeriesFactory.generate_series(n=10)
for point in series:
    print(point)
