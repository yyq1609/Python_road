from django.db import models


# Create your models here.
class Blog(models.Model):
	"""个人博客"""
	name = models.CharField('博客名称', max_length=64, unique=True)
	user = models.CharField('用户名', max_length=64, unique=True)

	def __str__(self):
		return self.name


class Article(models.Model):
	"""文章表"""
	category_choices = ((1, '未分类'), (2, '技术'), (3, '杂谈'), (4, '感悟'),)

	title = models.CharField('文章标题', max_length=128, unique=True)
	category = models.IntegerField('文章分类', choices=category_choices, default=1)
	blog = models.ForeignKey('Blog', verbose_name='所属博客')
	content = models.TextField('文章内容')
	create_at = models.DateTimeField(auto_now_add=True, blank=True)

