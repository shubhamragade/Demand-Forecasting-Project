# 🚀 FoodDemandForecasting

**Predict future meal demand at fulfillment centers — simple, deployable, and user-friendly.**

> A lightweight end-to-end project that uses historical orders to forecast short-term meal demand. Ideal for demos, prototypes, or as a starting point for ML-powered forecasting. ✅

---

## 📦 Highlights

* **End-to-end pipeline**: Data preprocessing → Forecast logic → FastAPI API → Modern web UI.
* **Backend**: FastAPI + Uvicorn for fast, production-ready APIs.
* **Frontend**: Bootstrap 5 modern UI — clean, responsive, and simple dropdown-driven interactions.
* **Forecast logic**: Quick statistical baseline — mean of historical orders (perfect for baseline comparisons). 📈
* **Error-proof UX**: Dropdowns only show valid `(center_id, meal_id)` combinations to avoid invalid requests. 🔒
* **Deployment-ready**: Can be hosted on Heroku / AWS / any server. 🌐

---

## 📁 Project Structure

```
FoodDemandForecasting/
│
├── data/
│   ├── train.csv
│   ├── meal_info.csv
│   └── fulfilment_center_info.csv
│
├── src/
│   ├── preprocess.py
│   └── forecast.py
│
├── app/
│   ├── templates/
│   │   └── index.html
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## 🗂️ Dataset Details

* **train.csv** — historical orders

  * `id, week, center_id, meal_id, checkout_price, base_price, emailer_for_promotion, homepage_featured, num_orders`
* **fulfilment_center_info.csv** — center metadata

  * `center_id, city_code, region_code, center_type, op_area`
* **meal_info.csv** — meal metadata

  * `meal_id, category, cuisine`

---

## ⚙️ Setup Instructions

1. Clone the repo:

```bash
git clone <your-repo-url>
cd FoodDemandForecasting
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Ensure `requirements.txt` contains: `fastapi`, `uvicorn`, `jinja2`, `pandas`, `python-multipart`.

---

## ▶️ Run the Application (Local)

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open UI in your browser:

```
http://127.0.0.1:8000/
```

---

## 🖥️ Features (UI)

* Modern, clean Bootstrap 5 design. ✨
* Dropdowns for **Center ID** and **Meal ID** (only valid pairs shown).
* Input for number of forecast days (default **7**).
* Forecast returned as a simple list of predicted daily orders.
* Quick client-side validation to prevent invalid combos. ✅

---

## 🔮 Forecast Logic

* The app checks whether the chosen `(center_id, meal_id)` exists in `train.csv`.
* If valid, forecast = **mean of historical `num_orders`** for that pair.
* The API returns a list with the predicted number of orders for each requested day.

This baseline is intentionally simple — it’s fast, interpretable, and useful as a performance baseline before adding ML models (e.g., Random Forest, XGBoost, LSTM). 🧠

---

## 🧪 Example API

**Endpoint (UI uses this):** `POST /forecast`

**Request JSON**:

```json
{
  "center_id": 1,
  "meal_id": 10,
  "days": 7
}
```

**Response JSON**:

```json
{ "forecast": [23, 23, 23, 23, 23, 23, 23], "mean": 23 }
```

> (Numbers above are illustrative — real output depends on `train.csv`.)

---

## 📈 Future Improvements (Ideas)

* Replace mean-based forecast with ML models: **Random Forest**, **XGBoost**, or **LSTM** for time-series trend capture. ⚡
* Add interactive charts (Plotly or Chart.js) to visualize forecasts & historical trends. 🖼️
* Support multi-center / multi-meal forecasts and batched predictions. 🔁
* Add CI/CD + Dockerfile for full production deployment. 🐳
* Add logging, monitoring, and evaluation metrics (MAE, RMSE). 🧾

---

## 🧰 Tips & Notes

* Keep your `train.csv` up-to-date to improve forecast relevance.
* This project is a great starting point for A/B testing forecasting models: compare the mean baseline vs ML models. ⚖️

---

## 📌 License

MIT License — feel free to reuse and extend. ❤️

---

If you want, I can:

* Add attractive badges (build, license, python version). 🏷️
* Create a simple Dockerfile + `docker-compose.yml`. 🐳
* Replace the mean forecast with a quick Random Forest baseline and add evaluation. 🔧

Tell me which of the above you'd like next — I’ll add it! 🙌
