from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("you must enter your Email")

        user = self.model(email=email, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD: str = "email"

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.email

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email
