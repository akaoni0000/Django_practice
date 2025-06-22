from django.db import models
from pathlib import Path#画像で使う
import uuid


class Page(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    title = models.CharField(max_length=100, verbose_name="タイトル")
    body = models.TextField(max_length=2000, verbose_name="本文")
    page_date = models.DateField(verbose_name="日付")
    picture = models.ImageField(
        upload_to="diary/picture/", blank=True, null=True, verbose_name="写真")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):#shellでPageオブジェクトの何かを出力するときに 下の値を返す
        #return self.title
        return f"{self.id} - {self.title}"
    
    def delete(self, *args, **kwargs):
        picture = self.picture
        super().delete(*args, **kwargs)
        if picture:
            Path(picture.path).unlink(missing_ok=True)


class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Good(models.Model):
    id = models.AutoField(primary_key=True)
    my_user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE,blank=True, null=True)
    page_id = models.ForeignKey(Page, on_delete=models.CASCADE,blank=True, null=True,)
    
