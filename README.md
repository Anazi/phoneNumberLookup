### Installation and Running Server
#### Virtual Environment
Assuming that python(3.7+) is already installed.
1. Change Dir to project dir - `cd /path/to/phoneNumberLookup`
2. Use - `python[version] -m venv /path/to/new/virtual/(eg.; python3.8 -m venv .venv)` to create virtual environment. 
3. Use - `source .venv/bin/activate` to activate the venv 
4. Use - `pip install -r requirements.txt` to install all lib dependencies.

#### Server Prep and Startup
1. Change Dir to project dir - `cd /path/to/phoneNumberLookup`
2. Use - `python manage.py makemigrations v1` to setup migrations on the system.
3. Use - `python manage.py migrate` to implement migrations.
4. Use - `python manage.py runserver` to run the server.

#### Automated Testing
1. Open a new terminal tab 
2. Change Dir to project dir - `cd /path/to/phoneNumberLookup`
3. Run `./manage.py test --pattern="test*.py" -v 2` to run all the available tests.

### Choice of programming language, framework, library
#### Programming Language
1. Easy and readable with good portability and interactivity.
2. OOP and Asynchronous coding.
3. Rich Standard Library and ecosystem.
4. Good software testing and Prototyping.

#### Framework(Django Framework) and Library
1. Low coupling and Rapid Development.
2. KISS(Keep It Short and Simple) and DRY(Don’t Repeat Yourself) compliant.
3. REST framework with good testing and debugging support. 
4. A lot of tools and utilities that add to the building of complex web applications.
5. Pycountry - Easier solution for country code validation


### Production Deployment
Considering the app would see a good amount of traffic, we would need to scale 
the app.

For this purpose, I would choose to deploy on Kubernetes so that new pods 
can easily be spun and would dockerize the app for easier deployment.

Deployment will be managed by Spinnaker and GoCD SaaS.

### Assumptions Made
Assuming that the app is only for testing purpose, I have used:
1. A light weight relational dB - sqlite
2. A host on `http://127.0.0.1:8000/`

### Improvement(s)
Can replace rest_framework exception handling(ApiException) with a custom exception handler.
