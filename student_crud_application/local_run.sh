#!\bin\sh 

echo "===============================================================" 
echo "Welcome to local run" 
echo "===============================================================" 

if [ -d '.env' ]; 
then 
    echo "local environment exists" 

else 
    echo "local environment not found" 
    echo "please run local_setup.sh first" 
fi 

echo "running the local_environment" 

. .env/Scripts/Activate

echo "exporting ENV" 
export ENV=development 

echo "running app.py" 
python app.py 