.PHONY: build

launch: build run

build: init static migrate import dumpdata lint test

init:
	mkdir -p static
	mkdir -p fixtures
	mkdir -p logs
	rm -f db.sqlite3
	rm -f ./api/migrations/0001_initial.py
	python -m pip install -r  requirements.txt

static:
	python manage.py collectstatic --noinput

migrate:
	python manage.py makemigrations -v 0
	python manage.py migrate -v 0

import:
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bayhasworld.com', 'adminpass',first_name='admin',last_name='admin')"
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('read-only', 'ro@bayhasworld.com', 'ropassword',first_name='read',last_name='only')"
	python manage.py loaddata -v 0 ./fixtures/publisher.json
	python manage.py loaddata -v 0 ./fixtures/bookformat.json
	python manage.py loaddata -v 0 ./fixtures/contributor.json
	python manage.py loaddata -v 0 ./fixtures/person.json
	python manage.py loaddata -v 0 ./fixtures/organization.json
	python manage.py loaddata -v 0 ./fixtures/gamesystem.json
	python manage.py loaddata -v 0 ./fixtures/game.json
	python manage.py loaddata -v 0 ./fixtures/book.json
	python manage.py loaddata -v 0 ./fixtures/workflow.json
	python manage.py loaddata -v 0 ./fixtures/token.json
	python manage.py populate_history -v 0 --auto

dumpdata:
	python manage.py dumpdata -v 0 auth.User --indent 4 | grep -v Fetch > ./fixtures/users.json
	python manage.py dumpdata api.contributor --indent 4 | grep -v Fetch > ./fixtures/contributor.json
	python manage.py dumpdata api.organization --indent 4 | grep -v Fetch > ./fixtures/organization.json
	python manage.py dumpdata api.person --indent 4 | grep -v Fetch > ./fixtures/person.json
	python manage.py dumpdata api.gamesystem --indent 4 | grep -v Fetch > ./fixtures/gamesystem.json
	python manage.py dumpdata api.publisher --indent 4 | grep -v Fetch > ./fixtures/publisher.json
	python manage.py dumpdata api.bookformat --indent 4 | grep -v Fetch > ./fixtures/bookformat.json
	python manage.py dumpdata api.book --indent 4 | grep -v Fetch > ./fixtures/book.json
	python manage.py dumpdata api.game --indent 4 | grep -v Fetch > ./fixtures/game.json
	python manage.py dumpdata api.workflow --indent 4 | grep -v Fetch > ./fixtures/workflow.json
	python manage.py dumpdata authtoken.token --indent 4 | grep -v Fetch > ./fixtures/token.json

lint:
	pylint api --ignore=migrations,settings.py --disable=R0801,W0511

test:
	mkdir -p static
	mkdir -p fixtures
	mkdir -p logs
	coverage run --rcfile=.coveragerc --source='.' manage.py test api
	coverage html --rcfile=.coveragerc
	coverage report

coverage:
	xdg-open file:///home/mbayha/development/rpgtools-api/htmlcov/index.html

run:
	python ./manage.py runserver --settings rpgtools.settings
