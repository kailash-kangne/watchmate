from django.urls import path, include
#from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewDetail, ReviewList,
                                     ReviewCreate,
                                     StreamPlatformDetailAV,
                                     StreamPlatformAV,
                                     WatchListAV, WatchDetailsAV)

# urlpatterns = [
#     path("list/", movie_list, name='movie-list'),
#     path("<int:pk>", movie_details, name='movie-details'),
# ]

urlpatterns = [
    path("list/", WatchListAV.as_view(), name='watch-list'),
    path("<int:pk>", WatchDetailsAV.as_view(), name='watch-details'),
    
    path("stream/", StreamPlatformAV.as_view(), name='stream'),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    path("stream/<int:pk>/review-create", ReviewCreate.as_view(), name='review-create'),
    path("stream/<int:pk>/review", ReviewList.as_view(), name='review-list'),
    path("stream/review/<int:pk>",ReviewDetail.as_view(), name='review-detail'),
    
    #path('review/',ReviewList.as_view(), name='review-list'),
    #path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail'),
    
        
]