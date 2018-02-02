from flask import Flask
from flask import render_template

from flask_cors import CORS

from api.api import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api')

CORS(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    print('http://0.0.0.0:5000/api')
    app.run(host="0.0.0.0", debug=True)

