import json
from flask import Flask, render_template, request

app = Flask(__name__)

def load_services():
    # Убедитесь, что файл services.json существует в каталоге data/
    # Иначе приложение не запустится
    try:
        with open('data/services.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: data/services.json not found. Returning empty services list.")
        return []

@app.route('/')
def home():
    services = load_services()
    return render_template('index.html', services=services)

@app.route('/services')
def services():
    services = load_services()
    return render_template('services.html', services=services)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')
        # TODO: Implement email sending or database saving logic here
        print(f"New contact form submission: Name: {name}, Phone: {phone}, Message: {message}")
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

if __name__ == '__main__':
    # ...
    app.run(debug=True, host='0.0.0.0', port=8080)