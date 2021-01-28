mkdir Isaac
cd Isaac
ssh-keygen -t rsa -b 2048 -C "github.davidisaac905@outlook.com"
sudo yum install git
git clone https://github.com/AdeyinkaDavid/DataEngineering.git
cd DataEngineering/
cd cf-scripts/
aws s3 cp cf-vpc-pub-priv-subnet.yaml s3://isaacdataprocess/cfscript/
