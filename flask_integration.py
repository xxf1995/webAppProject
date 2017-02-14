#!/usr/bin/env python3
'''
    javascript_sample.py
    Jeff Ondich, 5 May 2016
    Modified by Eric Alexander, 10 February 2017

    Flask app serving up the pieces of the javascript-sample for
    CS 257, Spring 2016.
'''
import sys, flask, datetime
from flask import jsonify, request

app = flask.Flask(__name__, static_folder='website/static', template_folder='website')

@app.route('/')
def get_main_page():
    return flask.render_template('index.html')

@app.route('/date/')
def get_date():
    return datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M:%S %p")

@app.route('/playerStats/', methods=['POST'])
def playerStats():
    playerName = request.form['srch-term-players']
    result = api.getAllAttributes(playerName)
    return jsonify(results = result)

@app.route('/comparePlayers/', methods=['POST'])
def comparePlayerStats():
    player1 = request.form['srch-term-comparePlayers-1']
    player2 = request.form['srch-term-comparePlayers-2']
    result = api.compareDifference(player1, player2)
    return jsonify(results = result)

@app.route('/similarPlayers/', methods=['POST'])
def findSimilarPlayers():
    playerName = request.form['srch-term-similarPlayers']
    result = api.similarPlayer(playerName)
    return jsonify(results = result)

@app.route('/fruitPlease/')
def get_fruit():
    fruitRatings = [
        {
            'name': 'banana',
            'rating': 6
        },
        {
            'name': 'blueberry',
            'rating': 8
        },
        {
            'name': 'apple',
            'rating': 9
        }
    ]
    
    return jsonify({'results': fruitRatings})

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
