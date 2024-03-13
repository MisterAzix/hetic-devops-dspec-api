from pyspark.sql import SparkSession

from src.utils.spark import get_spark_session


def main():
    spark: SparkSession = get_spark_session()
    df = spark.createDataFrame([("Hello, PySpark!",)], ["greeting"])
    df.show()


if __name__ == "__main__":
    main()
