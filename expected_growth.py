import lxml as lxml
import lxml.html
import requests as requests

yahoo_finance_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',  # Do Not Track Request Header
    'Connection': 'close'
}


def get_expected_growth(ticker: str):
    r = requests.get("https://finance.yahoo.com/quote/" + ticker + "/analysis", headers=yahoo_finance_headers)
    page = r.text.encode('utf-8')
    html = lxml.html.fromstring(page)
    result = html.xpath("//*[@id='Col1-0-AnalystLeafPage-Proxy']/section/table[6]/tbody/tr[5]/td[2]")[0].text
    return result
