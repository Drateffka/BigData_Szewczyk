from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext


def create_spark_session(app_name="SparkDemo"):
    conf = SparkConf()
    conf.set("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:../log4j.properties")

    spark = SparkSession.builder.appName(app_name).getOrCreate()
    spark.sparkContext.setLogLevel("INFO")
    return spark
