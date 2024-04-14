import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
#1:다 의 관게라고 생각해야함. 질문 하나의 여러개의 선택이니까
#데이터 베이스 내용은 질문과 선택
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.question_text
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  #저위에 질문 테이블에 질문이 제거되면 얘도 같이 제거된다는 뜻
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
