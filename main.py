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
    # loader = unittest.TestLoader()
    # loader.testMethodPrefix = "test_prefix"# default value is "test"
    #
    # suite1 = loader.discover('Test1', pattern = "Test*.py")
    # suite2 = loader.discover('Test2', pattern = "Test*.py")
    # alltests = unittest.TestSuite((suite1, suite2))
    # unittest.TextTestRunner(verbosity=2).run(alltests)


manager.run()
