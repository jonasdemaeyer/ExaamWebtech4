from django.contrib import admin
form django.urls import include, path

urlpatterns = [
	path('polls/', include('polls.urls')),
	path('admin/', admin.site.urls),
]
