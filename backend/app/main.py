from fastapi import FastAPI
from app.api.routes import router
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Legal Document QA Bot")
app.include_router(router)

@app.get("/")
def serve_ui():
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)
    
    html_path = os.path.join(BASE_DIR,"..","..", "demo", "interface.html")
    
    with open(html_path, "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)