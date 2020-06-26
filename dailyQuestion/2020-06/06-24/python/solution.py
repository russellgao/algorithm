
import os

def common_url(filenameA, filenameB) :
    """
    输入为两个文件名,输出为 result.txt
    :param filenameA:
    :param filenameB:
    :return:
    """
    filenames = []
    result_filename = "result.txt"
    def hash_url(filename) :
        with open(filename) as fp :
            for line in fp.readlines() :
                _filename = str(hash(line) % 20)
                filenames.append(_filename)
                with open(_filename, "a") as _fp :
                    _fp.write(line)
    hash_url(filenameA)
    hash_url(filenameB)
    with open(result_filename,"w") as fp :
        for _tmp_file in filenames :
            tmp_list = []
            with open(_tmp_file) as tmp_fp :
                for tmp_line in tmp_fp.readlines() :
                    if tmp_line in tmp_list :
                        if tmp_line and tmp_line != os.linesep :
                            fp.write(tmp_line)
                    else :
                        tmp_list.append(tmp_line)

if __name__ == "__main__" :
    filenameA = "file1"
    filenameB = "file2"
    common_url(filenameA,filenameB)
