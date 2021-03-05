all: chown start


chown:
	sudo chown -R $$USER ./main/.dbdata/
	sudo chown -R $$USER ./admin/.dbdata/


start: 
	docker-compose up -d  -f ./main/docker-compose
	docker-compose up -d  -f ./admin/docker-compose