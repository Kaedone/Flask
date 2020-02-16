from flask import Flask, escape, url_for, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello')
def hello():
    return 'Hello world'
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)
if __name__ == "__main__":
    app.run()
