.PHONY: build

launch: build run

build: init collectstatic migrate import dumpdata lint test

init:
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs

	rm -f db.sqlite3
	rm -f ./api/migrations/0001_initial.py

	PIPENV_VERBOSITY=-1  pipenv install --skip-lock
	PIPENV_VERBOSITY=-1  pipenv lock --requirements > requirements.txt


collectstatic:
	PIPENV_VERBOSITY=-1  pipenv run python manage.py collectstatic --noinput

migrate:
	PIPENV_VERBOSITY=-1  pipenv run python manage.py makemigrations -v 0
	PIPENV_VERBOSITY=-1  pipenv run python manage.py migrate -v 0

import:
	PIPENV_VERBOSITY=-1  pipenv run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bayhasworld.com', 'adminpass',first_name='admin',last_name='admin')"
	PIPENV_VERBOSITY=-1  pipenv run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('read-only', 'ro@bayhasworld.com', 'ropassword',first_name='read',last_name='only')"
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/publisher.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/bookformat.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/contributor.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/person.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/organization.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/gamesystem.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/game.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/book.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/workflow.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata -v 0 ./fixtures/token.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py populate_history -v 0 --auto

dumpdata:
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata -v 0 auth.User --indent 4 | grep -v Fetch > ./fixtures/users.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.contributor --indent 4 | grep -v Fetch > ./fixtures/contributor.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.organization --indent 4 | grep -v Fetch > ./fixtures/organization.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.person --indent 4 | grep -v Fetch > ./fixtures/person.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.gamesystem --indent 4 | grep -v Fetch > ./fixtures/gamesystem.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.publisher --indent 4 | grep -v Fetch > ./fixtures/publisher.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.bookformat --indent 4 | grep -v Fetch > ./fixtures/bookformat.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.book --indent 4 | grep -v Fetch > ./fixtures/book.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.game --indent 4 | grep -v Fetch > ./fixtures/game.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.workflow --indent 4 | grep -v Fetch > ./fixtures/workflow.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata authtoken.token --indent 4 | grep -v Fetch > ./fixtures/token.json

lint:
	PIPENV_VERBOSITY=-1  pipenv run pylint api --ignore=migrations,settings.py --disable=E0401,W0613,R0201,R0401,R0801,R0903

test:
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	PIPENV_VERBOSITY=-1  pipenv run coverage run --rcfile=.coveragerc --source='.' manage.py test api
	PIPENV_VERBOSITY=-1  pipenv run coverage html --rcfile=.coveragerc
	PIPENV_VERBOSITY=-1  pipenv run coverage report

run:
	PIPENV_VERBOSITY=-1  pipenv run python ./manage.py runserver --settings rpgtools.settings

travis-build:
	rm -f db.sqlite3
	rm -f ./api/migrations/0001_initial.py
	rm -f ./base/migrations/0001_initial.py
	rm -f ./ui/migrations/0001_initial.py
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	python manage.py collectstatic -v 0 --noinput
	python manage.py makemigrations -v 0
	python manage.py migrate -v 0
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bayhasworld.com', 'adminpass',first_name='admin',last_name='admin')"
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('read-only', 'ro@bayhasworld.com', 'ropassword',first_name='read',last_name='only')"
	python manage.py loaddata -v 0 ./fixtures/publisher.json
	python manage.py loaddata -v 0 ./fixtures/bookformat.json ./fixtures/contributor.json ./fixtures/person.json ./fixtures/organization.json ./fixtures/gamesystem.json ./fixtures/game.json ./fixtures/book.json ./fixtures/workflow.json ./fixtures/token.json
	python manage.py populate_history -v 0 --auto

travis-test:
	coverage run --rcfile=.coveragerc --source='.' manage.py test api -v 0
	coveralls

travis-lint:
	pylint api --ignore=migrations,settings.py --disable=E0401,W0613,R0201,R0401,R0801,R0903