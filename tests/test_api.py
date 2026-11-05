import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def test_get_all_bookings():
    response = requests.get(f"{BASE_URL}/booking")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_booking():
    new_booking = {
        "firstname": "Vadym",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-10",
            "checkout": "2026-11-15"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(f"{BASE_URL}/booking", json=new_booking)

    assert response.status_code == 200
    data = response.json()
    assert "bookingid" in data
    assert data["booking"]["firstname"] == "Vadym"


def test_create_and_get_booking():
    new_booking = {
        "firstname": "Vadym",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-11-10",
            "checkout": "2026-11-15"
        },
        "additionalneeds": "Breakfast"
    }

    create_response = requests.post(f"{BASE_URL}/booking", json=new_booking)
    print(create_response.json())

    booking_id = create_response.json()["bookingid"]
    print(f"Booking ID: {booking_id}")

    get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")

    assert get_response.status_code == 200
    assert get_response.json()["firstname"] == "Vadym"


def test_get_non_existent_booking():
    response = requests.get(f"{BASE_URL}/booking/999999999")

    assert response.status_code == 404