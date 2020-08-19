from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def helloWorld():
    data = {'mensagem': os.environ.get('HELLO') + ' ;) ' + os.environ.get('APP_ENV') }
    return jsonify(data)

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
    