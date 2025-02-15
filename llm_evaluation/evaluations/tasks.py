import time
from celery import shared_task
from django.utils.timezone import now
from .models import EvaluationRequest
from django.conf import settings
import random
from .utils import send_email_notification

@shared_task
def process_evaluation_request(request_id):
    
    try:
        # Fetch the evaluation request
        evaluation = EvaluationRequest.objects.get(id=request_id)
        
        # Dummy sentiment analysis
        sentiments = ["positive", "negative", "neutral"]
        evaluation.result = f"Sentiment analysis result: {random.choice(sentiments)}"
        evaluation.status = "completed"
        evaluation.save()

        # Send email notification
        send_email_notification(request_id, "lukekenny480@gmail.com")
        print(f"Evaluation {request_id} processed successfully!")
    
    except EvaluationRequest.DoesNotExist:
        print(f"EvaluationRequest with id {request_id} not found.")
    
    except Exception as e:
        print(f"Error processing evaluation {request_id}: {e}")