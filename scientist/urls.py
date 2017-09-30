from django.conf.urls import url
from scientist import views

app_name='scientist'

urlpatterns = [
    # url(r'^$',views.index,name="index"),
    # url(r'^mailingaddress',views.mailingaddress,name='mailingaddress'),
    # url(r'^mailingaddress',views.UserMailingAddressUpdateView.as_view(),name='updateaddress'),
    url(r'^mailingaddress',views.ScientistMailingAddressListView.as_view(),name='list'),
    url(r'^create/$',views.ScientistMailingAddressCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.ScientistMailingAddressUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.ScientistMailingAddressDeleteView.as_view(),name='delete'),
    url(r'^addLetter',views.LettersCreateView.as_view(),name='add_letter'),
    url(r'^letters',views.LettersListView.as_view(),name='letter_list'),
    url(r'^updateletter/(?P<pk>\d+)/$',views.LettersUpdateView.as_view(),name="update_letter"),
    url(r'^students',views.StudentsListView.as_view(),name='students_list'),
    # url(r'^studentinfo',views.StudentInfo.as_view(),name='studentinfo'),

    # url(r'^scientist/',views.index,name="index"),
]
