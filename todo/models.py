from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок задачи')
    description = models.TextField(max_length=400, verbose_name='Описание задачи')
    is_solved = models.BooleanField(default=False, verbose_name='Выполнено')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_published = models.DateTimeField('date_published', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ( 'is_solved', '-date_published',)
