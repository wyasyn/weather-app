from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    
    # Check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = 'Kampala'
        
    weather = get_current_weather(city)
    
    # City is not found
    
    if not weather['cod'] == 200:
        return render_template('city-not-found.html')
    
    return render_template(
        'weather.html', 
        title=weather["name"], 
        status=weather["weather"][0]["description"].capitalize(),
        temp=f"{weather['main']['temp']:.1f}",
        feels_like=f"{weather['main']['feels_like']:.1f}",
        humidity=weather["main"]["humidity"],
        pressure=weather["main"]["pressure"],
        wind_speed=weather["wind"]["speed"],
        wind_deg=weather["wind"]["deg"])

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8001)