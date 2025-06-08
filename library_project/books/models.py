from datetime import datetime

from django.db import models
from django.core.validators import FileExtensionValidator

from PIL import Image


YEAR_CHOICES = []
for r in range(1800, (datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class Book(models.Model):
    id = models.IntegerField(
        primary_key=True
    )

    title = models.CharField(
        verbose_name="Название",
        max_length=100
    )

    author = models.CharField(
        verbose_name="Автор",
        max_length=100
    )

    description = models.CharField(
        verbose_name="Описание",
        max_length=500
    )

    cover = models.ImageField(
        verbose_name="Обложка книги",
        upload_to="images/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            )
        ]
    )

    year = models.IntegerField(
        verbose_name="Год издания",
        choices=YEAR_CHOICES,
        default=datetime.now().year
    )

    genre = models.CharField(
        verbose_name="Жанр"
    )

    def __str__(self):
        return f"Book: {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cover.path)
        if img.height > 300 or img.width > 450:
            output_size = (300, 450)
            img.thumbnail(output_size)
            img.save(self.cover.path)
        return
