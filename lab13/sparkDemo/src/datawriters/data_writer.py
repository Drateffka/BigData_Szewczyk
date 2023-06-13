class DataWriter:

    @staticmethod
    def write_csv(df, file_path):
        df.write.csv(file_path, header=True, mode='overwrite')

    @staticmethod
    def write_json(df, file_path):
        df.write.json(file_path, mode='overwrite')