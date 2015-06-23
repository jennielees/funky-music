from flask import Flask, request, render_template, jsonify, session
from spotify import get_music

app = Flask(__name__)
app.secret_key = 'ilovesecrets'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/music', methods=['POST'])
def music():

    mood = request.form.get('mood')
    music = get_music(mood)

    # Store the mood in the session so we don't need to send it up all the time
    session['mood'] = mood

    return render_template('music.html', music=music)


@app.route('/api/music', methods=['POST'])
def music_api():

    offset = request.form.get('offset')
    mood = session.get('mood')

    # We can skip arguments with defaults - we don't need to supply 'limit'
    # but we do need to specify that the thing we're sending is 'offset'

    music = get_music(mood, offset=offset)

    return jsonify({'playlists': music}) # you can't just jsonify a list


if __name__ == "__main__":
    app.run(port=8080, debug=True)