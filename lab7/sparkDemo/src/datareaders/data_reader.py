class DataReader:
    def __init__(self, spark_session):
        self.spark = spark_session

    def read_csv(self, file_path, header=True):
        df = self.spark.read.option("header", header).csv(file_path)
        return df

    def read_json(self, file_path):
        df = self.spark.read.json(file_path)
        return df
