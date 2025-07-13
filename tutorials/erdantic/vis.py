import erdantic as erd
from typing import Literal, List
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum, auto

class DataSource(Enum):
    SENSOR = auto()
    DATABASE = auto()
    MANUAL = auto()

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

class TimeSeriesMetadata(BaseModel):
    programme_code: Literal["ee"] = Field(default="ee", frozen=True)
    programme_full_name: Literal["Edantic Example"] = Field(default="Edantic Example", frozen=True)
    programme_machine_name: Literal["edantic_example"] = Field(default="edantic_example", frozen=True)
    data_source_name: str
    data_source_type: DataSource

class TimeSeries(BaseModel):
    points: List[TimeSeriesPoint]
    metadata: TimeSeriesMetadata

diagram = erd.create(TimeSeries)

diagram.draw("diagram.png")