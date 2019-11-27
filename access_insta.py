import requests
import pyfacebook

app_id = "xxx"
app_secret = "xxx"
access_token = "xxx"
insta_id = "xxx"

def get_insta_photos():
    try:
        api = pyfacebook.InstagramApi(app_id = app_id,
                            app_secret = app_secret,
                            short_token = access_token,
                            instagram_business_id = insta_id)
        photos = "https://graph.facebook.com/v5.0/me/photos?access_token="+access_token
        api.get_token_info()
    except pyfacebook.error.PyFacebookError as f_error:
        return str(f_error)
    else:
        photos_resp = requests.get(photos)
        return str(photos_resp.text)


if __name__ == '__main__':
    print(get_insta_photos())
