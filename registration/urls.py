from django.conf.urls import url
from registration import views

app_name='registration'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^formpage/',views.form_name_view,name="form_name"),
    url(r'^user_login',views.user_login,name="user_login"),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^register',views.register,name='register'),
]
