import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from loguru import logger
from lstm_model import __version__ as model_version
from lstm_model.predict import make_prediction

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()

@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
async def predict(input_data: schemas.PredictionInputs) -> Any:
#    logger.info(f"\n\n\nPRRRRRRRUEBASSS\n\n\n")
    """
    Make predictions qith your packaged model.\n
    CUIDADO: Ahora input_data no es diccionario, es de tipo schemas.PredictionInputs ->
    -> Sería un error hacer input_data["inputs"]
    """

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    # Advanced: You can improve performance of your API by rewriting the
    # `make prediction` function to be async and using await here.
    logger.info(f"Making prediction on inputs: {input_data.inputs[:3]}")

    aux = input_df.copy()
    
    aux.columns = [x.replace('_',' ') for x in aux.columns]
    
    results = make_prediction(input_data=aux.replace({np.nan: None}))

# I'll have to write the errors to make a more robust product.
#    if results["errors"] is not None:
#        logger.warning(f"Prediction validation error: {results.get('errors')}")
#        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')[:3]}")
    
    
    return results