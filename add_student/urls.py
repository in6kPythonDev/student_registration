from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^add_student/show_students', 'add_student.student_form.views.show_students'),
    url(r'^add_student/(?P<student_id>\d+)/student_form', 'add_student.student_form.views.edit'),
    url(r'^add_student/student_form', 'add_student.student_form.views.edit'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)