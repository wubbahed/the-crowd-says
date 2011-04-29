import os

from django.utils import simplejson

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.api import channel

from md5 import md5
import random
from datetime import datetime

class AdminHandler(webapp.RequestHandler):
    def get(self):
		token = channel.create_channel('thecrowdsays_display')
		template_values = {'token': token, 'id' : token }
		path = os.path.join(os.path.dirname(__file__) + '/../templates/', 'display.html')
		self.response.out.write(template.render(path, template_values))

class MainHandler(webapp.RequestHandler):
    def get(self):
		token = str(random.random()) + " - " + str(random.random()) + " = " + str(datetime.now().microsecond)
		token_id = md5(token).hexdigest()
		template_values = {'token': token, 'id' : token_id }
		path = os.path.join(os.path.dirname(__file__) + '/../templates/', 'client.html')
		self.response.out.write(template.render(path, template_values))
		
class UpdateHandler(webapp.RequestHandler):
	def post(self):
		result = self.request.get('id') + "," + self.request.get('p')
		try:
			channel.send_message('thecrowdsays_display', result)
		except channel.InvalidChannelClientIdError:
			result = ""	