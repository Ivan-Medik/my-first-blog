import datetime
from django.db import models
from django.utils import timezone

# Создаю класс Article, который отвечает за создание статьи

class Article(models.Model):
	article_title = models.CharField("Название статьи.", max_length = 200)
	article_text = models.TextField("Текст статьи.")
	pub_date = models.DateTimeField("Дата публикации.")

	# Функция которая возвращает вместо индекса статьи, её название
	def __str__(self):
		return self.article_title

	# Функция которая возвращает нам True, если статье не больше 7 дней
	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	# Создаю класс Meta, который меняет название с англ на Русский
	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"

# Создаю класс Comment, который отвечает за создание комментариев к статье

class Comment(models.Model):
	arcticle = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField("Имя коментатора.", max_length = 50)
	comment_text = models.CharField("Текст коментатора.", max_length = 200)

	# Функция которая возвращает вместо индекса комментария, имя его автора
	def __str__(self):
		return self.author_name

	# Создаю класс Meta, который меняет название с англ на Русский
	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"