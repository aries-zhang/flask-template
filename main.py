#!/usr/bin/env python
#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
# Run a test server.
from flask_script import Manager, Server
from app import app


manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0", port=9000))

@manager.command
def createdb():
    from app import db
    db.create_all()


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    import tests
    tests = unittest.TestLoader().discover('tests', pattern='*tests.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.run()
