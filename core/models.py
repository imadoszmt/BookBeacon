from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

class Person(AbstractUser):
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="person_set",
        related_query_name="person",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="person_set",
        related_query_name="person",
    )

    def register_user(self):
        return self.save()

    def login_user(self):
        return self

    def update_user(self):
        return self.save()

    def delete_user(self):
        return self.delete()

class User(Person):
    created_at = models.DateTimeField(auto_now_add=True)

class Admin(Person):
    def login_admin(self):
        return self

    def add_book(self, book):
        return book.save()

    def update_book(self, book):
        return book.save()

    def manage_notifications(self):
        # Implement notification management logic
        pass

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    stock = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def add_book(self):
        return self.save()

    def update_book(self):
        return self.save()

    def delete_book(self):
        return self.delete()

    @classmethod
    def search_book(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_request(self):
        return self.save()

    def update_request(self):
        return self.save()

    def delete_request(self):
        return self.delete()

    @classmethod
    def search_request(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    notification_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def create_notification(self):
        return self.save()

    def update_notification_status(self, status):
        self.notification_status = status
        return self.save()

    def send_notification(self):
        # Implement notification sending logic
        pass

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.notification_status}"
