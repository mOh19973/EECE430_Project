from django.db import models


class TDModel(models.Model):
    username = models.CharField(max_length=20)
    carName = models.CharField(max_length=20)
    day = models.IntegerField(max_length=20)
    month = models.IntegerField(max_length=20)
    year = models.IntegerField(max_length=20)
    hour = models.IntegerField(max_length=20)
    minutes = models.IntegerField(max_length=20)

    def __str__(self):
        return self.username + '-' + self.carName #+ ' - ' + str(self.day) + ' - ' + str(self.month) +' - ' \
              # + str(self.year) + ' - ' + str(self.hour) + ' - ' + str(self.minutes)


 #   def get_absolute_url(self):
 #       return reverse('cars:detail', kwargs={'pk': self.pk})

