from django.conf.urls import url
from Coordinator import views

app_name='Coordinator'

urlpatterns = [
    url(r'^matched_students',views.MatchedStudentsListView.as_view(),name='students_list'),
    url(r'^unmatched_students',views.UnmatchedStudentsListView.as_view(),name='unmatched_students_list'),
    url(r'^update_students/(?P<pk>\d+)/$',views.MatchStudentsUpdateView.as_view(),name='update_students'),

    ]
