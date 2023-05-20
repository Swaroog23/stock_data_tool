from sklearn.linear_model import LinearRegression
import joblib


class PredictionModel:
    def __init__(self, model_file) -> None:
        self.model_file = model_file
        self.model = None

    def save(self):
        joblib.dump(self.model, self.model_file)

    def load(self):
        self.model = joblib.load(filename=self.model_file)

    def train(self, features, target):
        self.model = LinearRegression()
        self.model.fit(features, target)
        self.save()

    def predict(self, input_features):
        return self.model.predict(input_features)