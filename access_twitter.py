import twitter

consumer_api_keys = "xxx" #incorrect one
consumer_api_secret_key = "xxx"
access_token = "xxx"
access_secret_token = "xxx"

def get_twitter_timeline():
    api = twitter.Api(consumer_key = consumer_api_keys,
                        consumer_secret = consumer_api_secret_key,
                        access_token_key = access_token,
                        access_token_secret = access_secret_token)

    try:
        api.VerifyCredentials()
    except twitter.error.TwitterError as t_error:
        return str(t_error)
    else:
        return str(api.GetUserTimeline())

if __name__ == '__main__':
    print(get_twitter_timeline())
