from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def register_user(self):
        self.save()
        return True

    def update_user(self):
        self.save()
        return True

    def delete_user(self):
        self.delete()
        return True

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    stock = models.IntegerField(default=0)
    added_at = models.DateTimeField(default=timezone.now)

    def add_book(self):
        self.save()
        return True

    def update_book(self):
        self.save()
        return True

    def delete_book(self):
        self.delete()
        return True

    @classmethod
    def search_book(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def add_request(self):
        self.save()
        return True

    def update_request(self):
        self.save()
        return True

    def delete_request(self):
        self.delete()
        return True

    @classmethod
    def search_request(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    notification_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def create_notification(self):
        self.save()
        return True

    def update_notification_status(self, new_status):
        self.notification_status = new_status
        self.save()
        return True

    def send_notification(self):
        # Implement email sending logic here
        # For example, using Django's send_mail function
        # from django.core.mail import send_mail
        # send_mail(subject, message, from_email, [self.user.email])
        return True
