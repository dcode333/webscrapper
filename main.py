from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

html = '<p>This is a paragraph of text.</p>'

# create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, 'html.parser')

# find the <p> tag and extract its text
p_tag = soup.find('p')
text = p_tag.text

@app.route('/')
def index():
  return jsonify(text)

if __name__ == '__main__':
  app.run(port=5000)
