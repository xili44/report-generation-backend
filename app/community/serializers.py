from rest_framework import serializers
from community.models import Post, Comment, Patient, Pharmacogenomics, Genome

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'post')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class PharmacogenomicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacogenomics
        fields = "__all__"

class GenomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genome
        fields = '__all__'