import yfinance as yf
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="risk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_data():
    df = yf.download("AAPL", period="1mo", interval="1d", auto_adjust=True)
    df = df.reset_index()
    return df

def calculate_risk(df):
    # Calculate daily returns
    df["Return"] = df["Close"].pct_change()

    # Calculate volatility (standard deviation of returns)
    volatility = df["Return"].std()

    # Get latest return
    latest_return = df["Return"].iloc[-1]

    return volatility, latest_return

def check_risk(volatility, latest_return):
    alerts = []

    # Rule 1: High volatility
    if volatility > 0.02:
        alerts.append("⚠️ High volatility detected")

    # Rule 2: Big daily drop
    if latest_return < -0.03:
        alerts.append("🚨 Large daily loss detected")

    return alerts

def main():
    print("Running Risk Monitoring System...\n")
    logging.info("System started")

    df = get_data()

    if df.empty:
        print("Error: No data fetched.")
        logging.error("No data fetched")
        return

    volatility, latest_return = calculate_risk(df)

    print(f"Volatility: {volatility:.4f}")
    print(f"Latest Daily Return: {latest_return:.4f}\n")

    logging.info(f"Volatility: {volatility}")
    logging.info(f"Latest Return: {latest_return}")

    alerts = check_risk(volatility, latest_return)

    if alerts:
        print("ALERTS:")
        logging.warning("Risk alerts triggered")

        for alert in alerts:
            print(alert)
            logging.warning(alert)
    else:
        print("✅ No major risk detected")
        logging.info("No major risk detected")

if __name__ == "__main__":
    main()