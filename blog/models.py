from django.db import models
#from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author 	= models.ForeignKey('auth.User', 'on_delete')
	title 	= models.CharField(max_length=200)
	image	= models.ImageField(upload_to='library/', default="img.jpg")
	text	= models.TextField()
	created_date	= models.DateTimeField()
	published_date	= models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title
