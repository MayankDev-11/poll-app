from django.db import models



class Question(models.Model):
    question = models.CharField(max_length=50)
    image = models.ImageField(upload_to="photos/%Y/%M/%d")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    option_1 = models.CharField(max_length=25)
    option_2 = models.CharField(max_length=25)
    option_3 = models.CharField(max_length=25)
    option_4 = models.CharField(max_length=25)
    optionone_count = models.IntegerField(default=0)
    optiontwo_count = models.IntegerField(default=0)
    optionthree_count = models.IntegerField(default=0)
    optionfour_count = models.IntegerField(default=0)

    def total(self):
        return self.optionone_count + self.optiontwo_count + self.optionthree_count + self.optionfour_count


    def __str__(self):
        return self.question