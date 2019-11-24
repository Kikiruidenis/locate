from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

Choices = (
	('M', 'Male'),
	('F', 'Female'),
)
CHOICES = (
	('dark', 'Dark'),
	('light', 'Light Skin'),
	('chocolate', 'Chocolate'),
)
class Lost(models.Model):
    user=models.ForeignKey(User)
    name=models.CharField(max_length=256)
    age=models.IntegerField(null=True)
    gender = models.CharField(max_length=1, choices=Choices, blank=True)
    clothes_color = models.CharField(max_length=120, null=True, blank=True)
    complexion = models.CharField(max_length=120, choices=CHOICES, blank=True)
    child_pic = models.ImageField(upload_to = 'HackOkPlease/pic_folder/',null=False)
    contact=models.CharField(null=True,max_length=256)
    found = models.BooleanField(default=False)
    published = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name  
    def all(self):
        return self.get_queryset()
    def get_absolute_url(self):
        return reverse('child:detail_view', args=[self.published.year, self.published.strftime('%m'),self.published.strftime('%d'),self.name])

class Found(models.Model):
    location = models.CharField(max_length=500)
    contact=models.CharField(null=True,max_length=256)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.location + ": " + str(self.videofile)
