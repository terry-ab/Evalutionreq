from rest_framework import serializers
from .models import EvaluationRequest

class EvaluationRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= EvaluationRequest
        fields= ['id', 'input_prompt', 'status', 'result', 'created_at', 'updated_at']