from django.conf import settings
from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=100)
	price = models.FloatField()

	def _str__(self):
		return self.title

class orderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	def _str__(self):
		pass

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE)
	items = models.ManyToManyField(orderItem)
	start_date = models.DateTimeField(auto_now_add=True)
	order_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def _str__(self):
		return self.user.username