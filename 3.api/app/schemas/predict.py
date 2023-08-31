from typing import Any, List, Optional

from pydantic import BaseModel


class PredictionResults(BaseModel):
#    errors: Optional[Any]
    predictions: Optional[List[float]]
    version: str


class InputData(BaseModel):
    Gmt_time: str
    Close: float

class PredictionInputs(BaseModel):
    inputs: List[InputData]