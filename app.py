from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized v1.0'


#Serve traffic on localhost:5000
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
