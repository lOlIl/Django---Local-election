from django.contrib import admin
from election.models import Election, Question, Answer, Voter, Candidate

class QuestionInline(admin.TabularInline):
	model = Election.question.through

class VoterInline(admin.TabularInline):
    	model = Voter

class CandidateInline(admin.TabularInline):
    	model = Candidate

class ElectionAdmin(admin.ModelAdmin):
	def voters_total(self, obj):
		return obj.voter_set.count()
	def voted_percentage(self, obj):
		return str(round(obj.voter_set.filter(voted=True).count()/float(obj.voter_set.count()),2)) + " %"
	def candidates_total(self, obj):
		return obj.candidate_set.count()


	list_display = ('name', 'start', 'end', 'visibility', 'candidates_total', 'voters_total', 'voted_percentage')
	fields = ('name', 'description', 'start', 'end', 'visibility', 'image')	
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
