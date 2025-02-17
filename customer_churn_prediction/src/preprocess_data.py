import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Handle missing values (example: fill with mean)
    df.fillna(df.mean(), inplace=True)
    
    # Encode categorical variables (example: one-hot encoding)
    df = pd.get_dummies(df, columns=['gender', 'contract', 'payment_method'])
    
    # Split the data into features and target
    X = df.drop('churn', axis=1)
    y = df['churn']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = preprocess_data('../data/churn_data.csv')
    pd.DataFrame(X_train).to_csv('../data/X_train.csv', index=False)
    pd.DataFrame(X_test).to_csv('../data/X_test.csv', index=False)
    pd.DataFrame(y_train).to_csv('../data/y_train.csv', index=False)
    pd.DataFrame(y_test).to_csv('../data/y_test.csv', index=False)