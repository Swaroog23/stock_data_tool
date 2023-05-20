from data_utils import get_data_set, prepare_feature, prepare_target
from prediction_model import PredictionModel
import numpy as np
from sklearn.metrics import mean_squared_error


def test_model(stock_symbol: str, model_file: str):
    training_data_set = get_data_set(stock_symbol)
    target = prepare_target(training_data_set)
    features = prepare_feature(training_data_set)

    model = PredictionModel(model_file)
    model.load()

    # Make predictions using the loaded model
    predicition = model.predict(features)

    # Calculate the root mean squared error (RMSE)
    rmse = np.sqrt(mean_squared_error(target, predicition))
    return f"Test Root Mean Squared Error: {rmse}"