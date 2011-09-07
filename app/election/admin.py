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

admin.site.register(Election, ElectionAdmin)

class AnswerInline(admin.TabularInline):
	model = Question.answer.through

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('text', 'max', 'candidate', 'mutiple')
	exclude = ('answer', )
	inlines = [
        	AnswerInline
    	]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
