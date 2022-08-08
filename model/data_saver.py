class DataSaver:

    @staticmethod
    def data_saver(result, file='matches_results.txt', flag=False):
        """Saves the passed data into external .txt file.
        The save of data proceed in append mode.

        :param flag: boolean: if flag False - data_saver will not work (in cases when minimax works and reaches
        end of the game recursively just for making a decision of the efficient move)
        :param result: list with external data to save.
        :param file: str file path
        :return: void
        """
        if flag:
            with open(file, 'a', encoding='UTF-8') as f:
                f.writelines(', '.join(result) + '\n')
