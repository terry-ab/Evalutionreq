from django.db import models
from django.utils import timezone


class EvaluationRequest(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('completed','Completed'),
    ]

    id = models.AutoField(primary_key= True)
    input_prompt= models.TextField()
    status= models.CharField(max_length= 10, choices=STATUS_CHOICES, default= 'pending')
    result= models.TextField(blank= True, null= True)
    created_at= models.DateTimeField(default= timezone.now)
    updated_at= models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"EvaluationRequest {self.id} - {self.status}"
