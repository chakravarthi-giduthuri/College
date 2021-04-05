from django.db import models
from django.conf import settings
from datetime import datetime
#from django.conf import settings

User = settings.AUTH_USER_MODEL


class Posts(models.Model):
    # user = models.ForeignKey(User,
    #                          default=1,
    #                          null=True,
    #                          on_delete=models.SET_NULL
    #                          )
    title = models.CharField(max_length=120)
    summary = models.TextField()
    files = models.FileField(upload_to='files/media/', null=True, blank=True)
    img = models.ImageField(upload_to='files/images', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.files.delete()
        self.img.delete()
        super().delete(*args, **kwargs)
