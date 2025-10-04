import pandas as pd

# Load train data
train = pd.read_csv("data/train.csv")

# Group all valid (center_id, meal_id) combos
valid_combos = train.groupby(['center_id','meal_id']).size().reset_index()[['center_id','meal_id']]

def forecast(center_id, meal_id, periods=7):
    center_id = int(center_id)
    meal_id = int(meal_id)

    # Check if combo exists
    if not ((valid_combos['center_id'] == center_id) & (valid_combos['meal_id'] == meal_id)).any():
        return f"No data for center {center_id} and meal {meal_id}"

    # Get historical orders
    data = train[(train['center_id'] == center_id) & (train['meal_id'] == meal_id)]
    
    # Simple forecast: mean of last week num_orders
    if data.empty:
        return f"No data for center {center_id} and meal {meal_id}"

    mean_orders = int(data['num_orders'].mean())
    forecast_list = [mean_orders for _ in range(periods)]
    
    return forecast_list
