from dotenv import load_dotenv
import os

load_dotenv()

print("✅ Coinbase API Key:", os.getenv("COINBASE_API_KEY"))
from fastapi import FastAPI
from bot.dashboard.api import app as dashboard_app

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Crypto Trading Bot is running"}

# Mount the dashboard under /dashboard
app.mount("/dashboard", dashboard_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
