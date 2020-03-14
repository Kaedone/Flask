from flask import Flask, escape, url_for, render_template
from start import get_table
app = Flask(__name__)
@app.route('/<param>')
def hello(param):
	return str(get_table(param))
if __name__ == "__main__":
    app.run(ssl_context='adhoc')
