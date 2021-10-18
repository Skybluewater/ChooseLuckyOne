import os
import xlrd
import json


class FileHandling:
    cur_folder = os.getcwd()
    file_folder = cur_folder + "/File"
    files = os.listdir(cur_folder + "/File")


class Json(FileHandling):
    Json_file_name = FileHandling.file_folder + "/stu_name.json"

    @staticmethod
    def write_json(dic, json_file_name=Json_file_name):
        with open(json_file_name, "w+", encoding="utf-8") as f:
            json.dump(dic, f, indent=2, ensure_ascii=False)

    @classmethod
    def change_json_file_name(cls, name):
        cls.Json_file_name = name

    @staticmethod
    def read_json_content(json_file_name=Json_file_name):
        with open(json_file_name, "r", encoding="utf-8") as f:
            dic = json.load(f)
        return dic


class Excel(FileHandling):

    def __init__(self):
        super().__init__()
        self.dic = {}
        for file in self.files:
            if os.path.splitext(file)[-1] == ".xls" or os.path.splitext(file)[-1] == ".xlsx":
                self.book = xlrd.open_workbook(file)
                self.sheet = self.book.sheet_by_index(0)
                return
        raise ValueError("No Such Excel")

    def filling_dic_from_excel(self):
        for row in range(2, self.sheet.nrows):
            str_content = self.sheet.row_values(row)
            if str_content[0] is None or str_content[0] == "" or not str_content[0].isdigit():
                break
            student_id = str_content[0]
            student_name = str_content[1]
            self.converting_to_dic(student_id, student_name)

    def converting_to_dic(self, parm1, parm2):
        if parm1 in self.dic:
            raise KeyError("Student_id already consists")
        self.dic[parm1] = parm2

    @staticmethod
    def saving_dic_as_json(dic):
        Json.write_json(dic)
