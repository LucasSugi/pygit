# Mandatory enviroment variables
_CONTAINER_NAME_=$(CONTAINER_NAME)
_GIT_FILEPATH_=$(GIT_FILEPATH)
_GIT_PROJECT_=$(GIT_PROJECT)

all: build run move

build:
	docker build -t $(_CONTAINER_NAME_):latest .

run:
	docker run --rm -v $(_GIT_FILEPATH_)$(_GIT_PROJECT_)/:/src/$(_GIT_PROJECT_) $(_CONTAINER_NAME_) python extract_git_deletion.py --git-path /src/$(_GIT_PROJECT_)/

move:
	mv $(_GIT_FILEPATH_)$(_GIT_PROJECT_)/git_deletion.csv .