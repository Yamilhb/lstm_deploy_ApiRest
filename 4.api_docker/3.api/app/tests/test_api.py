'''import math

import numpy as np
import pandas as pd
from lstm_model.config.core import config
from lstm_model.predict import make_prediction


def test_make_prediction(test_data):

    expected_no_predictions = 69030

    print('EEESO: ',test_data)
    result = make_prediction(input_data=test_data)

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list), "Las predicciones deberíar estar en una lista."
    print(type(predictions[0]))
    assert isinstance(predictions[0], np.float32), "Las predicciones deberían ser de tipo float."
    #assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions, f"Las predicciones deben tenr una longitud de {expected_no_predictions}"
    #assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)
'''
    
import math

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

from fastapi.encoders import jsonable_encoder
from lstm_model.predict import make_prediction

from loguru import logger


def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    assert isinstance(test_data, pd.DataFrame), "The test_data should be a pd.DataFrame"

    test_data.columns = [x.replace(' ','_') for x in test_data.columns]
#    assert math.sum([' ' in x for x in test_data.columns])==0, "The names of the columns don't have to have blank spaces."




    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    print('\nESTRUCTURA INPUT:\nCLAVE:', payload.keys(),'VALORES:',payload['inputs'][:3])


    input_df = pd.DataFrame(jsonable_encoder(payload["inputs"]))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {payload['inputs'][:3]}")

    aux = input_df.copy()

    aux.columns = [x.replace('_',' ') for x in aux.columns]

    results = make_prediction(input_data=aux.replace({np.nan: None}))


    print('\nESTRUCTURA salida:\nCLAVE: ', results.keys(),'VALORES:', results['predictions'][:3],results['version'][:3])




    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    print('ESSO: ',response,'------',response.status_code)

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
#    assert prediction_data["errors"] is None No tengo definido errores en la predicción de momento.
#    assert math.isclose(prediction_data["predictions"][0], 113422, rel_tol=100) Puedo comprobar valores concretos, o contrastar con tabla de valores conocidos.
