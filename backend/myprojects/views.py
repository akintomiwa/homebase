from django.shortcuts import render, get_object_or_404
from .models import Project
from django.views.generic import DetailView
from rest_framework import viewsets
from .serializers import ProjectSerializer

# Create your views here.
def homepage(request):
    projs = Project.objects
    return render(request, 'myprojects/home.html', {'projects': projs})
    # return render(request, 'myprojects/home.html')

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    return render(request, 'myprojects/project_detail.html', {'project': project_detail})

# class version of the above function

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'myprojects/projectdetail.html'
    context_object_name = 'project'
    # queryset = Project.objects.all()
    # slug_field = 'title'
    # slug_url_kwarg = 'title'
    # pk_url_kwarg = 'project_id'
    # def get_object(self):
    #     id_ = self.kwargs.get("project_id")
    #     return get_object_or_404(Project, id=id_)



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer