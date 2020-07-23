from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def helloWorld():
    data = {'message': os.environ.get('HELLO') + ' ;) master'}
    return jsonify(data)

# start the development server using the run() method
if __name__ == "__main__":
    app.run()
    