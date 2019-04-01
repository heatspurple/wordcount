from django.db import models

# Create your models here.
# 어떤 종류의 데이터를 처리하고 싶은지 쓰는것

class Blog(models.Model):
    title = models.CharField(max_length=200)
    #title을 model안에있는 200자 내의 charfield(제목같이 짧은것 문자로 되어있는 데이터)로 정의하겠다.
    pub_date = models.DateTimeField('date published')
    #이 변수 안에서는 datetimefield(날짜와 시간을 나타내는 필드)
    body = models.TextField()
    #같은 형식인데 TextField는 좀 긴 문자열
    def __str__(self):
        return self.title
    # Blog내에 글 목록이 blog object가 아니라 글 제목으로 원할 때

    #데이터베이스에 있는 파일

