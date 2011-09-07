from django.db import models
from django.utils.translation import ugettext_lazy as _

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

	def __unicode__(self):
		return self.name 
