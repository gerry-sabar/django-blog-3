from django.db import models


def upload_location(article, filename):
    return "%s%s" % (article.id, filename)


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
