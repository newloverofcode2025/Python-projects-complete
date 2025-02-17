import pandas as pd
import joblib
from sklearn.metrics import classification_report

def evaluate_model(X_test_path, y_test_path, model_path):
    # Load the preprocessed data and model
    X_test = pd.read_csv(X_test_path)
    y_test = pd.read_csv(y_test_path)
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model('../data/X_test.csv', '../data/y_test.csv', '../data/model.pkl')