from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import EvaluationRequest
from .serializers import EvaluationRequestSerializer
from .tasks import process_evaluation_request

#Submit Evaluation Request
class SubmitEvaluationRequest(APIView):

    def post(self, request):

        serializer = EvaluationRequestSerializer(data= request.data)
        if serializer.is_valid():
            eval_request= serializer.save(status= 'pending')

            #Trigger Celery task to process request
            process_evaluation_request.delay(eval_request.id)

            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#Retrive Evaluation Request
class RetrieveEvaluationRequest(APIView):

    def get(self, request, id):
        try:
            evaluation= EvaluationRequest.objects.get(id=id)
            serializer= EvaluationRequestSerializer(evaluation)
            return Response(serializer.data, status= status.HTTP_200_OK)
        except EvaluationRequest.DoesNotExist:
            return Response({'error: Evaluation request not found'}, status= status.HTTP_404_NOT_FOUND)