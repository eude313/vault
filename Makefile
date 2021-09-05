serve:
	python3 manage.py runserver


migrations:
	python3 manage.py makemigrations

	
migrate:
	python3 manage.py migrate

virtual:
	source virtual/bin/activate

update:
	git add .
	git commit -m"add initial commit"
	git push