from django.urls import path

from apps.courses.views import CourseDetailView, CourseListView, call_back, CourseCreateView, CallbackFormView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('callback/', call_back, name='callback'),
    path('callback_form/', CallbackFormView.as_view(), name='callback_form'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
]
