serve:
		python manage.py runserver

load_data:
		python manage.py loaddata armor.json
		python manage.py loaddata armorstats.json
		python manage.py loaddata mount.json
		python manage.py loaddata potion.json
		python manage.py loaddata tool.json
		python manage.py loaddata trinket.json

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
		python manage.py dumpdata resources.mount > resources/fixtures/mount.json --indent 4
		python manage.py dumpdata resources.potion > resources/fixtures/potion.json --indent 4
		python manage.py dumpdata resources.tool > resources/fixtures/tool.json --indent 4
		python manage.py dumpdata resources.trinket > resources/fixtures/trinket.json --indent 4
		python manage.py dumpdata resources.weapon > resources/fixtures/weapon.json --indent 4
		python manage.py dumpdata resources.weaponstats > resources/fixtures/weaponstats.json --indent 4