from django.contrib import admin
from election.models import Election, Question, Answer, Voter
from election.forms import ElectionAdminForm

class QuestionInline(admin.TabularInline):
	model = Election.question.through

class VoterInline(admin.TabularInline):
    	model = Voter

class ElectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'start', 'end', 'visibility')
	fields = ('name', 'description', 'start', 'end', 'visibility', 'image')
	form = ElectionAdminForm
	inlines = [
        	QuestionInline, VoterInline
    	]

admin.site.register(Election, ElectionAdmin)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'max', 'candidate', 'mutiple')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
