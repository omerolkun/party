from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields.related import ForeignKey

# Create your models here.
MEMBER_STATUS = (
    ('member','member'),
    ('party friend','p friend'),
)
IS_CO = (
    ('economy','eco'),
    ('woman','female'),
    ('culture','cultur'),
    ('union','unionx'),
)
class Columnist(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=30,validators=[MaxValueValidator(100),MinValueValidator(18)])
    membership = models.CharField(max_length=30, choices=MEMBER_STATUS)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    issue = models.CharField(max_length=30, choices=IS_CO)
    article_writer = ForeignKey(Columnist,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
