from model_training import train_model
from model_testing import test_model

# train_model("AAPL", "model.pkl")

print("IBM: ", test_model("IBM", "model.pkl"))
print("APPLE: ", test_model("AAPL", "model.pkl"))
print("GOOGLE: ", test_model("GOOGL", "model.pkl"))
print("META: ", test_model("META", "model.pkl"))
