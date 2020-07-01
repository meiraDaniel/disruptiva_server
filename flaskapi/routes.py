from flask import Flask, request, jsonify
from flaskapi import app

from flaskapi.youtubeApi import YoutubeApi


@app.route('/api/youtubeVideos')
def index():

    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')

    items = YoutubeApi().getInfoVideos('PLvegDljJljJzshbSFlWRq-qpDkMZnVbVK')
    
    response = jsonify({'videos': items})

    return response

    