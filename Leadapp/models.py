from django.db import models

# Create your models here.
class Lead(models.Model):
    source_choices=(
        ("walk-in","walk_in"),
        ("call","call"),
        ("referral","referral"),
        ("website","website")  
    )

    status_choices=(
            ("new","new"),
            ("contacted","contacted"),
            ("converted","converted"),
            ("lost","lost")  
        )
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    source=models.CharField(max_length=100,choices=source_choices)
    status=models.CharField(max_length=100,choices=status_choices)
    added_date=models.DateTimeField(auto_now=True)
    notes=models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return f"{self.name}-{self.phone}"

