from py_module.config import Configuration
from py_module.data_reader import DataReader
from py_module.data_preprocessing import DataProprocessing

import os

class EngineCyclePrediction(object):

    def __init__(self):
        self.config_obj = Configuration()
        self.reader_obj = DataReader()
        self.data_preprocessing_obj = DataProprocessing()

    def data_loading(self):
        file_path = os.path.join(self.config_obj.data_folder, self.config_obj.file_name)
        data = self.reader_obj.read_csv_data(file_path)

        test_file_path = os.path.join(self.config_obj.test_data_folder, self.config_obj.test_file_name)
        testing_data = self.reader_obj.read_csv_data(test_file_path)
        return data

    def data_preprocessing(self, data):
        
        data = self.data_preprocessing_obj.data_preprocessing_2008_PHM_Engine_data(data, self.config_obj.features_name)

        return(data)

def main_flow():
    
    main_obj = EngineCyclePrediction()
    data = main_obj.data_loading()
    data = main_obj.data_preprocessing(data)

if __name__ == "__main__":
    main_flow()

