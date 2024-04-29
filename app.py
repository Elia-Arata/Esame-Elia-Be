from flask import Flask, jsonify 
from weather_list import weather
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

# run: python3 app.py
# api call -> http://127.0.0.1:5000/api/weather/history

@app.route('/api/weather/history', methods=['GET'])
def get_weather_list():
    return jsonify(weather)

if __name__ == '__main__':
    app.run()