from django.db import models

class Movies(models.Model):
        cht_name = models.TextField()
        eng_name = models.TextField()
        expectation = models.TextField()
        poster_url = models.URLField()
        release_date  = models.DateTimeField()

        class Meta:
           db_table = "movies"
        
        def __str__(self):
            return self.cht_name