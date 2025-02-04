# pygit

# How To
This enviroment variable should be fullfill:
* **GIT_FULL_PATH**

Example, supose you have a git project on filepath `/Users/lucas.sugi/Desktop/my-project`, then you can fullfill like this:

* **GIT_FULL_PATH=/Users/lucas.sugi/Desktop/my-project**

❗❗❗ **GIT_FULL_PATH** should not have a slash on the end of string!

After set this variablee you can run a `make` command on bash to start the pipeline image -> container -> run python script
