class DataTransformer:
    @staticmethod
    def aggregate_count_data(df, by):
        transformed_df = df.groupby(by).count()
        return transformed_df
