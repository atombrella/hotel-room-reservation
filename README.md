# Hotel room reservation app

Sample Django app to demo exclusion constraints and how Django works in general.

## How to install

It requires Python 3 and Docker (including docker-compose) to get everything running.
One of the powers of Django is that it's very easy to do local changes and see them live,
so for that purpose it's also possible to run just using docker for the database.

	docker-compose up -d

Or if you want to run it locally, you can run the ./setup.sh script, and then activate
the virtual environment to run this command to be able to run the Django commands.

    source venv/bin/activate

I left some bits and pieces that we'll go through.
