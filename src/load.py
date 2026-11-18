import pandas as pd
def load_raw(path):
    df = pd.read_csv(path)
    return df

