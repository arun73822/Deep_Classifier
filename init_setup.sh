echo [$(date)]: "STARTED"
echo [$(date)]: "CREATING THE ENVIRNONMENT"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "ACTIVATING THE ENVIRNONMENT"
source activate ./env
echo [$(date)]: "INSTALLING THE DEVELOPER REQUIREMENTS"
pip install -r requirements_dev.txt
echo [$(date)]: "ENDED"