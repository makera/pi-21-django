from django.urls import path

from apps.courses.views import CourseDetailView, CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
