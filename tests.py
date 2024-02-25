import requests


def test_params():
    res = requests.get('http://127.0.0.1:5000?symbol=MSFT&interval=1d&period=5d')
    print(type(res))
    return res.json()

def test_bad_symbol():
    res = requests.get('http://127.0.0.1:5000?symbol=NOTASYMBOL')
    print(type(res))
    return res.json()

def test_bad_params():
    res = requests.get('http://127.0.0.1:5000?notaparam=asdf')
    print(type(res))
    return res.json()


print(test_bad_symbol())
print(test_bad_params())
print(test_params())