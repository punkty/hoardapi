serve:
		python manage.py runserver

load_data:
		python manage.py loaddata armor.json
		python manage.py loaddata armorstats.json

migrate_resources:
		python manage.py makemigrations resources

migrate:
		python manage.py migrate

drop_db:
		rm -f tmp.db db.sqlite3

drop_resources:
		rm -r resources/migrations

dump_data:
		python manage.py dumpdata resources.armor > resources/fixtures/armor.json --indent 4
		python manage.py dumpdata resources.armorstats > resources/fixtures/armorstats.json --indent 4