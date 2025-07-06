from flask import Flask, send_from_directory, jsonify, render_template_string
import os

app = Flask(__name__)
MUSIC_FOLDER = os.path.join(os.path.dirname(__file__), 'musicas')

@app.route('/')
def index():
    # Serve o index.html diretamente
    with open(os.path.join(os.path.dirname(__file__), 'index.html'), encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/playlist')
def playlist():
    # Lista todos os arquivos de áudio na pasta musicas
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith(('.mp3', '.wav', '.ogg'))]
    playlist = []
    for f in files:
        playlist.append({
            'title': os.path.splitext(f)[0],
            'artist': '',
            'url': f'/musicas/{f}',
            'duration': '0:00'  # O frontend pode buscar a duração
        })
    return jsonify(playlist)

@app.route('/musicas/<path:filename>')
def music(filename):
    return send_from_directory(MUSIC_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
