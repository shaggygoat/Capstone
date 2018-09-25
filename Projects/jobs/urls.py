from django.urls import path
from . views import (JobPageView, JobDetailView,
                    JobCreateView, JobUpdateView,
                    JobDeleteView, UserJobPageView)
from . import views
urlpatterns = [

    path('', JobPageView.as_view(), name='sites-jobs'),
    path('<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('new/', JobCreateView.as_view(), name='job-create'),
    path('<str:username>/jobs', UserJobPageView.as_view(), name='user-jobs'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job-update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
]
