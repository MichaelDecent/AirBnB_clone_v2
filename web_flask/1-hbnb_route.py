from web_flask import app

@app.route('/', strict_slashes=False)
@app.route('/hbnb', strict_slashes=False)
def hello_page():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')