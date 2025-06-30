# обновляем код main.py
import logging

from fastapi import FastAPI

from app.config import load_config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False


@app.get("/custom/")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello"}


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}
