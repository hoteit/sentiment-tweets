# Sentiment Tweets usig Tweepy & Google NLP

Sentiment analysis of tweets using google cloud natural language api.
I showed this at the University of Texas at Dallas as part of my presentation 'AI & I at Work'. 

## Code setup instructions

Please note that you need to be familiar with Python, VirtualEnv, Django, and, to some extent Docker.

### setup the data model via Django 

1. setup your Python virtual environment, such as `virtualenv`, then activate your Python environment. 

2. install all the code requirements `pip install -r requirements.txt`

3. setup your Django project. How to setup Django is available at [Django website](https://www.djangoproject.com)

4. install PostGresQL and create the database. In my case, I ran Docker container for the database 

5. migrate the Django model, i.e. `manage.py makemigrations` followed by `manage.py migrate`.
 If you did not create a superuser already, make sure to do so `manage.py createsuperuser` because you need it 
 log in to the admin site. After all that is done start the server `manage.py runserver`

6. access the admin link at `127.0.0.1:8000/admin/`

Table **SearchKeywords** is where you would include keywords that you want to search for on Twitter. Just add some keyword and check the enable option.
The field *enabled* is useful if you want to keep the keywords in the database but you do not want to include them in your Tweeter streaming.

### setup the Twitter API 

1. you need to setup a Twitter dev account first at [https://developer.twitter.com](https://developer.twitter.com) followed by creating an application to enable read-only access to tweets.
Steps to create a Twitter application is available at [Twitter Getting Started](https://developer.twitter.com/en/docs/basics/getting-started) 

2. create a python configuration `sentiment/local_settings.py` and add the following


    consumer_key = "[INSERT THE CONSUMER_KEY FROM YOUR TWITTER DEV APP]"
    consumer_secret = "[INSERT THE CONSUME_SECRET FROM YOUR TWITTER DEV APP]"
    access_token = "[INSERT THE ACCESS TOKEN FROM YOUR TWITTER DEV APP]"
    access_token_secret = "[INSERT THE ACCESS TOKEN SECRET FROM YOUR TWITTER DEV APP]"
    tweets_max_per_sample = 10 <- number of tweets each time you run or rerun your app
    tweets_polling_time = 10  <- time in seconds for polling Twitter 



### setup Google Cloud NLP for sentiment analysis 

1. Set up a [Google Cloud](http://cloud.google.com) and activate [Google Natural Language API](https://console.cloud.google.com/apis/library/language.googleapis.com)
2. Set up the Google Cloud Natural Language API at [https://cloud.google.com/natural-language/docs/quickstart-client-libraries]. You can also try their [Quick Start](https://cloud.google.com/natural-language/docs/quickstart-client-libraries)
3. Make sure that you set the environment variable GOOGLE_APPLICATION_CREDENTIALS in your machine ([read here](https://cloud.google.com/natural-language/docs/quickstart-client-libraries))


## run the code

- make sure you are at your project root and have your Python virtual environment activated
- to capture tweets run the following command `./manage.py script tweets_collector` 
- to run sentiment analysis over your collected data `../manage.py scrupt sentiment_analyzer` 


Note: this code works but is not perfectly complete... there are lots of things that are missing such as created views and a nice looking website. 
But it is also a great place for starters to play around with various code and try different things. Enjoy!

Thanks,
Tarek 
