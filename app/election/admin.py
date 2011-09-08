from django.contrib import admin
from election.models import Election, Question, Answer, Voter, Candidate
from election.forms import ElectionAdminForm

class QuestionInline(admin.TabularInline):
	model = Election.question.through

class VoterInline(admin.TabularInline):
    	model = Voter

class CandidateInline(admin.TabularInline):
    	model = Candidate

class ElectionAdmin(admin.ModelAdmin):
	list_display = ('name', 'start', 'end', 'visibility')
	fields = ('name', 'description', 'start', 'end', 'visibility', 'image')
	form = ElectionAdminForm
	inlines = [
        	QuestionInline, VoterInline, CandidateInline
    	]

class AnswerInline(admin.TabularInline):
	model = Question.answer.through

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'max', 'candidate')
	exclude = ('answer', )
	inlines = [
        	AnswerInline
    	]

class VoterAdmin(admin.ModelAdmin):
	list_display = ('election', 'user', 'voted')

class CandidateAdmin(admin.ModelAdmin):
	list_display = ('election', 'user')	

admin.site.register(Election, ElectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Voter, VoterAdmin)
admin.site.register(Candidate, CandidateAdmin)
