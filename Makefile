admin-setup:
	docker volume create --name admin-static
	docker network create admin-network

build:
	docker build -t fouz/admin . -f  admin/Dockerfile
	docker build -t fouz/nginx . -f nginx/

run:

	docker run -d --rm --name=admin-nginx --net admin-network -p 80:80 -v admin-static:/static fouz/nginx
	
	docker run -d --rm --name=admin-db --net admin-network -p 5432:5432 -v .dbdata:/var/lib/postgresql/data postgres
	docker run -d --rm  --name=gunicornDjango --net admin-network --env-file=.env -p 8000:8000 -v admin-static:/static fouz/admin
