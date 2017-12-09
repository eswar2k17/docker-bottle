from bottle import route, run
import os

@route('/index')
def hello():
    return "Hello" + os.environ['NAME'] + "!"

run(host='0.0.0.0', port=8080)
