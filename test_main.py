import unittest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import json

app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Welcome to My Receipt Processor"}


client = TestClient(app)


def assert_receipt_points(receipt: dict, points: int):
    # Submit the receipt to process
    response1 = client.post("/receipts/process", json=receipt)
    assert response1.status_code == 200
    receipt_id = response1.json()['id']

    # Query the API for points earned from receipt
    response2 = client.get(f"/receipts/{receipt_id}/points")
    assert response2.status_code == 200
    assert response2.json()['points'] == points


class TestCase(unittest.TestCase):

    def test_read_main(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to My Receipt Processor"}

    def test_early_receipt_points(self):
        receipt = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                    "shortDescription": "Mountain Dew 12PK",
                    "price": "6.49"
                }, {
                    "shortDescription": "Emils Cheese Pizza",
                    "price": "12.25"
                }, {
                    "shortDescription": "Knorr Creamy Chicken",
                    "price": "1.26"
                }, {
                    "shortDescription": "Doritos Nacho Cheese",
                    "price": "3.35"
                }, {
                    "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                    "price": "12.00"
                }
            ],
            "total": "35.35"
        }

        assert_receipt_points(receipt, 28)

    def test_mid_afternoon_receipt_points(self):
        receipt = {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                }, {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                }, {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                }, {
                    "shortDescription": "Gatorade",
                    "price": "2.25"
                }
            ],
            "total": "9.00"
        }

        assert_receipt_points(receipt, 109)


if __name__ == '__main__':
    unittest.main()
