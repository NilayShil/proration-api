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

        old = float(b["old_price"])
        new = float(b["new_price"])
        year = int(b["year"])
        month = int(b["month"])
        day = int(b["upgrade_day"])

        dim = calendar.monthrange(year, month)[1]
        remaining = dim - day + 1

        charge = round((new - old) * (remaining / dim), 2)

        return {"charge": charge}

    except Exception as e:
        return {"error": str(e)}
