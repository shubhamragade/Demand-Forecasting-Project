import pandas as pd

def load_data():
    # Load all datasets
    train = pd.read_csv("data/train.csv")
    test = pd.read_csv("data/test.csv")
    meal_info = pd.read_csv("data/meal_info.csv")
    center_info = pd.read_csv("data/fulfilment_center_info.csv")

    # Merge datasets
    train = train.merge(meal_info, on="meal_id", how="left")
    train = train.merge(center_info, on="center_id", how="left")

    test = test.merge(meal_info, on="meal_id", how="left")
    test = test.merge(center_info, on="center_id", how="left")

    return train, test
