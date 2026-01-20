#!\bin\sh

echo "---------------------"
echo "running the environment locally"
echo "--------------------"

if [ -d ".env" ]; 
then 
    echo "starting the local environment"

else
    echo "environment not found, please run loacl setup first"
    exit 1
fi

echo "activating the local environment" 

. .env/Scripts/Activate 

export ENV=development 

echo "running the app" 

python app.py 
 
echo "The server should be running now" 