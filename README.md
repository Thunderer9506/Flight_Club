# ✈ Flight Club – Automated Flight Deal Tracker

**Flight Club** is a Python-based automation tool that tracks flight prices for multiple destinations and notifies subscribed users when prices drop below a specified threshold.  
It integrates with **Google Sheets** (via Sheety API), **Kiwi.com Tequila API** for flight searches, **Twilio** for SMS notifications, and **SMTP** for email alerts.

---

## 📂 Project Structure

```
Flight_Club/
│
├── data_manager.py        # Handles Google Sheets data fetching & updates
├── flight_data.py         # Data model for storing flight details
├── flight_search.py       # Interfaces with Kiwi Tequila API for flight searches
├── main.py                # Main execution script
├── notification_manager.py# Sends SMS & email notifications
├── user.py                # Registers new users in Google Sheet
└── .env                   # Stores sensitive credentials (not committed)
```

---

## 🚀 How It Works

1. **User Registration** (`user.py`)
   - Collects user’s first name, last name, and email.
   - Saves this data into the Google Sheet via Sheety API.
   
2. **Data Retrieval** (`data_manager.py`)
   - Fetches destination list and lowest desired price from Google Sheets.
   - Updates missing IATA codes for destinations.

3. **Flight Search** (`flight_search.py`)
   - Queries **Kiwi Tequila API** for flight prices between the origin city and each destination.
   - Looks for round trips within 1 day to 6 months from now.
   - Supports direct flights only (`max_stopovers=0`).

4. **Price Comparison** (`main.py`)
   - Compares found prices with the target price from the sheet.
   - If a lower price is found, sends notifications.

5. **Notifications** (`notification_manager.py`)
   - **SMS** alerts via Twilio.
   - **Email** alerts to all registered users via SMTP.

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Thunderer9506/Flight_Club.git
cd Flight_Club
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory with:
```env
SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_AUTHORIZATION=Bearer your_sheety_token
TEQUILA_ENDPOINT=https://api.tequila.kiwi.com
TEQUILA_API=your_tequila_api_key
TWILIO_ACC_SID=your_twilio_sid
TWILIO_ACC_TOKEN=your_twilio_auth_token
TWILIO_PHONE_FROM=your_twilio_number
TWILIO_PHONE_TO=recipient_number
MY_EMAIL=your_email@gmail.com
MY_EMAIL_PASSWORD=your_email_password
```

### 4️⃣ Configure Google Sheet
- Your sheet must have columns for **city**, **iataCode**, **lowestPrice**.
- The `user` sheet should store **firstname**, **lastname**, and **email**.

### 5️⃣ Run the Scripts
- **Register a new user**:
```bash
python user.py
```
- **Start flight price tracking**:
```bash
python main.py
```

---

## 📜 File-by-File Overview

### **`data_manager.py`**
- Fetches data from the Google Sheet.
- Updates destination IATA codes using Sheety API.
- Stores sheet data in `destination_data`.

### **`flight_data.py`**
- A simple class to hold flight information:
  - Price
  - Origin & destination cities/airports
  - Departure & return dates
  - Optional stopovers and via cities

### **`flight_search.py`**
- **`get_destination_codes(city_name)`**: Gets IATA airport code for a given city.
- **`check_flights()`**: Searches for flights within a given date range.
- Returns a `FlightData` object.

### **`notification_manager.py`**
- **`send_msg(body)`**: Sends an SMS alert via Twilio.
- **`send_email(body, link)`**: Sends an email with flight details and a booking link to all registered users.

### **`main.py`**
- Orchestrates the process:
  - Retrieves data
  - Updates missing IATA codes
  - Searches for flights
  - Sends alerts for deals found

### **`user.py`**
- Collects new subscriber details.
- Posts data to Google Sheet via Sheety API.

---

## 📌 Example Output
```
Paris: ₹25500
Low price alert! Only ₹24000 to fly from Delhi-DEL to Paris-CDG,
from 2025-08-20 to 2025-08-27.
Link: https://www.google.co.in/flights?...
MSG SENT
```

---

## ⚠️ Notes
- Ensure `.env` is **never** committed to GitHub.
- Requires a valid Google Sheet and Sheety API setup.
- Twilio trial accounts can only send SMS to verified numbers.
