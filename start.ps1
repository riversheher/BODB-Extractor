param ($command)

if ($command -eq $null) {
    echo "Usage: start <command>"
    echo "  command: <setup|activate|deactivate|test>"
    exit
}

if ($command -eq "setup") {
    echo "Setting up environment"
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip3 install -r requirements.txt
    exit
}

if ($command -eq "activate") {
    echo "Activating environment"
    .\venv\Scripts\Activate.ps1
    exit
}

if ($command -eq "deactivate") {
    echo "Deactivating environment"
    deavtivate
    exit
}

if ($command -eq "test") {
    echo "Running tests"
    python -m unittest discover -s '.\internal'
    exit
}

echo "Starting $command"