import logging
import os

from flask_restplus import Api, Resource
from flask import Flask, request

from db.config import configure_mongo, MONGO_DB
from werkzeug.contrib.fixers import ProxyFix

logger = logging.getLogger('werkzeug')


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app)

configure_mongo(app, MONGO_DB)


@api.route('/imaj')
class Imaj(Resource):
    def post(self):
        enfo = request.json
        logger.info(request.json)

        teks = enfo['event']['text']
        imaj = enfo['event']['files'][0]['url_private_download']
        rapo = {
            'teks': teks,
            'iamj': imaj
        }
        logger.info(rapo)

        MONGO_DB.db.imaj_slack.insert_one(rapo)

        return request.json


@api.route('/lis-imaj')
class LisImaj(Resource):
    def get(self):
        return list(MONGO_DB.db.imaj_slack.find({}, {'_id': False}))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", default=8080))
    app.run(host='0.0.0.0', port=port)


