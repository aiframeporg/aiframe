from django.db import models
from django.core.exceptions import ValidationError

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    video = models.FileField(upload_to='blogs/videos/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.id}/"

    def clean(self):
        if self.image and self.video:
            raise ValidationError("You can upload either an image or a video, not both.")

    class Meta:
        verbose_name_plural = "Blogs"


class ModelPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='models/', blank=True, null=True)
    video = models.FileField(upload_to='models/videos/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/model/{self.id}/"

    def clean(self):
        if self.image and self.video:
            raise ValidationError("You can upload either an image or a video, not both.")

    class Meta:
        verbose_name_plural = "Models"


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tutorials/', blank=True, null=True)
    video = models.FileField(upload_to='tutorials/videos/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/tutorial/{self.id}/"

    def clean(self):
        if self.image and self.video:
            raise ValidationError("You can upload either an image or a video, not both.")

    class Meta:
        verbose_name_plural = "Tutorials"

class DownloadableApp(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='downloads/images/', blank=True, null=True)
    video = models.FileField(upload_to='downloads/videos/', blank=True, null=True)
    file = models.FileField(upload_to='downloads/files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure only one of image or video is uploaded
        if self.image and self.video:
            raise ValidationError("You can upload either an image or a video, not both.")

    def __str__(self):
        return self.title