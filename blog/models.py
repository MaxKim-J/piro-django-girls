# blog.models


from django.db import models
from django.utils import timezone   # ??????????

# Create your models here.


class Post(models.Model):   # 모델 클래스의 속성은 필드의 구성을(db의 속성)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)   # 아예 처음부터 박아버리기
    # 어드민에서 보면 인스턴스 생성할 때 자동으로 들어가 있다
    published_date = models.DateTimeField(blank = True, null=True)

    def publish(self):  # 모델 클래스의 매서드는 행위를 정의
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title