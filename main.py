import math
from datetime import time
from decimal import Decimal
from uuid import uuid4
from fastapi import FastAPI

from models.receipt import Receipt

app = FastAPI()
receipts = {}


@app.get("/")
async def root():
    return {"message": "Welcome to My Receipt Processor"}


@app.post("/receipts/process")
async def process_receipt(receipt: dict):
    receipt_id = str(uuid4())  # Generate random ID
    receipts[receipt_id] = Receipt(**receipt)  # Add receipt to "database" with key of ID

    return {"id": receipt_id}


@app.get("/receipts/{receipt_id}/points")
async def get_receipt_points(receipt_id: str):
    points = 0

    if receipt_id in receipts:
        receipt = receipts[receipt_id]

        # Add points equal to number of alphanumeric characters in the retailer name
        points += sum(char.isdigit() or char.isalpha() for char in receipt.retailer)

        # Add 50 points if total is a round dollar amount
        if receipt.total % 1 == 0:
            points += 50

        # Add 25 points if total is a multiple of 0.25
        if receipt.total % Decimal('0.25') == 0:
            points += 25

        # Add 5 points for every two items on the receipt
        points += (len(receipt.items) // 2) * 5

        # Earn points for items based on trimmed item description length and item price
        for item in receipt.items:
            if len(item.shortDescription.strip()) % 3 == 0:
                points += math.ceil(item.price * Decimal('0.2'))

        # Add 6 points if the day of the purchase date is odd
        if receipt.purchaseDate.day % 2 == 1:
            points += 6

        # Add 10 points if the time of purchase is after 2:00pm and before 4:00pm
        if time(14) < receipt.purchaseTime < time(16):
            points += 10

    return {"points": points}
