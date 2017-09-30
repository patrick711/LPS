from django.conf.urls import url
from teacher import views

app_name='teacher'

urlpatterns = [
 url(r'^letters',views.LettersListView.as_view(),name='tletter_list'),
 url(r'^addLetter',views.LettersCreateView.as_view(),name='add_letter'),
 url(r'^updateletter/(?P<pk>\d+)/$',views.LettersUpdateView.as_view(),name="update_letter"),
 url(r'^students',views.StudentsListView.as_view(),name='students_list'),
 url(r'^addStudent',views.StudentsCreateView.as_view(),name='add_student'),
]
