from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey( Tag, default=None, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return str(self.id)+"."+self.title

