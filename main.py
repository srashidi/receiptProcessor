from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()
receipts = {}


@app.get("/")
async def root():
    return {"message": "Welcome to My Receipt Processor"}

@app.post("/receipts/process")
async def process_receipt(receipt: dict):
    receipt_id = uuid4()
    receipts[receipt_id] = receipt
    return receipt_id

@app.get("/receipts/{receipt_id}.points")
async def get_receipt_points(receipt_id: str):
    pass
