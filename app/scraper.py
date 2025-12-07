import requests
from fake_useragent import UserAgent

API_URL = "https://catalog.api.2gis.com/3.0/items"

def parse_restaurants(city: str = "Нур-Султан", limit: int = 1000):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    results = []
    page_size = 50
    pages = (limit // page_size) + 1

    for page in range(1, pages + 1):
        params = {
            "key": "6dbb3295-2484-483e-8eff-e883215e94c9",
            "q": f"restaurant {city}",
            "fields": "items.point,items.full_address_name",
            "page_size": min(page_size, limit - len(results)),
            "page": page,
            "type": "branch"
        }

        response = requests.get(API_URL, headers=headers, params=params)
        data = response.json()

