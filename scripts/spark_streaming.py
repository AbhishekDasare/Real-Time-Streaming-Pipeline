from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Streaming Pipeline") \
    .getOrCreate()

stream_df = spark.readStream \
    .format("socket") \
    .option("host","localhost") \
    .option("port",9999) \
    .load()

query = stream_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
