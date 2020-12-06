import uuid
from django.db import models
from django.urls import reverse


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk':str(self.id)})
