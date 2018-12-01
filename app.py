
from flask import Flask, render_template, redirect, request, url_for, jsonify
from requests import get
from urllib.parse import urlencode
import json
import locale
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler()])

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html',
                           app_id=app.app_id,
                           app_code=app.app_code)


@app.route('/coordinates', methods=['POST'])
def coordinates():
    data = request.form
    logging.debug(data)
    if 'text' not in data:
        logging.error('no `text` field in form!')
        return jsonify({})
    else:
        text = data['text']
        logging.debug(text)
        #TODO(alexeyqu): extract coordinates from text
        return jsonify({})


try:
    with open('credentials.json') as fin:
        credentials = json.loads(fin.read())
        app.app_id, app.app_code = credentials['app_id'], credentials['app_code']
except (KeyError, FileNotFoundError, json.decoder.JSONDecodeError) as e:
    app.app_id, app.app_code = None, None
    logging.error("Error while reading HERE API credentials, proceed on your own risk!")
    logging.error(e)

if __name__ == '__main__':
    app.run()
