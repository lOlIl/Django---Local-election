from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Answer(models.Model):
	"""Model representing answers for questions"""
	text = models.CharField(_(u'text'), max_length=50, help_text=_(u'Text of answer.'))

	def __unicode__(self):
		return "(%d) %s" % (self.pk, self.text)

class Question(models.Model):
	"""Model representing election questions"""
	text = models.CharField(_(u'text'), max_length=50, help_text=_(u'Text of election question.'))
    	max = models.IntegerField(_(u'max'), default=1, help_text=_(u'Maximum count of selectable answers.'))
    	mutiple = models.BooleanField(_(u'multiple'), default=False, help_text=_(u'Multiple answers for election question.'))
    	candidate = models.BooleanField(_(u'candidate'), default=True, help_text=_(u'Is candidate question.'))
	answer = models.ManyToManyField(Answer, blank=True, null=True, verbose_name=_(u'list of answers'), help_text=_(u'Answers for question.'))

	def __unicode__(self):
		return "(%d) %s" % (self.pk, self.text)

class Election(models.Model):
	"""Model representing election event"""
    	name = models.CharField(_(u'title'), max_length=50, help_text=_(u'Name of the election.'))
    	description = models.TextField(_(u'description'), blank = True, help_text = _(u'Description of election.'))
	created_by = models.CharField(_(u'author'), max_length=50, blank=True, help_text=_(u'Name of the creator of election.'))
	created_at = models.DateTimeField(_(u'creation time'), blank=True, null=True, help_text=_(u'Date-time stamp of creation of the election.'))
    	start = models.DateTimeField(_(u'start time'), blank=True, null=True, help_text=_(u'Date-time stamp of the election start.'))
    	end = models.DateTimeField(_(u'end time'), blank=True, null=True, help_text=_(u'Date-time stamp of the election end.'))
    	visibility = models.BooleanField(_(u'visible'), default=True, help_text=_(u'Boolean control of election visibility.'))
    	image = models.FileField(_(u'photo'), upload_to='election/%Y/%m/%d', blank=True)
	question = models.ManyToManyField(Question, blank=True, null=True, verbose_name=_(u'list of questions'), help_text=_(u'Questions for election.'))

	def __unicode__(self):
		return self.name

class Voter(models.Model):
	"""Model representing voters for election"""
	user = models.ForeignKey(User, verbose_name=_(u'user'), help_text=_(u'User, which is configured as voter.'))
	election = models.ForeignKey(Election, verbose_name=_(u'election'), help_text=_(u'Election, which user has voting rights.'))
	voted = models.BooleanField(_(u'visible'), default=False, help_text=_(u'Is user has already voted.'))
