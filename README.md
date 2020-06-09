# Hotel room reservation app

Sample Django app to demo [exclusion constraints](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-EXCLUSION) 
and how Django works in general. It's meant 
for a session at [Eficode Praqma](https://www.eficode.com) CodeCamp in June 2020. However, it's also
intended as a sample of how Django works in general, which covers the 
[admin site](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/), 
[templates](https://docs.djangoproject.com/en/3.0/topics/templates/), 
[models](https://docs.djangoproject.com/en/3.0/topics/db/models/),
as well as [django.contrib.postgres](https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/).

## How to install

It requires Python 3 and Docker (including docker-compose) to get everything running.
One of the powers of Django is that it's very easy to do local changes and see them live,
so for that purpose it's also possible to run just using docker for the database.

	docker-compose up -d

Or if you want to run it locally, you can run the ./setup.sh script, and then activate
the virtual environment to run this command to be able to run the Django commands.

    source venv/bin/activate

I left some bits and pieces that we'll go through, which are mostly left as comments 
in the code, e.g., nobody would probably book a hotel room without a description or
images.
