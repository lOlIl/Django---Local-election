from django.contrib import admin
from election.models import Election
from election.forms import ElectionAdminForm

class ElectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'start', 'end', 'visibility')
	fields = ('name', 'description', 'start', 'end', 'visibility', 'image')
	form = ElectionAdminForm

admin.site.register(Election, ElectionAdmin)
