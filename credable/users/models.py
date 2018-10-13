from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    credit_score = IntegerField()
    pan_number = CharField(max_length=15)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})