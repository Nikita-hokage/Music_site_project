

from django.db import models


class Janr(models.Model):
    janr = models.CharField(max_length=999)
    description = models.CharField(max_length=999)

    def __str__(self):
        return self.janr + ' ' + self.description

class Author(models.Model):
    songAuthor = models.CharField(max_length=999)
    janr = models.ForeignKey(to=Janr, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.songAuthor



class Song(models.Model):
    songname = models.CharField(max_length=999)
    albums = models.CharField(max_length=999)
    description = models.CharField(max_length=999)
    janr = models.ForeignKey(to=Janr, on_delete=models.PROTECT, null=True)
    songAuthor = models.ForeignKey(to=Author, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.songname + ' ' + self.albums + ' ' + self.description