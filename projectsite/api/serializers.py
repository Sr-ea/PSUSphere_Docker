from rest_framework import serializers
from studentorg.models import College, Program, Student, Organization, OrgMember

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    college_name = serializers.CharField(source='college.college_name', read_only=True)
    
    class Meta:
        model = Program
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.prog_name', read_only=True)
    college_name = serializers.CharField(source='program.college.college_name', read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    college_name = serializers.CharField(source='college.college_name', read_only=True)
    
    class Meta:
        model = Organization
        fields = '__all__'

class OrgMemberSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.__str__', read_only=True)
    organization_name = serializers.CharField(source='organization.name', read_only=True)
    
    class Meta:
        model = OrgMember
        fields = '__all__'