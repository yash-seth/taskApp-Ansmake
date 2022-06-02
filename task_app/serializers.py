from rest_framework import serializers 
from task_app.models import Task
 
 
class TaskSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Task
        fields = ('id',
                  'name',
                  'description',
                  'email',
                  'created_at')