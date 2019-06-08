# ormucoTest

- [x] Display a form that accepts three fields as input: "Name", "Favorite Color", "Cats or Dogs". Ensure that "Name" is unique.
- [ ] Create an Ansible playbook to deploy it on a cloud
- [ ] Bonus points if the application can be easily scaled beyond a single server. More bonus points if the server is well secured (HTTPS, firewalls, etc).

# To run:
- `django` and `django-crispy-forms` must be installed
- Inside the `ormuco` directory run `manage.py` by writting: `python manage.py runserver`

## Install
In Python 3.7:
```
  pip install django django-crispy-forms
```

# References
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

https://www.guguweb.com/2017/05/02/how-to-deploy-a-django-project-in-15-minutes-with-ansible/
