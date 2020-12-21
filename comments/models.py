from django.db import models


class UserComment(models.Model):
    user_name = models.CharField("Имя пользователя", max_length=50)
    comment_text = models.TextField("Текс комментария")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
