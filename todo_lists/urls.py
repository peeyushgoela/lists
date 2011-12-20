from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'todo_lists.views.index'),
                       url(r'^login', 'todo_lists.views.login'),
                       url(r'^signup', 'todo_lists.views.signup'),
                       url(r'^home', 'todo_lists.views.home'),
                       url(r'^logout', 'todo_lists.views.logout'),
                       url(r'^edit/(\d+)', 'todo_lists.views.edit'),
                       url(r'^delete_task/(\d+)', 'todo_lists.views.delete_task'),
                       url(r'^add_task', 'todo_lists.views.add_task'),
    # Examples:
    # url(r'^$', 'lists.views.home', name='home'),
    # url(r'^lists/', include('lists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
