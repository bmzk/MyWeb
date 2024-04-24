from django.db import models




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class City(models.Model):
    name_zh=models.CharField(max_length=200)
    name_en=models.CharField(max_length=200)
    lvl=models.IntegerField(default=0)
    input_time=models.DateTimeField("date input time")
    
