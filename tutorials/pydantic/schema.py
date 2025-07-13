from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class TimeSeriesPoint(BaseModel):
    timestamp: datetime = Field(
        description="The timestamp"
    )
    value: float = Field(
        description="The time series value",
        unit="cm",
        ge=0
    )
    
    source: Literal["sensor-A"] = Field(default="sensor-A", frozen=True)
    unit: Literal["Celsius"] = Field(default="Celsius", frozen=True)
    num: Literal[1] = Field(default=1, frozen=True)

point = TimeSeriesPoint(timestamp=datetime.now(), value=42.0)
print(point.model_dump())
print(point.model_json_schema())
