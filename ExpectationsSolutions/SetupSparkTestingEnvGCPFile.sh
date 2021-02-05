############## Installing GCSFUSE #######################
export GCSFUSE_REPO=gcsfuse-'lsb_release -c -s'
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install gcsfuse


############## Mounting Bucket #######################
mkdir spark-data
gcsfuse --implicit-dirs isaacdataprocess


############## Load to HDFS #######################
hdfs dfs -mkdir /user/spark/dataset
hdfs dfs -put ~/spark-data/* /user/spark/dataset

pyspark  --packages org.apache.spark:spark-avro_2.12:2.4.5

prodDF.groupBy("product_category_id") \
	.agg(max(col("product_price")).alias("max_price")) \
	.orderBy("max_price",ascending= False) \
	.select(concat_ws("|","product_category_id","max_price")) \
	.coalesce(1) \
	.write.mode("overwrite").option("compression","gzip") \
	.text("/user/spark/dataset/mock1/q3/output")


#To read a .csv file in pyspark 
	df = spark.read.format("csv").load("/user/spark/dataset/aids.csv")


spark.read.csv("hdfs://nn1home:8020/file.csv")

After reading the file -> Use PySpark to remove 2 columns from the data 