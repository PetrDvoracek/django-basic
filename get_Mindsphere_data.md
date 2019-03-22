# !!!FLIPPED TO WIKI!!!
## Token

To be able to communicate with the Mindsphere api you need some kind of confirmation that you are logged in. For this purpose [Bearer token](https://swagger.io/docs/specification/authentication/bearer-authentication/) is used. [This part of documentation](https://developer.mindsphere.io/concepts/concept-authentication.html) deals with **getting** the token.

### How to get Bearer token using [Django](https://www.djangoproject.com/)

Everytime you want to use the token, you should get new token! following code should be in every view where you want to access the Mindsphere APIs
```
bearer_token = request.META['HTTP_AUTHORIZATION']
```
now the Bearer token should be in the **bearer_token** variable.

> **NOTE**: this works only if the web server runs on the Mindsphere. If you run it on your local machine ( `python manage.py runserver` ), the **bearer_token** variable will be Null

### How to use Bearer token to call Mindsphere APIs
Bearer token is used to authenticate when APIs call from backend. The API call from backend must be done thru **gateway**, the host should be in this format `gateway.{region}.mindsphere.io` (region=eu1, eu2, ...).
#### [Example](https://github.com/EasyHttp/EasyHttp/issues/47)
In this example we will call the assetmanagement API and we should get the assets. The HTTP request form is following
```http
GET /api/assetmanagement/v3/assets HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: gateway.eu1.mindsphere.io
User-Agent: HTTPie/0.9.8
authorization: Bearer {token}
```
The command using HTTPie
```
http GET https://gateway.eu1.mindsphere.io/api/assetmanagement/v3/assets "authorization:Bearer $token" -v --follow
```
The output should be 200 response and  JSON data (depends on the content of the asset manager).

#### HTTP  
Use [httpie](https://httpie.org/) or [postman](https://www.getpostman.com/) 
Useful Httpie [cheatsheet](https://devhints.io/httpie)
#####focus on [this](https://developer.mindsphere.io/howto/howto-simulation.html)
I struggle with assigning **mdsp:core:iot.timAdmin**, just try that without this role.
> **NOTE**: I got 500 error, maybe get the role, then try again.

#### Create request to get the data

Now it's the time for this part of [documentation](https://developer.mindsphere.io/apis/analytics-dataexchange/api-dataexchange-api-swagger-3-0-0.html) and little bit of [this](https://developer.mindsphere.io/frequently-used-links.html).
https://developer.mindsphere.io/concepts/concept-gateway-url-schemas.html
https://community.plm.automation.siemens.com/t5/Developer-Space/How-to-call-MindSphere-API-s-from-Application/td-p/522398

https://gateway.eu1.mindsphere.io/api/iottimeseries/v3/timeseries/7f03ff1dc93941e69c09dfc63389d43e/One?from=2019-01-31T12:44:46.196Z

```
http GET https://gateway.eu1.mindsphere.io/api/iottimeseries/v3/timeseries/7f03ff1dc93941e69c09dfc63389d43e/One "authorization:$token" from=="2019-01-31T12:44:46.196Z" -v --follow
```

## EntityId

[specified here](https://community.plm.automation.siemens.com/t5/Developer-Space/Agent-Management-API-where-to-find-Entity-ID/td-p/493887)
