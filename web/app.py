from flask import Flask
from redis import Redis

app = Flask(__name__)
r = Redis(host='redis', port=6379)

@app.route('/')
def home():
    visits = r.incr('visits')
    return f"Hello! This page has been visited {r.get('visits').decode('utf-8')} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


