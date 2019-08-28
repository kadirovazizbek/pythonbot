from django.db import models

class Chat(models.Model):
	id = models.BigIntegerField(primary_key=True, editable=True)
	username = models.CharField( max_length = 255 )
	first_name = models.CharField( max_length = 255 )
	last_name = models.CharField( max_length = 255 )
	phone_number = models.CharField( max_length = 255 )

	def __str__(self):
		return self.username

class Message(models.Model):
	message_id = models.IntegerField()
	chat = models.ForeignKey( Chat, on_delete = models.DO_NOTHING )
	text = models.TextField( "text", default = "" )
	my_in = models.SmallIntegerField( "incoming", db_column = 'in', default=0 )
	previous_command = models.CharField( "prev_command", max_length = 255, null = True, blank = True )
	next_command = models.CharField( "next_command", max_length = 255, null = True, blank = True )
	date = models.DateTimeField( "date", auto_now_add=True )

	def __str__(self):
		return self.text
	

class KeyboardButton(object):
	def __init__(self, text, action):
		self.text = text
		self.action = action
	def __str__(self):

		return self.text
	