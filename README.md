# The Socialite

*The socialite can view what's currently happening in all his 3 social networking sites.
Facebook, Twitter and Instagram*

*The socialite can also view what's happening in each social site also*

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
