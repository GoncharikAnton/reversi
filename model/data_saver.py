class DataSaver:

    @staticmethod
    def data_saver(result):
        with open('matches_results.txt', 'a', encoding='UTF-8') as f:
            f.writelines(' ,'.join(result))