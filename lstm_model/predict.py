import typing as t

import numpy as np
import pandas as pd

from lstm_model import __version__ as _version
from lstm_model.config.core import config
from lstm_model.processing.data_manager import load_pipeline

pipeline_file_name = f"{config.app_config.pipeline_save_file}{_version}.pkl"
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(
    *,
    input_data: pd.DataFrame,
) -> dict:
    """Make a prediction using a saved model pipeline."""

    data = pd.DataFrame(input_data)
    results = {"predictions": None, "version": _version}

    predictions = _price_pipe.predict(
        X=validated_data[config.model_config.features]
        )
    results = {
        "predictions": [np.exp(pred) for pred in predictions],  # type: ignore
        "version": _version
        }

    return results