from app import app

@app.route('/blog/<string:key>')
def detail(key):
    return 'blog %s' % key

@app.route('/blogs/')
def list():
    return 'blog list'
