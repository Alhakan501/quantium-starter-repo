# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

# How  to get started
1. Clone the repository
git clone https://github.com/Alhakan501/quantium-starter-repo
cd quantium-starter

2. Install dependencies
pip install -r requirements.txt

3. Build the package
python -m build

4. Install in editable mode
pip install -e .


# How to run the app
python app_main.py
# or
python3 app_main.py



# How to run the tests
pytest
# or
pytest -v  # For detailed output



# How to run integration tests and push changes to github
1. make the bash script excutable
----> 'chmod +x integration_tests.sh'

2. Execute the script
----> './integration_tests.sh'




# Use this if you get externally-managed-environment errors
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

