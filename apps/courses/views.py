from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.courses.models import Course


class CourseListView(ListView):
    template_name = 'courses/list.html'
    model = Course

    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = super().get_queryset().filter(name__icontains=q or '')
        return qs


class CourseDetailView(DetailView):
    template_name = 'courses/detail.html'
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = Course.objects.filter(id__gt=self.get_object().id).first()
        context['prev'] = Course.objects.filter(id__lt=self.get_object().id).last()
        return context

# Create your views here.
