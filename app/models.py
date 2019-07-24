from django.db import models

class Chat(models.Model):
	id = models.BigIntegerField(primary_key=True, editable=True)
	username = models.CharField( max_length = 255 )
	first_name = models.CharField( max_length = 255 )
	last_name = models.CharField( max_length = 255 )
	phone_number = models.CharField( max_length = 255 )

class Message(models.Model):
	message_id = models.IntegerField()
	chat = models.ForeignKey( Chat, on_delete = models.DO_NOTHING )
	text = models.TextField( default = "" )
	my_in = models.SmallIntegerField( db_column = 'in', default=0 )
	previous_command = models.CharField( max_length = 255 )
	next_command = models.CharField( max_length = 255 )
	date = models.DateTimeField( auto_now_add=True )

class KeyboardButton(object):
	def __init__(self, text, action):
		self.text = text
		self.action = action
	def __str__(self):

		return self.text
	