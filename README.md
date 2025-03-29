# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

# How  to get started
1. Clone the repository
git clone https://github.com/yourusername/quantium-starter.git
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



# Use this if you get externally-managed-environment errors
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

