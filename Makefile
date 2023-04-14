
  
build:
	docker-compose -f local.yml build

run:
	docker-compose -f local.yml up

test:
	docker-compose -f local.yml run django pytest

shell:
	docker-compose -f local.yml run --rm django python manage.py shell

build-css:
	npm run build

build-css-prod:
	NODE_ENV=production make build-css

migration:
	docker-compose -f local.yml run --rm django python manage.py makemigrations
	docker-compose -f local.yml run --rm django python manage.py migrate

squashmigrations:
	# make squashmigrations app=invoices upto=0004
	docker-compose -f local.yml run --rm django python manage.py squashmigrations ${app} ${upto}

createsuperuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

deploy:
	git push origin main
	git push heroku main

logs:
	heroku logs --num=50 --tail
