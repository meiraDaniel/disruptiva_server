from flask import Flask, request, jsonify
from flask_mail import Message
from apscheduler.schedulers.background import BackgroundScheduler

from flaskapi import app, mail, db
from flaskapi.youtubeApi import YoutubeApi
from flaskapi.models import Playlist

from datetime import datetime

def insertPlaylistVideos():

    try:
        videos = YoutubeApi().getInfoVideos('PLPTwwbrJNg5Bs659JJYqVeR4vQlDTe3rD')

        playlist_antiga = Playlist.query.first()
        playlist_antiga.playlist = str(videos)
        db.session.commit()

    except:
        print('error')


def createMsg(data):
    name = data['name']
    email = data['email']
    phone = data['phone']
    textMessage = data['textMessage']

    text_msg = f'''  Nome: {name}
  Email: {email}
  telefone: {phone}

  {textMessage}  
    '''

    return text_msg

@app.route('/api/sendMail', methods=['POST'])
def sendMail():
    data = request.get_json(silent=True)['data']

    text_msg = createMsg(data)
    msg = Message(f"Mensagem {data['name']}", sender='noreply@demo.com', recipients=['daniel-ams13@outlook.com'])
    msg.body = text_msg
    mail.send(msg)

    return jsonify({'sucess': 200})


@app.route('/api/getVideos', methods=['GET'])
def getVideos():

    response = jsonify({})
    response.headers.add('Access-Control-Allow-Origin', '*')

    playlist = Playlist.query.first()
    videos = eval(playlist.as_dict()['playlist'])

    response = jsonify({'videos': videos})

    return response


sched = BackgroundScheduler(daemon=True)
sched.add_job(insertPlaylistVideos,'cron',hour=14)
sched.start()

