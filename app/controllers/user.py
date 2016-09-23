from app import app

@app.route('/login/<string:key>')
def login(key):
    return 'user %s login' % key
