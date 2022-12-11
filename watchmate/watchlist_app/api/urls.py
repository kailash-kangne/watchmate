from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import StreamPlatformDetailAV, StreamPlatformAV, WatchListAV, WatchDetailsAV

# urlpatterns = [
#     path("list/", movie_list, name='movie-list'),
#     path("<int:pk>", movie_details, name='movie-details'),
# ]

urlpatterns = [
    path("list/", WatchListAV.as_view(), name='watch-list'),
    path("<int:pk>", WatchDetailsAV.as_view(), name='watch-details'),
    path("stream/", StreamPlatformAV.as_view(), name='stream'),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
]