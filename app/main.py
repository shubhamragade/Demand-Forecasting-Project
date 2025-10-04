from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
from src.forecast import forecast, valid_combos

app = FastAPI(title="Food Demand Forecast API")
templates = Jinja2Templates(directory="app/templates")

# Create dropdown lists from train.csv combos
center_ids = valid_combos['center_id'].astype(str).unique().tolist()
meal_ids = valid_combos['meal_id'].astype(str).unique().tolist()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "center_ids": center_ids, "meal_ids": meal_ids}
    )

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request,
            center_id: str = Form(...),
            meal_id: str = Form(...),
            periods: int = Form(7)):

    try:
        preds = forecast(center_id, meal_id, periods)

        # Ensure forecast is a list
        if isinstance(preds, str):
            preds = [preds]

        return templates.TemplateResponse(
            "index.html",
            {"request": request,
             "forecast": preds,
             "center_id": center_id,
             "meal_id": meal_id,
             "center_ids": center_ids,
             "meal_ids": meal_ids}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request,
             "error": str(e),
             "center_ids": center_ids,
             "meal_ids": meal_ids}
        )
