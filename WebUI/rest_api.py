from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

x = 100
with open('db.json', 'r', encoding='utf-8') as f:
    text = json.load(f)

print(text)


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(text), 200
        for quote in text:
            if (quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

    def post(self):
        global x
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        parser.add_argument("id")
        params = parser.parse_args()
        x = x + 1
        quote = {
            "id": x,
            "author": params["author"],
            "quote": params["quote"]
        }
        text.append(quote)

        with open('db.json', 'w', encoding='utf-8') as f:
            json.dump(text, f, ensure_ascii=False, indent=4)
        return quote, 201


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    app.run(debug=True)
