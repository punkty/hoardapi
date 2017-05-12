serve:
		python manage.py runserver


migrate_resources:
		python manage.py makemigrations resources

migrate:
		python manage.py migrate

drop_db:
		rm -f tmp.db db.sqlite3

drop_resources:
		rm -r resources/migrations
