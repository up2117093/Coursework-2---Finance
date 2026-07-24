import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def basic_clean(df):
    df = df.dropna()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

def train_test_split_time(df, test_size=0.2):
    split = int(len(df) * (1 - test_size))
    train = df.iloc[:split]
    test = df.iloc[split:]
    return train, test