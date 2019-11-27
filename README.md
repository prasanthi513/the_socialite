# The Socialite

*The socialite can view what's currently happening in all his 3 social networking sites.
Facebook, Twitter and Instagram*

*The socialite can also view what's happening in each social site also*

###Set-Up
You are supposed to have an app created in all 3 social networking sites and get 
"user access token", "app id", "app secret key" for accessing facebook api
"user access token", "app id", "app secret key", "instagram account id" for accessing instagram api and 
consumer_api_keys, consumer_api_secret_key, access_token and access_secret_token for accessing twitter api.

### View all social feeds
**Definitions**

`GET /social_feeds `

**Responses**

```json
{
"fb":"status",
"twitter":"tweets",
"insta":"photos"
}
```

**Definitions**
`GET /social_feeds/fb `
**Responses**
- current status

**Definitions**
`GET /social_feeds/insta `
**Responses**
- all photos of User

**Definitions**
`GET /social_feeds/twitter `
**Responses**
- all tweets of user
