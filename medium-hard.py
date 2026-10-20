from flask import Flask
from flask import request
import requests
from datetime import datetime, timedelta



nbu_api = 'https://bank.gov.ua/NBU_Exchange/exchange_site'

def nbu_request(base_url, date):
    params = {
        "start": date,
        "end": date,
        "valcode": "eur",
        "sort": "exchangedate",
        "order": "desc",
        "json": ""
        }
    return requests.get(base_url, params=params)



app=Flask(__name__)
@app.route("/", methods=["GET"])
def hello_world():
    return "Hello world!"

@app.route("/currency", methods=["GET"])
def currency():
    date = request.args.get('date')
    if not date:
        return "specify today/yesterday in query!"
    if date == "today":
        date = datetime.now().strftime('%Y%m%d')
        response = nbu_request(nbu_api, date)
        return response.json()
    elif date == "yesterday":
        date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        response = nbu_request(nbu_api, date)
        return response.json()
    else:
        return "unknown date man, only //'yesterday//' or //'today//'"
        


if __name__ == '__main__':
    app.run(host = "127.0.0.1", port=8000, debug=True)

