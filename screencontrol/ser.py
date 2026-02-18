from flask import Flask, request

app = Flask(__name__)
debugMode=False

if not debugMode:
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)


@app.route('/mouse', methods=['POST'])
def mouse():
    data=request.get_json()
    print(type(data),data)
    return "OK"

@app.route('/click', methods=['POST'])
def click():
    data=request.get_json()
    print(type(data),data)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
