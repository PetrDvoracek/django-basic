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
TODO
#### Create HTTP request in Django

use [HTTPie](https://httpie.org/) for learn how the HTTP works. I have tried many ways how to connect to Mindsphere but I was not successfull, the problem was in the token and with login.

> **NOTE**: [1](https://developer.mindsphere.io/howto/howto-agent-access-token.html) [2](https://developer.mindsphere.io/concepts/concept-authentication.html) does not work for me.


#### Create request to get the data

Now it's the time for this part of [documentation](https://developer.mindsphere.io/apis/analytics-dataexchange/api-dataexchange-api-swagger-3-0-0.html) and little bit of [this](https://developer.mindsphere.io/frequently-used-links.html).