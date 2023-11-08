from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView

from apps.courses.forms import CallbackForm
from apps.courses.models import Course, Callback


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


class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/create.html'
    fields = ['name', 'date_start']

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.object.id})


class CallbackFormView(FormView):
    form_class = CallbackForm
    template_name = 'courses/callback_form.html'

    def get_success_url(self):
        return reverse('callback_form')

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)



def call_back(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'courses/call_back.html')
    data = request.POST.copy()
    data.pop('csrfmiddlewaretoken')
    # item = Callback.objects.create(**data.dict())
    item = Callback(**data.dict())
    item.save()
    return render(request, 'courses/call_back.html', context={'item': item})

# Create your views here.
