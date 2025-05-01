<<<<<<< HEAD
#!/bin/bash

# Create and activate virtual environment
python3 -m venv /opt/venv
source /opt/venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Deactivate virtual environment
deactivate
=======
#!/bin/bash python manage.py migrate python manage.py collectstatic --noinput 
>>>>>>> b929cf953f137608e7f1df2c8095eaea708de70b
