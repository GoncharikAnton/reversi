import os
import unittest

from model.data_saver import DataSaver


class TestDataSaver(unittest.TestCase):

    def test_data_saver_with_result(self):
        DataSaver.data_saver(['some', 'result'], 'test_file.txt')
        try:
            with open('test_file.txt') as f:
                for i in f:
                    self.assertEqual(i.strip(), 'some, result')
        except FileExistsError:
            print('File doesn\'t exist')
        finally:
            os.remove('test_file.txt')
