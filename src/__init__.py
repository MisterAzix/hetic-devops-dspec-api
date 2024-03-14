from pyspark.sql import SparkSession

from src.spark import get_spark_session


def init():
    spark: SparkSession = get_spark_session()

    df = spark.createDataFrame([("World",)], ["Hello"])
    df.show()

    spark.stop()

