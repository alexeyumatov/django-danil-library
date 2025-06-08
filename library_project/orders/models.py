from django.db import models


class Order(models.Model):
    id = models.IntegerField(
        primary_key=True
    )

    book = models.ForeignKey(
        "books.Book",
        verbose_name="Книга",
        on_delete=models.CASCADE
    )

    user_name = models.CharField(
        verbose_name="Имя пользователя",
        max_length=50
    )

    user_email = models.EmailField(
        verbose_name="Email пользователя",
        max_length=254
    )

    user_address = models.CharField(
        verbose_name="Адрес пользователя",
        max_length=100
    )

    comment = models.TextField(
        verbose_name="Комментарий",
        max_length=250
    )

    date = models.DateField(
        verbose_name="Дата заказа",
        auto_now_add=True
    )


class Feedback(models.Model):
    id = models.IntegerField(
        primary_key=True
    )

    user_email = models.EmailField(
        verbose_name="Email",
        max_length=254
    )

    comment = models.TextField(
        verbose_name="Комментарий",
        max_length=250
    )

    date = models.DateField(
        verbose_name="Дата заказа",
        auto_now_add=True
    )
