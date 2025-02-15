from django.urls import path
from .views import SubmitEvaluationRequest, RetrieveEvaluationRequest

urlpatterns = [
    path('evaluate', SubmitEvaluationRequest.as_view(), name='submit_evaluation'),
    path('evaluate/<int:id>/', RetrieveEvaluationRequest.as_view(), name='retrieve_evaluation'),
]