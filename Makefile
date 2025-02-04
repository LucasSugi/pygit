# Default value for container
CONTAINER_NAME ?= git-deletion
_CONTAINER_NAME_=$(CONTAINER_NAME)

# Mandatory enviroment variables
_GIT_FULL_PATH_=$(GIT_FULL_PATH)

# Extract the base path withou last folder
GIT_BASE_PATH=$(dir $(GIT_FULL_PATH))

# Extract the last folder
GIT_PROJECT=$(notdir $(GIT_FULL_PATH))

all: build run move

build:
	docker build -t $(_CONTAINER_NAME_):latest .

run:
	@echo "GIT_BASE_PATH: '$(GIT_BASE_PATH)'"
	@echo "GIT_PROJECT: '$(GIT_PROJECT)'"

	docker run --rm -v $(GIT_BASE_PATH)$(GIT_PROJECT)/:/src/$(GIT_PROJECT) $(_CONTAINER_NAME_) python extract_git_deletion.py --git-path /src/$(GIT_PROJECT)/

move:
	mv $(GIT_BASE_PATH)$(GIT_PROJECT)/git_deletion.csv .
