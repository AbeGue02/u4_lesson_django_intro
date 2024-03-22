from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artist/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('song/', views.SongList.as_view(), name='song_list'),
    path('song/<int:pk>', views.SongDetail.as_view(), name='song_detail')
]