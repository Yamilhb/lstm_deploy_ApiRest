from typing import Generator

import pandas as pd
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from lstm_model.config.core import config, DATASET_DIR
#from lstm_model.processing.pipe_needs import ReestructuraLSM

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    return pd.read_csv(Path(f"{DATASET_DIR}/{config.app_config.data_file}"), usecols = config.model_config.features)#.iloc[:10,:]

#    transformer = ReestructuraLSM(config.model_config.ventana)

      # Basic transformations.
#    features = config.model_config.features
#    sample_input_data['fecha'] = pd.to_datetime(sample_input_data[features[0]],format='%d.%m.%Y %H:%M:%S.%f')
#    sample_input_data[f'precio_EURUSD'] = sample_input_data[features[1]]

      # NULOS
      # For the null values we will take the preceed value.
#    sample_input_data['precio_EURUSD'] = sample_input_data['precio_EURUSD'].fillna(method='ffill')
      # Except when we do not have a preceed value, then we will take the next value.
#    sample_input_data['precio_EURUSD'] = sample_input_data['precio_EURUSD'].fillna(method='bfill')

      # Select columns.
#    sample_input_data = sample_input_data[['fecha','precio_EURUSD']]
#    sample_input_data.set_index('fecha',inplace=True)

#    subject = transformer.transform(sample_input_data.values)

#    return subject


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}