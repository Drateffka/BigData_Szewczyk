from spark_session import create_spark_session
from datareaders.data_reader import DataReader
from datawriters.data_writer import DataWriter
from datatransformers.data_transformer import DataTransformer

if __name__ == "__main__":
    spark = create_spark_session()

    dr = DataReader(spark)
    actors_df = dr.read_csv("../data/actors.csv")

    transformed_df = DataTransformer.aggregate_count_data(actors_df, "category")
    transformed_df.show()

    DataWriter.write_csv(transformed_df, "../data/transformed.csv")

