gcloud beta dataproc clusters create cluster-analysis1 --enable-component-gateway \
          --region us-east4 --zone us-east4-a --master-machine-type n1-standard-8 \
          --master-boot-disk-size 500 --num-workers 2 --worker-machine-type n1-standard-8 \
          --worker-boot-disk-size 500 --image-version 1.5-debian10 \
          --optional-components ANACONDA,HIVE_WEBHCAT,JUPYTER --project firstgcpproject-303102


-- Using ITVarsity Labs to run my cluster 

STEP 3: Get dataset 