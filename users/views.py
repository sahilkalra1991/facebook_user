from urllib.request import urlopen
from allauth.socialaccount.models import SocialAccount
from django.core.files.base import ContentFile
from django.dispatch.dispatcher import receiver
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from allauth.account.signals import user_signed_up


class HomeView(TemplateView):
    """
    Home View to display User Name and Profile Picture
    """
    template_name = "users/home.html"

    def get_context_data(self, **kwargs):
        pass


@receiver(user_signed_up)
def facebook_profile_picture_receiver(sender, request, user, **kwargs):
    """
    This will fetch the profile picture and store it in User model
    """
    social_objs = SocialAccount.objects.filter(user_id=user.id, provider="facebook")
    if len(social_objs) > 0:
        avatar_url = social_objs[0].get_avatar_url()
        avatar = urlopen(avatar_url)
        user.profile_picture.save(
            slugify("{0}_{1}".format(user.username ,user.id)) + ".jpg",
            ContentFile(avatar.read())
        )
        user.save()
