from flask import Flask, escape, url_for, render_template
from start import get_table
app = Flask(__name__)
@app.route('/')
def hello():
	return str(get_table())
if __name__ == "__main__":
    app.run(host= '0.0.0.0',ssl_context='adhoc')
