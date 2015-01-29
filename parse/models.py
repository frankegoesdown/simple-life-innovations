from django.db import models


class Sites(models.Model):
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Sites"

class Tags(models.Model):
	info = models.TextField()
	url = models.ForeignKey(Sites)

	class Meta:
		verbose_name_plural = "Tags"