import requests
import pyfacebook

app_id = "xxx"
app_id = "xxx"
app_secret = "xxx"
access_token = "xxx"

def get_facebook_status():
    try:
        api = pyfacebook.Api(app_id = app_id,
                            app_secret = app_secret,
                            short_token = access_token)
        status = "https://graph.facebook.com/v5.0/me/posts?access_token="+access_token
        api.get_token_info()
    except pyfacebook.error.PyFacebookError as f_error:
        return str(f_error)
    else:
        status_resp = requests.get(status)
        return str(status_resp.text)

if __name__ == '__main__':
    print(get_facebook_status())
