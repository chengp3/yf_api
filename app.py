from flask import Flask, jsonify, request
import yfinance as yf

"""

period: data period to download (Either Use period parameter or use start and end) Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
interval: data interval (intraday data cannot extend last 60 days) Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
start: If not using period - Download start date string (YYYY-MM-DD) or datetime.
end: If not using period - Download end date string (YYYY-MM-DD) or datetime.
prepost: Include Pre and Post market data in results? (Default is False)
auto_adjust: Adjust all OHLC automatically? (Default is True)

example:
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
    
"""

app = Flask(__name__)

@app.route('/')
def home():
    symbol = request.args.get('symbol')
    interval = request.args.get('interval')
    period = request.args.get('period')
    data = yf.download(symbol, interval=interval, period=period).to_json(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)