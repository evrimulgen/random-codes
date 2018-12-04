from bottle import Bottle, run

app = Bottle()

from bottle import error
@app.error(404)
def error404(error):
    return 'Nothing here, sorry'

run(app, host='localhost', port=8080)