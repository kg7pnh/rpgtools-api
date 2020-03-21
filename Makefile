.PHONY: build

build:
	PIPENV_VERBOSITY=-1  pipenv lock --requirements > requirements.txt
	rm -f db.sqlite3
	rm -f ./api/migrations/0001_initial.py
	rm -f ./base/migrations/0001_initial.py
	rm -f ./ui/migrations/0001_initial.py

	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	PIPENV_VERBOSITY=-1  pipenv run python manage.py collectstatic --noinput
	# psql -h localhost -U postgres -c 'DROP database IF EXISTS rpgtools';
	# psql -h localhost -U postgres -c 'CREATE database rpgtools';
	PIPENV_VERBOSITY=-1  pipenv run python manage.py makemigrations
	PIPENV_VERBOSITY=-1  pipenv run python manage.py migrate
	PIPENV_VERBOSITY=-1  pipenv run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@bayhasworld.com', 'adminpass',first_name='admin',last_name='admin')"
	PIPENV_VERBOSITY=-1  pipenv run python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('read-only', 'ro@bayhasworld.com', 'ropassword',first_name='read',last_name='only')"
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/publisher.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/bookformat.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/contributor.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/person.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/organization.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/gamesystem.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/game.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/book.json
	# PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/handler.json
	# PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/action.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/workflow.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py loaddata ./fixtures/token.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py populate_history --auto
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata auth.User --indent 4 | grep -v Fetch > ./fixtures/users.json

collectstatic:
	PIPENV_VERBOSITY=-1  pipenv run python manage.py collectstatic --noinput

# delete-db:
# 	psql -h localhost -U postgres -c 'DROP database IF EXISTS rpgtools';

dumpdata:
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.contributor --indent 4 | grep -v Fetch > ./fixtures/contributor.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.organization --indent 4 | grep -v Fetch > ./fixtures/organization.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.person --indent 4 | grep -v Fetch > ./fixtures/person.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.gamesystem --indent 4 | grep -v Fetch > ./fixtures/gamesystem.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.publisher --indent 4 | grep -v Fetch > ./fixtures/publisher.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.bookformat --indent 4 | grep -v Fetch > ./fixtures/bookformat.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.book --indent 4 | grep -v Fetch > ./fixtures/book.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.game --indent 4 | grep -v Fetch > ./fixtures/game.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.handler --indent 4 | grep -v Fetch > ./fixtures/handler.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.action --indent 4 | grep -v Fetch > ./fixtures/action.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.workflow --indent 4 | grep -v Fetch > ./fixtures/workflow.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata authtoken.token --indent 4 | grep -v Fetch > ./fixtures/token.json

init:
	PIPENV_VERBOSITY=-1  pipenv install --skip-lock

lint:
	PIPENV_VERBOSITY=-1  pipenv run pylint * --ignore=manage.py,Makefile,LICENSE,Pipfile,Pipfile.lock,README.md,requirements.txt,settings.py,wsgi.py,migrations,check_contributers.py --disable=R0801,R0401

test:
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	echo CODECOV_TOKEN
	PIPENV_VERBOSITY=-1  pipenv run coverage run --rcfile=.coveragerc --source='.' manage.py test api
	PIPENV_VERBOSITY=-1  pipenv run coverage html --rcfile=.coveragerc
	PIPENV_VERBOSITY=-1  pipenv run coverage report

dump_test_data:
	mkdir -p ui/static
	mkdir -p fixtures
	mkdir -p logs
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.contributor --indent 4 | grep -v Fetch > ./api/fixtures/test_contributor.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.organization --indent 4 | grep -v Fetch > ./api/fixtures/test_organization.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.person --indent 4 | grep -v Fetch > ./api/fixtures/test_person.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.gamesystem --indent 4 | grep -v Fetch > ./api/fixtures/test_gamesystem.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.publisher --indent 4 | grep -v Fetch > ./api/fixtures/test_publisher.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.bookformat --indent 4 | grep -v Fetch > ./api/fixtures/test_bookformat.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.book --indent 4 | grep -v Fetch > ./api/fixtures/test_book.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.game --indent 4 | grep -v Fetch > ./api/fixtures/test_game.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.handler --indent 4 | grep -v Fetch > ./api/fixtures/test_handler.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.action --indent 4 | grep -v Fetch > ./api/fixtures/test_action.json
	PIPENV_VERBOSITY=-1  pipenv run python manage.py dumpdata api.workflow --indent 4 | grep -v Fetch > ./api/fixtures/test_workflow.json

run:
	PIPENV_VERBOSITY=-1  pipenv run python ./manage.py runserver --settings rpgtools.settings

# setup-db:
# 	psql -h localhost -U postgres -c "CREATE USER rpgtools_admin with PASSWORD 'Gerrit8684!';"
# 	psql -h localhost -U postgres -c 'ALTER USER rpgtools_admin WITH SUPERUSER;'
# 	psql -h localhost -U postgres -c 'DROP database IF EXISTS rpgtools';
# 	psql -h localhost -U postgres -c 'CREATE database rpgtools';
