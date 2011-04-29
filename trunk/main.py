from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from app.views import *

def main():

    application = webapp.WSGIApplication([
		(r'/display', AdminHandler),
		(r'/update', UpdateHandler),
		(r'.*', MainHandler)
		], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
