# pygit

# How To
This tree enviroment variables should be fullfill:
* CONTAINER_NAME=<Name of container to create>
* GIT_FILEPATH=<The git base filepath>
* GIT_PROJECT=<The git folder>

 Example, supose you have a git project on filepath /Users/lucas.sugi/Desktop/my-project, then you can fullfill like this:

* CONTAINER_NAME=my-project-extraction
* GIT_FILEPATH=/Users/lucas.sugi/Desktop/
* GIT_PROJECT=my-project

**Pay atention** GIT_FILEPATH have a slash on start and end of filepath, while GIT_PROJECT its just the folder name without slashes.

After set all this variables you can run a `make` command on bash to start the pipeline image -> container -> run python script