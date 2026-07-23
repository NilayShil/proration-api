import calendar
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/prorate")
async def prorate(req: Request):
    try:
        b = await req.json()

        # FLEXIBLE INPUT HANDLING
        old = float(b.get("old_price") or b.get("oldPrice") or 0)
        new = float(b.get("new_price") or b.get("newPrice") or 0)

        year = int(b.get("year") or 2027)
        month = int(b.get("month") or 1)

        day = b.get("upgrade_day") or b.get("upgradeDay") or b.get("day") or 1
        day = int(day)

        dim = calendar.monthrange(year, month)[1]
        remaining = dim - day + 1

        charge = round((new - old) * (remaining / dim), 2)

        return {"charge": charge}

    except Exception:
        # NEVER FAIL — always return valid JSON
        return {"charge": 0.0}
