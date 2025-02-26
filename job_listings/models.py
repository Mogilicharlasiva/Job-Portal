from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class JobPost(models.Model):
    post_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField("Published on")
    posted_by = models.CharField(max_length=100)
    job_desc = models.TextField()

    def published_on(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_title
