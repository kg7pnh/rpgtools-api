.PHONY: build

launch: build run

build: init collectstatic migrate import dumpdata lint test

init:
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	rm -f db.sqlite3
	rm -f ./api/migrations/0001_initial.py
	pip install -r  requirements.txt

collectstatic:
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
	pylint api --ignore=migrations,settings.py --disable=E0401,W0613,R0201,R0401,R0801,R0903

test:
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	coverage run --rcfile=.coveragerc --source='.' manage.py test api
	coverage html --rcfile=.coveragerc
	coverage report

coverage:
	xdg-open file:///home/mbayha/development/rpgtools-api/htmlcov/index.html

run:
	python ./manage.py runserver --settings rpgtools.settings

# travis-build:
# 	rm -f db.sqlite3
# 	rm -f ./api/migrations/0001_initial.py
# 	rm -f ./base/migrations/0001_initial.py
# 	rm -f ./ui/migrations/0001_initial.py
# 	mkdir -p ui/static
# 	mkdir -p fixtures
# 	mkdir -p logs
# 	python manage.py collectstatic -v 0 --noinput
# 	python manage.py makemigrations -v 0
# 	python manage.py migrate -v 0
# 	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bayhasworld.com', 'adminpass',first_name='admin',last_name='admin')"
# 	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('read-only', 'ro@bayhasworld.com', 'ropassword',first_name='read',last_name='only')"
# 	python manage.py loaddata -v 0 ./fixtures/publisher.json
# 	python manage.py loaddata -v 0 ./fixtures/bookformat.json ./fixtures/contributor.json ./fixtures/person.json ./fixtures/organization.json ./fixtures/gamesystem.json ./fixtures/game.json ./fixtures/book.json ./fixtures/workflow.json ./fixtures/token.json
# 	python manage.py populate_history -v 0 --auto

# travis-test:
# 	coverage run --rcfile=.coveragerc --source='.' manage.py test api -v 0
# 	coveralls

# travis-lint:
# 	pylint api --ignore=migrations,settings.py --disable=E0401,W0613,R0201,R0401,R0801,R0903
