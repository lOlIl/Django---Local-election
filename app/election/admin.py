from django.contrib import admin
from election.models import Election, Question
from election.forms import ElectionAdminForm

class QuestionInline(admin.TabularInline):
	model = Election.question.through

class ElectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'start', 'end', 'visibility')
	fields = ('name', 'description', 'start', 'end', 'visibility', 'image')
	form = ElectionAdminForm
	inlines = [
        	QuestionInline,
    	]

admin.site.register(Election, ElectionAdmin)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'max', 'candidate', 'mutiple')

admin.site.register(Question, QuestionAdmin)
