from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=32, verbose_name="菜单名")
    icon = models.CharField('图标', max_length=50)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """权限表
    有menu_id      二级菜单
    没有menu_id   普通的权限
    """
    url = models.CharField('url地址', max_length=100)
    name = models.CharField('url别名', max_length=50, unique=True)
    title = models.CharField('标题', max_length=32)
    weight = models.IntegerField('权重', null=True, blank=True)
    menu = models.ForeignKey('Menu', verbose_name='菜单', blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name='父权限', blank=True, null=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    """角色表"""
    name = models.CharField('角色名称', max_length=32)
    permissions = models.ManyToManyField('Permission', verbose_name='角色所拥有的权限', blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    """用户表"""
    # username = models.CharField('用户名', max_length=32)
    # password = models.CharField('密码', max_length=32)
    roles = models.ManyToManyField(Role, verbose_name='用户所拥有的角色', blank=True)

    class Meta:
        abstract = True
