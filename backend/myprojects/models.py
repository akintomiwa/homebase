from django.db import models
from .myprojects_utils import ProjectState

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    summary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imgs/')
    url = models.URLField()
    github = models.URLField()
    # type = models.CharField(max_length=20)
    # state = ProjectState(initial = 'not_live', states = ProjectState.states, transitions = ProjectState.transitions)
    
    def __str__(self):
        return self.title
    
