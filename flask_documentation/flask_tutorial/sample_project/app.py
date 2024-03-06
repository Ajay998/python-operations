from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello world</h1>"

@app.route('/about')
def about(username):
    return "<p>About page</p>"

@app.route('/about/<username>')
def about_page(username):
    return f"<p>The is page of {username}</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
