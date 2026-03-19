# Risk Monitoring & Alerts System

A Python-based system that analyzes financial data, calculates key risk metrics, and triggers alerts based on predefined thresholds.

---

## Overview

This project simulates a real-world **risk monitoring system** used in finance and operations.  
It continuously evaluates market data and flags abnormal conditions such as high volatility or sharp losses.

---

## Features

- Pulls real-time stock data using `yFinance`
- Calculates daily returns and volatility
- Detects risk conditions:
  - High volatility
  - Large daily losses
- Displays alerts in the terminal
- Logs system activity to `risk.log`

---

## Tech Stack

- **Python**
- **pandas**
- **yfinance**
- **logging**

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the system
```bash
python app.py
```

---

## Example Output

```text
Running Risk Monitoring System...

Volatility: 0.0135  
Latest Daily Return: -0.0073  

No major risk detected
```

---

## Key Concepts Demonstrated

- Risk metric calculation (volatility, returns)
- Threshold-based alert systems
- Real-time data ingestion
- Logging for monitoring and auditing

---

## Project Purpose

This project demonstrates how financial institutions monitor risk exposure in real time and trigger alerts when conditions exceed acceptable thresholds.

---
