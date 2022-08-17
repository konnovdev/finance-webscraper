import json
from flask import Flask

from expected_growth import get_expected_growth

app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

# ticker - google finance ticker, ex: "AAPL", "GOOG"
@app.route('/exp_growth/<ticker>')
def exp_growth(ticker: str):
    return get_expected_growth(ticker)


app.run()
