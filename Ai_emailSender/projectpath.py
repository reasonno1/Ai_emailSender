import os
import re


class PathData:

    reference = r"01_Reference"
    export = r"03_Export"
    final = r"04_Final"
    scenes = "02_ProjectWork\\scenes\\"

    export_sync = r"T:\Digicom\RESOURSE\10_Statements\Sync_Files\Export_Sync.bat"
    export_sync_split = r"/to="


class AiProjectPath:

    def __init__(self, export):

        self.__root = None
        self.__export = None

        self.set_root(export)
        self.set_export(export)

    def get_root(self):
        return self.__root

    def set_root(self, root_path):

        pattern = r"\w:\\Digicom\\\d{4}\\\d{8}.+"

        p = re.compile(pattern)

        if not p.match(root_path):
            raise ValueError

        path_split = root_path.split("\\")

        self.__root = "\\".join(path_split[0:4])

    def set_export(self, export):
        pattern = r"\w:\\Digicom\\\d{4}\\\d{8}.+\\03_Export\\\d{8}"

        p = re.compile(pattern)
        if p.match(export):
            self.__export = export

        if not p.match(export):
            raise ValueError

    def get_scenes(self,):
        path = os.path.join(self.__root, PathData.scenes)
        return path
    #
    # def get_render_output(self):
    #     return self.__render_output

    def get_reference(self):
        path = os.path.join(self.__root, PathData.reference)
        return path

    def get_export(self):
        path = os.path.join(self.__root, PathData.export)
        return path

    def get_final(self):
        path = os.path.join(self.__root, PathData.final)
        return path

    def get_export_date(self):
        if self.__export:
            path = os.path.basename(self.__export)
            return path

        else:
            raise ValueError

    def get_chinese_name(self):

        with open(PathData.export_sync) as contents:
            src = contents.readlines()

        for i in src:
            line = i.strip()

            if line:
                if line.find(os.path.basename(self.__root)) != -1:
                    chinese = line.split(PathData.export_sync_split)[1]
                    chinese = chinese.replace('"', "")

                    chinese_path = os.path.basename(chinese)

                    return chinese_path

    def get_english_name(self):

        eng_name = self.__root.split("_")[1]

        return eng_name

if __name__ == '__main__':

    test = AiProjectPath(r"T:\Digicom\2016\20161102_ChuFengChingTing\03_Export\20161110_B")
    print(test.get_chinese_name())
    print(test.get_english_name())
    print(test.get_root())
    print(test.get_export())

    # test.set_root(r"T:\Digicom\2015\20150605_LiangMaoJTGS")
    # print(test.get_chinese_name())
    # print(test.get_root())
    # print(test.get_export())
