#!\bin\sh 

echo "=============================================================" 
echo "Welcome to setup" 
echo "=============================================================" 

if [ -d '.env' ]; 
then 
    echo "the environment already exists" 
else 
    echo "local environment not found" 
    echo "creating a local environment" 
    python -m venv .env
fi 

echo "running the local envionment" 
. .env/Scripts/Activate

echo "installing the required libraries" 

pip install --upgrade pip 
pip install -r requirements.txt 

pip freeze > requirements.txt 

#pip list 

echo "Exporting flask_app" 
export FLASK_APP=app

if [ -d 'migrations' ]
then 
    echo "migration folder already exists" 
else 
    echo "initialising db using flask" 
    flask db init 

    #done initiliasing it once 
    #don't run initial migrations multiple time 
    echo "doing the initial migration" 
    flask db migrate -m "Initial Migration"
fi 



echo "Adding changes (if any) to the db" 
flask db upgrade 

#echo "======================"
#echo "DEBUG" 
#echo "======================" 
#echo "checking the current db" 
#flask db current 

echo "Setup complete" 