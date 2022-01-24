from django.db import models

# Create your models here.
class Good(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    imgs = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)
    mood1 = models.CharField(max_length=200)
    mood2 = models.CharField(max_length=200)
    mood3 = models.CharField(max_length=200)

class Board(models.Model):
    title = models.CharField(max_length=200) # 게시글 제목
    content = models.CharField(max_length=500) # 게시글 내용
    writer = models.CharField(max_length=200) # 게시글 작성자
    registered_date = models.DateTimeField() # 게시글 작성시간
    comment = models.CharField(max_length=200) # 게시글에 달린 댓글
    like = models.IntegerField() # 게시글 좋아요
    img = models.CharField(max_length=200)  # 게시글 사진 파일 이름

    # @property
    # def created_string(self):
    #     time = datetime.now(tz=timezone.utc) - self.registered_date
    #
    #     if time < timedelta(minutes=1):
    #         return '방금 전'
    #     elif time < timedelta(hours=1):
    #         return str(int(time.seconds / 60)) + '분 전'
    #     elif time < timedelta(days=1):
    #         return str(int(time.seconds / 3600)) + '시간 전'
    #     elif time < timedelta(days=7):
    #         time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
    #         return str(time.days) + '일 전'
    #     else:
    #         return False

class Comment(models.Model):
    bid = models.IntegerField()
    content = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)


class Interior_obj(models.Model):
    category = models.CharField(max_length=20)
    obj_name = models.CharField(max_length=50)
    detail_link = models.CharField(max_length=200)
    minimal = models.IntegerField()
    modern = models.IntegerField()
    vintage = models.IntegerField()
    natural = models.IntegerField()
    individuality = models.IntegerField()
    romantic = models.IntegerField()
    casual = models.IntegerField()
    useful = models.IntegerField()
    enfj = models.FloatField()
    enfp = models.FloatField()
    entj = models.FloatField()
    entp = models.FloatField()
    esfj = models.FloatField()
    esfp = models.FloatField()
    estj = models.FloatField()
    estp = models.FloatField()
    infj = models.FloatField()
    infp = models.FloatField()
    intj = models.FloatField()
    intp = models.FloatField()
    isfj = models.FloatField()
    isfp = models.FloatField()
    istj = models.FloatField()
    istp = models.FloatField()
    like = models.IntegerField()
    photo_link = models.CharField(max_length=200)
