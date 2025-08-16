import time
import threading
import uvicorn
from fastapi import FastAPI
from pyngrok import ngrok
import nest_asyncio
from db import Base, engine
from auth import create_test_user
from routes import router  # make sure this file exists

# Create tables
Base.metadata.create_all(bind=engine)

# Create default test user
create_test_user()

# Setup FastAPI
app = FastAPI(title="User Profile Analyzer")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the User Profile Analyzer API"}

# Allow nested event loops (for ngrok)
nest_asyncio.apply()

# Kill existing tunnels (in case of reruns)
ngrok.kill()

# Start ngrok tunnel
public_url = ngrok.connect(8000)
print("🔗 Public URL:", public_url.public_url)

# Start FastAPI app in a thread
def run_app():
    uvicorn.run(app, host="0.0.0.0", port=8000)

thread = threading.Thread(target=run_app)
thread.start()

time.sleep(2)
print(f" FastAPI server is live!\nVisit: {public_url.public_url}/docs to access Swagger UI")

