mkdir Isaac 
cd Isaac
aws s3 cp s3://isaacdataprocess/myscript/RandScript.py .
chmod +x RandScript.py 
date= $(date +%F_%H-%M-%S)
pythonfilename=$date'-pythonrandoutput.txt'
python RandScript.py |& tee -a result-$pythonfilename
aws s3 cp result-$pythonfilename s3://isaacdataprocess/RandResult/

cd ..
rm -rm Isaac