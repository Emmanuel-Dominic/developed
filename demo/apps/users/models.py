from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .validators import validate_zipcode


# Create your models here.
class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('username field is required!')
        if not email:
            raise ValueError('email field is required!')
        if not password:
            raise ValueError('password field is required!')
        self.username = username
        self.email = email
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_normal_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(username, email, password, **extra_fields)

    def create_staff_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    bio = models.TextField()
    zipcode = models.CharField(max_length=5, validators=[validate_zipcode])
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Invalid phone number, please start with '+********'")
    phone = models.CharField(validators=[MinLengthValidator(15)], max_length=16, unique=True) # validators should be a list
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
