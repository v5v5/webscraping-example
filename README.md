# Create virtual environment
py -m venv .venv
# Activate virtual environment
./.venv/Scripts/Activate.ps1
# Deactivate if need
deactivate
# Install python libraries
pip install requests
pip install lxml