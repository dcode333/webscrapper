from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def scrape_results(url, count):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.select('#myTable tbody tr')[:count]

    results = [{
        'dateTime': row.select_one('.dataMt').text.strip(),
        'team_b': row.select_one('.teamBmatch').text.strip() if row.select_one('.teamBmatch') else '',
        'team_a': row.select_one('.teamAmatch').text.strip() if row.select_one('.teamAmatch') else '',
        'prediction': row.select_one('.predMt a').text.strip() if row.select_one('.predMt a') else '',
        'odds': row.select_one('.oddPredBook').text.strip() if row.select_one('.oddPredBook') else '',
        'score': row.select_one('.resultMt').text.strip() if row.select_one('.resultMt') else '',
        'result': row.select_one('.imgCorrect img')['title'] if row.select_one('.imgCorrect img') else '',
        'lg': row.select_one('.iconLega img')['alt'] if row.select_one('.iconLega img') else '',
    } for row in rows if row.select_one('.dataMt')]

    return results

@app.route('/')
def index():
  return jsonify({"Prompt":"Hello from Umair"})
  
@app.route('/<int:count>')
def get_results(count):
    url = 'https://www.bettingclosed.com/predictions/date-matches/today/'

    results = scrape_results(url, count)
    return jsonify(results)


@app.route('/mixed/<int:count>')
def get_results2(count):
    url = 'https://www.bettingclosed.com/predictions/date-matches/today/bet-type/mixed'

    results = scrape_results(url, count)
    return jsonify(results)


@app.route('/underover/<int:count>')
def get_results3(count):
    url = 'https://www.bettingclosed.com/predictions/date-matches/today/bet-type/under-over'

    results = scrape_results(url, count)
    return jsonify(results)


@app.route('/golnogol/<int:count>')
def get_results4(count):
    url = 'https://www.bettingclosed.com/predictions/date-matches/today/bet-type/gol-nogol'

    results = scrape_results(url, count)
    return jsonify(results)


@app.route('/finalscores/<int:count>')
def get_results5(count):
    url = 'https://www.bettingclosed.com/predictions/date-matches/today/bet-type/correct-scores'

    results = scrape_results(url, count)
    return jsonify(results)





if __name__ == '__main__':
  app.run(port=5000)
