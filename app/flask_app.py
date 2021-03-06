from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Openshift Jenkins Pipeline Python/Nginx',
        'description': 'Find the implementation at here'
    },
    {
        'id': 2,
        'title': 'testing',
        'description': 'test teknovatus'
    },
    {
        'id': 3,
        'title': 'testing',
        'description': 'testing change'
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
