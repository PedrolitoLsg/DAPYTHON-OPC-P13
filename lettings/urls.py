from django.urls import path
from .views import letting, index


urlpatterns = [
    path('lettings/', index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting')
]
