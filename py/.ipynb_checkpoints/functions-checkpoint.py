import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def basic_clean(df):
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

def train_test_split_time(X, y, test_size=0.2):
    split = int(len(X) * (1 - test_size))
    X_train = X.iloc[:split]
    X_test = X.iloc[split:]
    y_train = y.iloc[:split]
    y_test = y.iloc[split:]
    return X_train, X_test, y_train, y_test
