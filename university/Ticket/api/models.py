import uuid

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group


class Tag(models.Model):
    TagId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)


class Ticket(models.Model):
    OPEN = 'Open'
    PENDING = 'Pending'
    CLOSED = 'Closed'
    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (PENDING, 'Pending'),
        (CLOSED, 'Closed'),
    ]
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="creator")
    content = models.TextField(default="Enter text here")
    openDate = models.DateTimeField(auto_now_add=True)
    closeDate = models.DateTimeField(blank=True, null=True)
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="assignee")
    priority = models.IntegerField(default=4)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=OPEN)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    subject = models.TextField(max_length=50)


class Activity(models.Model):
    activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Author")
    external = models.BooleanField(default=False)
    message = models.TextField(default="Enter text here")
    attachment = models.FileField()
    ticket = models.ForeignKey(Ticket, related_name="activities", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)


