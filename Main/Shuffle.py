from Main.DataImporting import Json, Excel
import random


class Shuffle:

    Json_file = None
    dic = None
    dic_keys_list = None

    @staticmethod
    def excel_renew():
        exe = Excel()
        exe.filling_dic_from_excel()
        Excel.saving_dic_as_json(exe.dic)

    @classmethod
    def read_from_json_as_dic(cls):
        cls.dic = Json.read_json_content()
        cls.dic_keys_list = list(cls.dic.keys())

    @classmethod
    def shuffle_dic(cls):
        while True:
            random.shuffle(cls.dic_keys_list)
            for key in cls.dic_keys_list:
                input("Please press Enter")
                print("幸运儿是: " + str(cls.dic[key]))