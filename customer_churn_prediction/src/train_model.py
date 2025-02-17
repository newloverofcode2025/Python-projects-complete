import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(X_train_path, y_train_path):
    # Load the preprocessed data
    X_train = pd.read_csv(X_train_path)
    y_train = pd.read_csv(y_train_path)
    
    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())
    
    # Save the model (example: using joblib)
    import joblib
    joblib.dump(model, '../data/model.pkl')

if __name__ == "__main__":
    train_model('../data/X_train.csv', '../data/y_train.csv')