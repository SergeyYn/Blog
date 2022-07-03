from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('post-details', args=(str(self.id)))



    def save(self, previous_cat=None, *args, **kwargs):
        super().save(*args, **kwargs)
        if previous_cat:
            print('sending to post_list_%s' % previous_cat)
            async_to_sync(get_channel_layer().group_send)(
                'post_list_%s' % previous_cat, {"type": "update.list"}
            )
            print('sent! to post_list_%s' % self.category.id)
        print('sending to post_list_%s' % self.category.id)
        async_to_sync(get_channel_layer().group_send)(
            'post_list_%s' % self.category.id, {"type": "update.list"}
        )
        print('sent! to post_list_%s' % self.category.id)
        print('sending to post_list_0')
        async_to_sync(get_channel_layer().group_send)(
            'post_list_0', {"type": "update.list"}
        )
        print('sent! to post_list_0')