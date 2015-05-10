from django.views import generic
from . import models

# Create your views here.
class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "entry_list.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"