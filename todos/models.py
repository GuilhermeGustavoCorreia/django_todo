from django.db import models
from datetime import date

class Todo(models.Model):

	title = models.CharField(verbose_name="Titulo" ,max_length=100, null=False, blank=False)
	ceated_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	deadline = models.DateTimeField(verbose_name="Prazo", null=False, blank=False)
	finished_at = models.DateTimeField(null=True)


	def mark_has_complete(self):

		if self.finished_at:
			self.finished_at = date.today()
			self.save()