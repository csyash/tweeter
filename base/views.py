from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tweet, Comments, CustomUser, Likes, Retweets, UserFollowing
from datetime import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def homePage(request):

    if request.method == 'POST':
        tweet_description = request.POST.get('tweet')
        if not request.user.is_anonymous:
            new_tweet = Tweet.objects.create(host=request.user,desciption=tweet_description)
            new_tweet.save()
        else:
            messages.error('Not Logged In pls log in first')
            return HttpResponseRedirect('login')


    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    tweets = Tweet.objects.all()
    #x = Tweet.objects.filter(request.user.followers.all().contains())
    #print(x)
    who_to_follow = CustomUser.objects.exclude(username=request.user.username).order_by('-date_joined')[:3]
    return render(request, "base/feed.html", {
        'tweets' : tweets,
        'wtf': who_to_follow
    })

def tweetPage(request,tweet_id):
    tweet = Tweet.objects.get(pk=tweet_id)
    curr_time = datetime.now()
    tweet_time_wo_tz = tweet.created.replace(tzinfo=None)
    who_to_follow = CustomUser.objects.exclude(username=request.user.username).order_by('-date_joined')[:3]
    comments = tweet.comments.all()
    return render(request, "base/tweet.html", {
        'tweet':tweet,
        'comments':comments,
        'wtf' : who_to_follow
    })

def loginPage(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homePage'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('homePage'))
        else:
            messages.error(request, 'Invalid Credentials')
            

    return render(request, 'base/login.html')

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def profilePage(request, username):
    try:
        user = CustomUser.objects.get(username=username)    
    except:
        messages.error(request, 'User does not exist')
        return HttpResponseRedirect(reverse('homePage'))
        
    tweets = user.tweets.all()
    who_to_follow = CustomUser.objects.exclude(username=request.user.username).order_by('-date_joined')[:3]
    
    return render(request, "base/profilePage.html", {
        'tweets' : tweets,
        'wtf':who_to_follow,
        'user':user
    })

def commentPage(request, tweet_id):
    if request.method == "POST":
        comment = request.POST.get('comment')
        comment_obj = Comments.objects.create(commenter=request.user, comment_description = comment, tweet = Tweet.objects.get(pk=tweet_id))
        comment_obj.save()
       

    return HttpResponseRedirect(reverse('tweet', args=(tweet_id,)))
    
@csrf_exempt
def likeHandler(request, tweet_id):
    if request.method == 'POST' and request.user.is_authenticated:
        tweet = Tweet.objects.get(pk=tweet_id)
         
        if not Likes.objects.filter(tweet=tweet, user = request.user):
           like = Likes.objects.create(tweet=tweet, user=request.user)
           like.save()
        else:
           messages.error(request,'Already Liked')  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
@csrf_exempt
def RTHandler(request, tweet_id):
    if request.method == 'POST' and request.user.is_authenticated:
        tweet = Tweet.objects.get(pk=tweet_id)
         
        if not Retweets.objects.filter(Tweet=tweet, user = request.user):
           retweet = Retweets.objects.create(Tweet=tweet, user=request.user)
           retweet.save()
        else:
           messages.error(request,'Already Retweeted')  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            user.save()
            
        except:
            pass
    
    return render(request, 'base/login.html')

@csrf_exempt
def followUser(request, username):
    user = request.user   
    follow = CustomUser.objects.get(username=username)
    x = UserFollowing.objects.create(user_who_is_following = user, user_who_is_getting_followed=follow)
    x.save()
    return HttpResponseRedirect(reverse('profilePage', args=(username,)))


@csrf_exempt
def unfollowUser(request, username):
    user = request.user   
    follow = CustomUser.objects.get(username=username)
    x = UserFollowing.objects.get(user_who_is_following = user, user_who_is_getting_followed=follow)
    x.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

