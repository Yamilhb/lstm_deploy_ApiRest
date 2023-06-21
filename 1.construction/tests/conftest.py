import pytest
import pandas as pd
from pathlib import Path

from lstm_model.config.core import DATASET_DIR, config


@pytest.fixture()
def sample_input_data():
    return pd.read_csv(Path(f"{DATASET_DIR}/{config.app_config.data_file}"), usecols = config.model_config.features)