from django.db import models
from cms.models.fields import PlaceholderField


class Message(models.Model):
    message = PlaceholderField('message')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class User(models.Model):
    nick = models.CharField(
        verbose_name='Nick',
        unique=True,
        max_length=33)
    email = models.EmailField(
        unique=True,
        verbose_name='Email')
    password = models.CharField(
        verbose_name='Password',
        max_length=33)
    message = models.ForeignKey(
        Message,
        on_delete=models.SET('User deleted'),
        verbose_name='Message',
        null=True)

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Topic(models.Model):
    name = models.TextField(
        verbose_name='Topic')
    message = models.ForeignKey(
        Message,
        verbose_name='Message',
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


