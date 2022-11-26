from django.db import models
class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modify_at', '-create_at', 'title')

    def __str__(self):
        return f'{self.title} | {self.content}'
