from django.db import models
# Create your models here.


  
class Image(models.Model):
    image_type = models.CharField(max_length=16)
    tag = models.CharField(max_length=16)
    webformatURL = models.URLField(max_length=256)
    views = models.PositiveIntegerField(default=0)
    downloads = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    user = models.CharField(max_length=16)
    userimageURL = models.URLField(max_length=256)
  
    def __str__(self):
        return f"{self.tag} - {self.webformatURL}"

    # class Meta:
    #     ordering = ['-views']
  
