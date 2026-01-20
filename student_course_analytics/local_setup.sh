#!\bin\sh

echo "---------------------------------------"
echo "welcome to local setup"
echo "---------------------------------------"

echo "setting up local environment"

if [ -d ".env" ]; 
then 
    echo "local environment already exists" 
else 

    echo "local environment not found" 
    echo "creating a local environment" 

    python -m venv .env 
fi 

echo "running the local environment" 

. .env/Scripts/Activate 

echo "installing the required libraries" 

pip install --upgrade pip 
pip install -r requirements.txt 

pip freeze > requirements.txt

echo "Setup complete, you can run local_run.sh now!"