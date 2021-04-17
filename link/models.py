from django.db import models

# Config for db length
_DEFAULT_CHAR_FIELD_LENGTH = 255
_DEFAULT_TEXT_FIELD_LENGTH = 1020


class TargetType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name = '对象类型'
        verbose_name_plural = '对象类型'


class Target(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH)
    type = models.ForeignKey(TargetType, null=True, on_delete=models.SET_NULL)
    parent_id = models.IntegerField(null=True, blank=True, default=-1)
    description = models.TextField(max_length=_DEFAULT_TEXT_FIELD_LENGTH, null=True)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name = '对象'
        verbose_name_plural = '对象'


class WebSiteType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH)
    source_url = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH, default="")
    can_format = models.BooleanField(default=False, null=False)
    format_template = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name = '站点类型'
        verbose_name_plural = '站点类型'


class WebSiteLink(models.Model):
    id = models.AutoField(primary_key=True)
    target_id = models.ForeignKey(Target, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH)
    type = models.ForeignKey(WebSiteType, null=True, blank=True, on_delete=models.SET_NULL)
    url = models.CharField(max_length=_DEFAULT_CHAR_FIELD_LENGTH)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name = '站点链接'
        verbose_name_plural = '站点链接'
