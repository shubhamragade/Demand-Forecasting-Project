This project predicts the future demand of meals at various fulfillment centers using historical data. Users can select a center and a meal from dropdowns and get a 7-day forecast of the number of orders.

The project includes:

End-to-end pipeline: Data preprocessing → Model → API → Modern Web UI

Backend: FastAPI

Frontend: Bootstrap 5 modern UI with dropdowns

Forecast logic: Simple statistical forecast (mean of historical orders)

Error-proof: Users can only select valid center_id and meal_id

Deployment-ready: Can be hosted on any server (Heroku, AWS, etc.)

Folder Structure
FoodDemandForecasting/
│
├── data/
│   ├── train.csv                 # Historical orders
│   ├── meal_info.csv             # Meal metadata
│   └── fulfilment_center_info.csv # Fulfillment center metadata
│
├── src/
│   ├── preprocess.py             # Data preprocessing functions (if needed)
│   └── forecast.py               # Forecast function and valid combos
│
├── app/
│   ├── templates/
│   │   └── index.html            # Modern UI template
│   └── main.py                   # FastAPI application
│
├── requirements.txt              # Python dependencies
└── README.md                     # This file

Dataset Details
train.csv – Historical Orders
Column	Description
id	Unique record ID
week	Week number
center_id	Fulfillment center ID
meal_id	Meal ID
checkout_price	Checkout price of meal
base_price	Base price of meal
emailer_for_promotion	Whether emailed for promotion (0/1)
homepage_featured	Whether featured on homepage (0/1)
num_orders	Number of orders (Target)
fulfilment_center_info.csv – Center Metadata
Column	Description
center_id	Fulfillment center ID
city_code	City code
region_code	Region code
center_type	Type of center
op_area	Operational area
meal_info.csv – Meal Metadata
Column	Description
meal_id	Meal ID
category	Meal category
cuisine	Meal cuisine
Setup Instructions
Clone the repo:
git clone <your-repo-url>
cd FoodDemandForecasting

Create virtual environment:
python -m venv venv
# Activate venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt


Ensure requirements.txt includes: fastapi, uvicorn, jinja2, pandas, python-multipart

Running the Application

Start the FastAPI server:

uvicorn app.main:app --reload


Open in browser:

http://127.0.0.1:8000/

Features in UI

Modern, clean design with Bootstrap

Dropdowns for Center ID and Meal ID (only valid combinations)

Enter forecast days (default: 7)

See forecast as a list of number of orders

Forecast Logic

Checks if (center_id, meal_id) exists in train.csv

Uses mean of historical num_orders as forecast

Returns list of num_orders for the requested number of days

Prevents errors for invalid inputs

Future Improvements

Replace mean-based forecast with ML models (Random Forest, XGBoost, LSTM) for better accuracy

Add charts to visualize forecast trends

Allow multi-center or multi-meal forecasts

Deploy on Heroku, AWS, or Streamlit for public access