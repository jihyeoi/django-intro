# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.core.exceptions import ValidationError
# from django.core.validators import FileExtensionValidator, RegexValidator


# class SISUsernameValidator(validators.RegexValidator):
#     regex = r"^[a-z][a-z0-9-]*\Z"
#     message = (
#         "Enter a valid username. This value may contain only lowercase "
#         "letters, numbers, and - characters."
#     )
#     flags = 0


# class User(AbstractBaseUser, PermissionsMixin):

#     username_validator = SISUsernameValidator()

#     username = models.CharField(
#         "username",
#         max_length=30,
#         primary_key=True,
#         help_text=(
#             "Required. 30 characters or fewer. Lowercase, digits and - only."
#         ),
#         validators=[username_validator],
#         error_messages={
#             "unique": "A user with that username already exists.",
#         },
#     )

#     first_name = models.CharField(_("first name"), max_length=150, blank=True)
#     last_name = models.CharField(_("last name"), max_length=150, blank=True)
#     email = models.EmailField(_("email address"), blank=True)

#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]

#     def get_full_name(self):
#         """
#         Return the first_name plus the last_name, with a space in between.
#         """
#         full_name = "%s %s" % (self.first_name, self.last_name)
#         return full_name.strip()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
