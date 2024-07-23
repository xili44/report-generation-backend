from rest_framework import viewsets
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
# Import the Post and Comment models
from community.models import Post, Comment, Patient, Pharmacogenomics, Genome

# Import the Post and Comment serializers
from community.serializers import PostSerializer, CommentSerializer, PatientSerializer, PharmacogenomicsSerializer, GenomeSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class PatientViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
class GenomeViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        field_names = [field.name for field in Genome._meta.get_fields()]
        print(field_names)
        genes = []
        for field in field_names:
            if field == 'id':
                continue
            if getattr(instance, field):
                genes.append(field)
        return Response({"detectedGenes": genes}, status=status.HTTP_200_OK)

class PharmacogenomicsViewSet(viewsets.GenericViewSet):
    queryset = Pharmacogenomics.objects.all()
    serializer_class = PharmacogenomicsSerializer
    
    @action(detail=False, methods=["post"], url_path="get-pharmacogenomics-from-genome")
    def get_pharmacogenomics_from_genome(self, request):
        detected_genes = request.data.get('detectedGenes', [])
        result_set = self.queryset.filter(gene__in=detected_genes)
        try:
            serializer = self.serializer_class(result_set, many=True)
            print(serializer.data)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)