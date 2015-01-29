from django.contrib import admin

from parse.models import Sites
#admin.site.register(Sites)
# Register your models here.
class SitesAdmin(admin.ModelAdmin):
	"""
	Main class, show informations about users
	"""
	list_display = ("title", "url")
	class Meta:
			model = Sites
			fields = ("title", "url")

admin.site.register(Sites, SitesAdmin)