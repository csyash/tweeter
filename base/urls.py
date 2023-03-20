from django.urls import path
from . import views
urlpatterns = [
      # Login and Registration
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('reg', views.reg, name='reg'),
    
    path('', views.homePage, name='homePage'),
    path('tweet/<int:tweet_id>', views.tweetPage, name='tweet'),
    path('tweet/<int:tweet_id>/comment',views.commentPage, name="comment"),
    path('tweet/<int:tweet_id>/like',views.likeHandler, name="like"),
    path('tweet/<int:tweet_id>/retweet',views.RTHandler, name="retweet"),

    path('<str:username>', views.profilePage, name='profilePage'),
    path('<str:username>/follow', views.followUser, name='follow'),
    path('<str:username>/unfollow', views.unfollowUser, name='unfollow'),
]