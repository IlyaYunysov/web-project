from django.conf.urls import url
import questions.views as question_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', question_views.question_list, name='question_list'),
    url(r'create/$', login_required(question_views.QuestionCreate.as_view()), name='question_create'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(question_views.QuestionEdit.as_view()), name='question_edit'),
    url(r'^(?P<pk>\d+)/$', question_views.question_detail, name='question_detail'),
]