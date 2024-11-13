# BODB-Extractor
The BODB-Extractor is an effor to create a set of tools which will extract the data encoded in the "Berkley Option Database" into a modern format and database.  This is a project for the CS4470Y capstone course at the University of Western Ontario.

# Start Here

## Linux
A makefile is provided to help initialize your environment with the required dependencies for this project.

After you have cloned the project, you can get started by running the following commands:
```
make setup
```

Currently the following commands are also provided:

`make activate` - reinitialize your environment to the virtual env

`make deactivate` - stop using the virtual environment for this project

`make test` - runs unit tests

## Windows
A powershell script is provided to help initialize your environment, and to aid in automating testing procedures.

After you can cloned the project, you can get started by running the following commands:

`make setup` - initialize your environment

`make activate` - initialize the virtual environment for this project

`make deactivate` - stop using the virtual environment for this project

`make test` - runs unit tests