from flask import Flask, jsonify, request
import yfinance as yf
import json

"""

period: data period to download (Either Use period parameter or use start and end) Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
interval: data interval (intraday data cannot extend past 60 days) Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
start: If not using period - Download start date string (YYYY-MM-DD) or datetime.
end: If not using period - Download end date string (YYYY-MM-DD) or datetime.
prepost: Include Pre and Post market data in results? (Default is False)
auto_adjust: Adjust all OHLC automatically? (Default is True)

example:
data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")


invalid symbol returns: ['FDASFDA']: Exception('%ticker%: No timezone found, symbol may be delisted')
bad keywords: {"error":"download() got an unexpected keyword argument 'fdsaf'"}

"""

app = Flask(__name__)

@app.route('/')
def home():
    try:
        symbol = request.args.get('symbol')
        args = request.args.to_dict()
        for key in args.keys():
            if key not in ['symbol', 'period', 'interval', 'start', 'end', 'prepost', 'auto_adjust']:
                return {'error': f'invalid parameter: {key}', 'status_code': 500}
        if args.get('symbol'):
            del args['symbol']
        data = yf.download(symbol, **args).to_json(orient='records')
        parsed_data = json.loads(data)
        if len(parsed_data) == 0:
            return {'error': 'empty response, possible delisted/unlisted symbol', 'status_code': 500}
        return {'data': parsed_data, 'status_code': 200}
    except Exception as e:
        return {"error": str(e), 'status_code': 500}

if __name__ == '__main__':
    app.run(debug=False)