from flask import Flask ,request ,send_file
import base64
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class InteractWithMe(Resource):

    def saveFile(self,data):
        with open("YourQuery.mp3", "wb") as fh:
            fh.write(base64.b64decode(data))

    def post(self):
        json=  request.get_json()
        jsonvalue=json.get("audioByteArray")
        self.saveFile(jsonvalue)
        base64.b64decode(jsonvalue)
        result=send_file("YourQuery"+".mp3", as_attachment=True)
        return  result

    def get(self):
        result = send_file("YourQuery" + ".mp3", as_attachment=True)
        return result

api.add_resource(HelloWorld, '/')
api.add_resource(InteractWithMe, '/interaction')

if __name__ == '__main__':
    app.run(debug=True)