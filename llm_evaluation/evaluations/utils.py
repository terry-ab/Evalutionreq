# evaluations/utils.py
import resend
from django.conf import settings

def send_email_notification(evaluation_id, recipient_email):
    """
    Send an email notification using the Resend API.
    """
    resend.api_key = settings.RESEND_API_KEY

    # Fetch the evaluation request
    from .models import EvaluationRequest
    evaluation = EvaluationRequest.objects.get(id=evaluation_id)

    # Prepare the email content
    subject = "Evaluation Completed"
    html_content = f"""
    <p>Your evaluation for the prompt <strong>{evaluation.input_prompt}</strong> is complete.</p>
    <p>Result: <strong>{evaluation.result}</strong></p>
    <p>Status: <strong>{evaluation.status}</strong></p>
    """

    # Send the email
    try:
        resend.Emails.send({
            "from": "terry_201610@yahoo.com",  # Replace with your verified Resend email
            "to": "lukekenny480@gmail.com",
            "subject": subject,
            "html": html_content,
        })
        print(f"Email sent to {'lukekenny480@gmail.com'} for evaluation {evaluation_id}.")
    except Exception as e:
        print(f"Failed to send email: {e}")