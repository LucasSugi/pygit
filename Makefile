CONTAINER_NAME=""
GIT_FILEPATH=""
GIT_PROJECT=""

all: build run move

build:
	docker build -t $(CONTAINER_NAME):latest .

run:
	docker run --rm -v $(GIT_FILEPATH)$(GIT_PROJECT)/:/src/$(GIT_PROJECT) $(CONTAINER_NAME) python extract_git_deletion.py --git-path /src/$(GIT_PROJECT)/

move:
	mv $(GIT_FILEPATH)$(GIT_PROJECT)/git_deletion.csv .