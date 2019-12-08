.PHONY: build

build-dev:
	pipenv lock --requirements > requirements.txt
	rm -f ./api/migrations/0001_initial.py
	rm -f ./base/migrations/0001_initial.py
	rm -f ./ui/migrations/0001_initial.py

	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	pipenv run python manage.py collectstatic --noinput
	psql -h localhost -U postgres -c 'DROP database IF EXISTS rpgtools';
	psql -h localhost -U postgres -c 'CREATE database rpgtools';
	pipenv run python manage.py makemigrations
	pipenv run python manage.py migrate
	pipenv run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bayhasworld.com', 'adminpass',first_name='admin',last_name='admin')"
	pipenv run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('read-only', 'ro@bayhasworld.com', 'ropassword',first_name='read',last_name='only')"
	pipenv run python manage.py loaddata ./fixtures/publisher.json
	pipenv run python manage.py loaddata ./fixtures/bookformat.json
	pipenv run python manage.py loaddata ./fixtures/schema.json
	pipenv run python manage.py loaddata ./fixtures/contributor.json
	pipenv run python manage.py loaddata ./fixtures/person.json
	pipenv run python manage.py loaddata ./fixtures/organization.json
	pipenv run python manage.py loaddata ./fixtures/gamesystem.json
	pipenv run python manage.py loaddata ./fixtures/game.json
	pipenv run python manage.py loaddata ./fixtures/book.json
	pipenv run python manage.py loaddata ./fixtures/handler.json
	pipenv run python manage.py loaddata ./fixtures/action.json
	# pipenv run python manage.py loaddata ./fixtures/workflow.json
	pipenv run python manage.py loaddata ./fixtures/token.json
	pipenv run python manage.py populate_history --auto
	pipenv run python manage.py dumpdata auth.User --indent 4 | grep -v Fetch > ./fixtures/users.json

collectstatic:
	pipenv run python manage.py collectstatic --noinput

delete-db:
	psql -h localhost -U postgres -c 'DROP database IF EXISTS rpgtools';

dumpdata:
	pipenv run python manage.py dumpdata api.contributor --indent 4 | grep -v Fetch > ./fixtures/contributor.json
	pipenv run python manage.py dumpdata api.organization --indent 4 | grep -v Fetch > ./fixtures/organization.json
	pipenv run python manage.py dumpdata api.person --indent 4 | grep -v Fetch > ./fixtures/person.json
	pipenv run python manage.py dumpdata api.gamesystem --indent 4 | grep -v Fetch > ./fixtures/gamesystem.json
	pipenv run python manage.py dumpdata api.publisher --indent 4 | grep -v Fetch > ./fixtures/publisher.json
	pipenv run python manage.py dumpdata api.bookformat --indent 4 | grep -v Fetch > ./fixtures/bookformat.json
	pipenv run python manage.py dumpdata api.book --indent 4 | grep -v Fetch > ./fixtures/book.json
	pipenv run python manage.py dumpdata api.game --indent 4 | grep -v Fetch > ./fixtures/game.json
	pipenv run python manage.py dumpdata api.schema --indent 4 | grep -v Fetch > ./fixtures/schema.json
	pipenv run python manage.py dumpdata api.handler --indent 4 | grep -v Fetch > ./fixtures/handler.json
	pipenv run python manage.py dumpdata api.action --indent 4 | grep -v Fetch > ./fixtures/action.json
	pipenv run python manage.py dumpdata api.workflow --indent 4 | grep -v Fetch > ./fixtures/workflow.json
	pipenv run python manage.py dumpdata authtoken.token --indent 4 | grep -v Fetch > ./fixtures/token.json

init:
	pipenv install --skip-lock

lint:
	pipenv run pylint * --ignore=manage.py,Makefile,LICENSE,Pipfile,Pipfile.lock,README.md,requirements.txt,settings.py,settings_dev.py,wsgi.py,migrations,schemas --disable=R0801

run:
	pipenv run python ./manage.py runserver --settings rpgtools.settings

run-dev:
	pipenv run python ./manage.py runserver 0.0.0.0:8000 --settings rpgtools.settings_dev

setup-db:
	psql -h localhost -U postgres -c "CREATE USER rpgtools_admin with PASSWORD 'Gerrit8684!';"
	psql -h localhost -U postgres -c 'ALTER USER rpgtools_admin WITH SUPERUSER;'
	psql -h localhost -U postgres -c 'DROP database IF EXISTS rpgtools';
	psql -h localhost -U postgres -c 'CREATE database rpgtools';
