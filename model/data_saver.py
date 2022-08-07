class DataSaver:

    @staticmethod
    def data_saver(result, file='matches_results.txt'):
        """Saves the passed data into external .txt file.
        The save of data proceed in append mode.

        :param result: list with external data to save.
        :param file: str file path
        :return: void
        """
        with open(file, 'a', encoding='UTF-8') as f:
            f.writelines(', '.join(result) + '\n')
