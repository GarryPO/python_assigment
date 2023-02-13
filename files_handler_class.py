import glob
import csv
import os
import shutil


class Files_handler:
    def __init__(self, pathA, pathB, pathC):
        self.pathA = pathA
        self.pathB = pathB
        self.pathC = pathC
        self.path_list = [self.pathA, self.pathB, self.pathC]

    def compare_sets(self, setA, setB):
        count = 0
        for i in setA:
            for j in setB:
                if i == j:
                    count += 1
        return count

    def copy_file_to_C(self, file_path, path):
        shutil.copy(file_path, path)

    def update_scores_file(self, csv_file, max_match, path):
        scores_file = open(path + "/scores.txt", "a")
        scores_file.write(csv_file + "    " + str(max_match) + "\n")
        scores_file.close()

    def check_if_path_exist(self, path_list):
        for path in path_list:
            if not os.path.exists(path):
                return False
        return True

    def is_int(self, min_amount):
        if isinstance(min_amount, int):
            return True
        return False

    def main(self, min_amount):
        path_list = [self.pathA, self.pathB, self.pathC]
        assert self.check_if_path_exist(
            path_list), "One of the paths doesn't exist - check the input"
        assert self.is_int(
            min_amount), f"Value passed - {min_amount} - is not an integer - check the  input"
        try:
            for fnameA in glob.glob(self.pathA + "/*.csv"):
                max_match = 0
                with open(fnameA, 'r') as file:
                    readerA = csv.reader(file)
                    rowA = next(readerA)
                    for fnameB in glob.glob(self.pathB + "/*.csv"):
                        print("comparing " + fnameA + " And " + fnameB)
                        with open(fnameB, 'r') as file:
                            readerB = csv.reader(file)
                            rowB = next(readerB)
                            similarity_num = self.compare_sets(rowA, rowB)
                            if similarity_num > max_match:
                                max_match = similarity_num
                if max_match >= min_amount:
                    print('Copying')
                    self.copy_file_to_C(fnameA, self.pathC)
                    self.update_scores_file(fnameA, max_match, self.pathC)
        except Exception as e:
            print("ERROR!! check if the input is correct %s" % e)


"""
TODO: add tests for each class function
TODO: add functional tests against class provided 
TODO:Arrange folder structure add requirements.txt  reporting and logger 
"""
