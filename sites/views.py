from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.db.models import Sum
from django.http import JsonResponse
from django.urls import reverse
from .models import Site, Rating
from .forms import SiteForm

# Create your views here.
 
class SiteCreateView(CreateView):
    model = Site
    template_name = 'add_site.html'
    fields = ('cover','title','link','description','tags')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SiteListView(ListView):
    model = Site
    template_name = 'home.html'


class SiteDetailView(DetailView):
    model = Site
    template_name= 'site.html'
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        site = Site.objects.get(id=self.object.id)
        count = len(site.rating.all())
        if count > 0:
            content = (site.rating.all().aggregate(Sum('content')).get('content__sum'))/count * 10
            design = (site.rating.all().aggregate(Sum('design')).get('design__sum'))/count *10
            usability = (site.rating.all().aggregate(Sum('usability')).get('usability__sum'))/count *10
            context["content"] = int(content)
            context["design"] = int(design)
            context["usability"] = int(usability)
        else:
            context["content"] = 0
            context["design"] = 0
            context["usability"] = 0
        return context


class SiteUpdateView(UpdateView):
    model = Site
    template_name = 'edit_site.html'
    fields = ('cover', 'title', 'link', 'description', 'tags')


def vote(request):
    design = request.POST.get('design_range')
    content = request.POST.get('content_range')
    usability = request.POST.get('usability_range')
    site_id = request.POST.get('site_id')

    site = Site.objects.get(id=site_id)
    if len(Rating.objects.filter(author=request.user, site=site)) == 0:
        rating = Rating(design=design, usability=usability, content=content, site=site, author=request.user)
        rating.save()
        data = {'success': 'Thank you for voting for us!'}
    else:
        data = {'success':'Sorry, You can only vote once!'}
    return JsonResponse(data)


class ApiView(TemplateView):
    template_name = 'apis.html'