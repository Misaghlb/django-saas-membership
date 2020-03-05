from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    # def __user_get_usersubscription(self):
    #     if not hasattr(self, '_usersubscription_cache'):
    #         user._usersubscription_cache = None
    #         for us in UserSubscription.active_objects.filter(user=user):
    #             if us.valid():
    #                 user._usersubscription_cache = us
    #                 break
    #
    #     return user._usersubscription_cache
