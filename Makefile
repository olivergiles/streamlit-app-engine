.PHONEY: build
build:
	docker build . -t engine-test

.PHONEY: run
run:
	docker run -p 8080:8080 engine-test

.PHONEY: deploy
deploy:
	gcloud app deploy app.yaml
