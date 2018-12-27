from django.conf.urls import url
from django.contrib import admin
from blog_app.views import Login, Register, ResetPassword, Home, AddTopic, ShowTopic, AddMessage, Logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^register$', Register.as_view(), name='register'),
    url(r'^reset_password$', ResetPassword.as_view(), name='reset_password'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^show_topic/(?P<topic_id>(\d)+)$', ShowTopic.as_view(), name='show_topic'),
    url(r'^add_topic$', AddTopic.as_view(), name='add_topic'),
    url(r'^add_message/(?P<topic_id>(\d)+)$', AddMessage.as_view(), name='add_message'),
]
