#!\bin\sh 

echo "============================================================"
echo "welcome to testing"
echo "===========================================================" 


if [ -d '.env' ];
then 
    echo "Environment is already existing in the folder" 
    echo "Starting the environment" 

else 
    echo "No Virtual Environment Found! Please run local_setup.sh first" 
    exit 1 
fi

. .env/Scripts/Activate 

export ENV=testing 

python -m pytest