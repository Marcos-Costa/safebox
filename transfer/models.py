from django.db import models
from varys.models import SingleTransaction,Box

# Any transference of any value from a box to another
class Transference (SingleTransaction):
	#From which safebox the money comes from
	origin = models.ForeignKey(
		Box,
		on_delete = models.SET_NULL,
		null = True,
		related_name = 'origin'
	)

	#To which safebox the money goes to
	destination = models.ForeignKey(
		Box,
		on_delete = models.SET_NULL,
		null = True,
		related_name = 'destination'
	)

	class Meta:
		# Human friendly singular and plural name
		verbose_name = 'Transferência'
		verbose_name_plural = 'Transferências'

	def delete(self, *args, **kwargs):
		origins = Box.objects.filter(id=self.origin.id)
		destinations = Box.objects.filter(id=self.destination.id)

		for origin, destination in zip(origins,destinations):
			origin.value = origin.value + self.value
			destination.value = destination.value - self.value

			origin.save()
			destination.save()
		super().delete(*args, **kwargs)  # Call the "real" save() method.
