#!\bin\sh 

echo "====================================================" 
echo "welcome to testing environment" 
echo "this environment is created for running your tests." 
echo "====================================================" 

if [ -d '.env' ]; 
then 
    echo "local environment exists" 
else 
    echo "local environment not found" 
    echo "please run local_setup first" 
fi 

echo "Activating the local environment" 
. .env/Scripts/Activate

echo "exporting the environment" 
export ENV=testing 

pytest