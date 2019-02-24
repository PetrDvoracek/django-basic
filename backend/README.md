>**NOTE**: Can I access this service by the name in the manifes.yml?

# django-basic
Basic web application developed using Django framework and deployed in the Minsphere environment.

## Getting started

These instructions will get you a copy of the project up and running on your local **Linux** machine for development purposes. See deployment for notes on how to deploy the project on a Mindsphere.

### Prerequisites

The best practices is working in so called **virtual environment**, lets create one! First intall `virtualenv` using **pip**, which is the Python's package manager.
```
sudo pip install virtualenv
```
Now you should be able to create new Python **virtual environment** called *venv3* (choose whatever name you want). *~/Venvs* stands for the folder, where all virtual environments are located. This is just my system, you can create new venv anywhere.
```
mkdir ~/Venvs
virtualenv -p python3 ~/Venvs/venv3
```
Next step is to activate the venv. Run `source ~/Venvs/venv3/bin/activate` for activate the venv and `deactivate` for exit venv.
Now install crutial packages for developing an aplication.

```
pip install django
```

Great, You are ready for developing web applications using Python and Django!
Another best practice is creating `requirements.txt` folder, which contains all the packages needed to run the app. With virtual environment it is super easy! 

```
pip freeze > requirements.txt
```

Boom! Now anybody can install all the dependencies running this 

```
pip install -r requirements.txt
```

>**NOTE**: You must do this for propper deploying app on Mindsphere!

Now install the git into your **Linux** system so you will be able to download this project easily! You can do thi sing package manager (on Debian distr. it is **apt-get**)

```
sudo apt-get install git
```

### Installing

Just clone the repository into your local **Linux**

```
git clone https://github.com/PetrDvoracek/django-basic.git 
```

This will download all the stuff in the folder where you are located. Now install all the python packages crutial for this app

```
cd django-basic
pip install -r requirements.txt
```
Great! 


## Deployment on Mindsphere

For deploying the application the [Cloud Foundry](https://www.cloudfoundry.org/) is used. Yo will be able to install it using **apt-get** by adding the Cloud Foundry Foundation public key and package repository to your system

```
wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | sudo apt-key add -
echo "deb https://packages.cloudfoundry.org/debian stable main" | sudo tee /etc/apt/sources.list.d/cloudfoundry-cli.list
sudo apt-get update
sudo apt-get install cf-cli
```
Just check propper instalation by `cf -v`, you should see something like `cf version 6.42.0+0cba12168.2019-01-10` depending 
on the version of cf. Now log in
```
cf login -a https://api.cf.eu1.mindsphere.io --sso
```
>**NOTE** log in https://login.cf.eu1.mindsphere.io/passcode and copy-paste the code into the console.

You should see something like
```
OK

Targeted org vsbfei01

Targeted space spaceFei


                
API endpoint:   https://api.cf.eu1.mindsphere.io (API version: 2.128.0)
User:           petr.dvoracek@vsb.cz
Org:            vsbfei01
Space:          spaceFei
```
If the Org and Space are empty, contact the admin of your organization, he will add you with ([find more](https://docs.cloudfoundry.org/adminguide/cli-user-management.html))
```
cf set-org-role <user@mail.net> <organization_name> OrgManager
```
Now, to deploy the application to Mindsphere 
```
cf push
```
Congratulations! If this action ends with following lines, you have successfully uploaded your first application to Mindsphere!
```
name:              hello-django
requested state:   started
routes:            hello-django.apps.eu1.mindsphere.io
last uploaded:     Sun 10 Feb 19:34:15 CET 2019
stack:             cflinuxfs2
buildpacks:        python

type:            web
instances:       1/1
memory usage:    512M
start command:   python manage.py runserver --insecure 0.0.0.0:$PORT
     state     since                  cpu    memory          disk             details
#0   running   2019-02-10T18:34:28Z   1.9%   28.5M of 512M   388.1M of 512M   
```
