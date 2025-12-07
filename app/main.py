from fastapi import FastAPI
from app.scraper import parse_restaurants

app = FastAPI()

@app.get("/restaurants/")
def get_restaurants(city: str = "Нур-Султан", num_restaurants: int = 100):
    data = parse_restaurants(city, num_restaurants)
    return {"restaurants": data}
