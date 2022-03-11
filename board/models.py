from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()        # not null
    modify_date = models.DateTimeField(null=True, blank=True) # null 허용, blank 폼 데이터
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') # user의 username와 외래키 설
    voter = models.ManyToManyField(User, related_name='voter_question')    # 추천수 - 다대다 관계

    def __str__(self):
        return self.subject

class Answer(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
