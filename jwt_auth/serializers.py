from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_roll(self, roll):
        student = Student.objects.filter(roll = roll)
        if student.exists():
            raise serializers.ValidationError("Roll No. of every student should be unique!!")
        elif roll < 0 or roll > 200:
            raise serializers.ValidationError("Roll No. should be in range from 1 - 200!!")
        return roll