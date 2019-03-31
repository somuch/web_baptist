from django.conf.urls import patterns, url
from baptist import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^portal$', views.protal, name='portal'),
    url(r'^report_base$', views.report, name='report_base'),
    url(r'^reports_generate$', views.reports_generate, name='reports_generate'),
    url(r'^setting$', views.setting, name='setting'),
    url(r'^policies$', views.policies_check, name='policies'),
    url(r'^findPolicyByChurch$', views.find_policy_by_church, name='findpolicybychurch'),
    url(r'addPolicy/(?P<polTypeID>\d+)/(?P<churchID>\d+)/$', views.add_policy_by_policyIdNchurch),
    url(r'^updateSetting$',views.updateSetting, name='updateSetting'),
    
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)