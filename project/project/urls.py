from django.contrib import admin
from django.urls import path
from csvapp.views import MetricsSearchView, LogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MetricsSearchView.as_view()),
    path('logs/', LogsView.as_view())
]


