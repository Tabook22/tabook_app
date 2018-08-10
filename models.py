from django.db.models import(
    Model,
    TextField
)

# Create your models here.
class Tabooksite(Model):
    title=TextField(null=True, blank=True)
    description=TextField(null=True, blank=True)

    def __str__(self):
        return "Tabook Site  Title {} ".format(self.title)
