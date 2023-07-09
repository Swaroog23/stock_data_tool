from data_utils import get_data_set, prepare_feature, prepare_target
from prediction_model import PredictionModel
from sklearn.model_selection import train_test_split


def train_model(stock_symbol: str, model_file: str):
    training_data_set = get_data_set(stock_symbol)
    target = prepare_target(training_data_set)
    features = prepare_feature(training_data_set)
    X_train, _, y_train, _ = train_test_split(features, target, test_size=0.2, random_state=42)

    # Create a Linear Regression model and fit it to the training data
    model = PredictionModel(model_file)
    model.train(features=X_train, target=y_train)
