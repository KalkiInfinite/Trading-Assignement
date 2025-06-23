# Binance Futures Trading Bot (Testnet)

A simplified trading bot built with Python and Streamlit to place **Market** and **Limit** orders on the **Binance Futures USDT-M Testnet**. This project was developed as part of a technical task for a Junior Python Developer role.

## Features

- Connects to Binance Futures Testnet API
- Supports `MARKET` and `LIMIT` order types
- Handles both `BUY` and `SELL` orders
- Logs all API activity and errors
- Clean Streamlit web interface
- Modular, extensible Python code

---

## Demo Screenshot

![UI Screenshot](https://via.placeholder.com/800x400?text=Streamlit+UI+Trading+Bot)

---

## Technologies Used

- Python 3
- [python-binance](https://github.com/sammchardy/python-binance)
- Streamlit
- Logging

---

## Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/binance-futures-bot.git
   cd binance-futures-bot
   
2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your Binance Testnet API keys**

```bash
Create a file config.py and add:
API_KEY = "your_testnet_api_key"

API_SECRET = "your_testnet_api_secret"

BASE_URL = "https://testnet.binancefuture.com"
```
4. **Run the Streamlit app**
```bash
streamlit run app.py
