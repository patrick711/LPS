from django.conf.urls import url
from Coordinator import views
#from Coordinator.views import people


app_name='Coordinator'

urlpatterns = [
    #url(r'^matched_students',views.MatchedStudentsListView.as_view(),name='students_list'),
    #url(r'^unmatched_students',views.UnmatchedStudentsListView.as_view(),name='unmatched_students_list'),
    #url(r'^unmatched_students',views.StudentListView.as_view(),name='unmatched_students_list'),
    #url(r'^studs',views.people,name='studs'),
    url(r'^students',views.FilteredStudentListView.as_view(),name='students'),
    url(r'^scientists',views.FilteredSciListView.as_view(),name='scientists'),
    #url(r'^update_students/(?P<pk>\d+)/$',views.MatchStudentsUpdateView.as_view(),name='update_students'),
    #url(r'^MakeMatch/(?P<pk>\d+)/$',views.MakeMatch.as_view(),name='MakeMatch'),
    url(r'^MakeMatch/(?P<scientist>\d+)/$',views.MakeMatch.as_view(),name='MakeMatch'),
    url(r'^Matches',views.FilteredMatches.as_view(),name='all_matches'),
    url(r'^DeleteMatch/(?P<pk>\d+)/$',views.DeleteMatch.as_view(),name='DeleteMatch'),
    ]
