# BODB-Extractor
The BODB-Extractor is an effor to create a set of tools which will extract the data encoded in the "Berkley Option Database" into a modern format and database.  This is a project for the CS4470Y capstone course at the University of Western Ontario.

# Start Here

## Linux
A shell script is in progress to aid in setup

## Windows
A powershell script is provided to help initialize your environment, and to aid in automating testing procedures.

After you can cloned the project, you can get started by running the following commands:

`.\start.ps1 setup` - initialize your environment

`.\start.ps1 activate` - initialize the virtual environment for this project

`.\start.ps1 deactivate` - stop using the virtual environment for this project

`.\start.ps1 test` - runs unit tests

## .env File
This project requires you to create a .env file to configure the database connection.  To do this, you will want to create a new file named `.env` in the root directory:

- On Windows: `ni .env`
- On Linux: `touch .env`

Then, you will require a file with the following structure:
- `[postgresql]` : The section heading for the database configurations
- `host = <hostname>`
- `database = <database name>`
- `user = <username>`
- `password = <password>`

This assumes you are utilizing password authentication or `md5` for connections.