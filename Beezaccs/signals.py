# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from .models import Customer

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#         print('Customer Add Done..!!!')

# post_save.connect(create_user_profile, sender=User)