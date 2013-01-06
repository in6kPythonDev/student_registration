from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^student_registration/show_students', 'student_registration.student_form.views.show_students'),
    url(r'^student_registration/(?P<student_id>\d+)/student_form', 'student_registration.student_form.views.edit'),
    url(r'^student_registration/student_form', 'student_registration.student_form.views.edit'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)