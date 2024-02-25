### What is this  
This application builds a Flask microsevice that handles incoming GET requests and associated parameters, calls yfinance data feed API, and responds with the appropriate data (or error messages if appropriate).

### Requesting Data:  
clone, then 'python app.py'  
send GET request to end point: http://127.0.0.1:5000?symbol=AAPL[&param1=parameter][&param2=anotherparameter]...  
Parameters can be in any order but the first 'symbol' param MUST be present.  

#### Valid parameters:  
**period**: data period to download (Either Use period parameter or use start and end)
<li>**Valid periods**: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max</li>  
**interval**: data interval (intraday data cannot extend last 60 days)  
<li>**Valid intervals**: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo</li>
**start**: If not using period - Download start date string (YYYY-MM-DD) or datetime.  
**end**: If not using period - Download end date string (YYYY-MM-DD) or datetime.  
**prepost**: Include Pre and Post market data in results? (Default is False)  auto_adjust: Adjust all OHLC automatically? (Default is True)  

Returned data is a JSON object (call .json() method on response). Data will be value of key 'data', and status code will be in key 'status_code'. Status code will either be 200 or 500. If it is 500 (Internal Server Error), error message will be value of key 'error'.

### Example:  
import requests  
url = http://127.0.0.1:5000?symbol=AAPL  
response = requests.get(url)  
data = response.json()  
print(data)

{'data': [{'Adj Close': 404.0599975586, 'Close': 404.0599975586, 'High': 408.2900085449, 'Low': 403.4400024414, 'Open': 407.9599914551, 'Volume': 22281100}, {'Adj Close': 402.7900085449, 'Close': 402.7900085449, 'High': 404.4899902344, 'Low': 398.0100097656, 'Open': 403.2399902344, 'Volume': 24307900}, {'Adj Close': 402.1799926758, 'Close': 402.1799926758, 'High': 402.2900085449, 'Low': 397.2200012207, 'Open': 400.1700134277, 'Volume': 18631100}, {'Adj Close': 411.6499938965, 'Close': 411.6499938965, 'High': 412.8299865723, 'Low': 408.5700073242, 'Open': 410.1900024414, 'Volume': 27009900}, {'Adj Close': 410.3399963379, 'Close': 410.3399963379, 'High': 415.8599853516, 'Low': 408.9700012207, 'Open': 415.6700134277, 'Volume': 16284800}], 'status_code': 200}

### Diagram:  
![Screenshot 2024-02-24 at 1 50 00 PM](https://github.com/chengp3/yf_api/assets/22820728/54f3c71f-4d98-490f-bf52-e11cd88657f2)
