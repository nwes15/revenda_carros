from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print("###Car pre save###")
    print(instance)

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):

    print("###Car post save###")
    print(instance)

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print("###Car pre delete###")
    print(instance)

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print("###Car post delete###")
    print(instance)

