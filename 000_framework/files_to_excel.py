'''
Title: List All files of the folder, this program will get each files name in folder and exporting to the Excel.
Author : Billour Ou(歐育溙)
\\020_IEEEE論文20240319下載\\
Date : 2024/4/14
Verstion: 2024041401
#pip3 install pandas
#pip3 install openpyxl
'''

import os
import sys
import pandas as pd

#sys.set_int_max_str_digits(0)
excel_path = u"D:\\t\\020_IEEEE20240319\\論文列表1.xlsx"
directory = u"D:\\t\\020_IEEEE20240319\\"

files = []
class ls_files:
    def __init__(self) -> None:
        pass
    def e_list(file_name):
        with open(file_name, "r", encoding='UTF-8') as f :
            data = f.read()

    def main():
        try:
            folder_path = directory
            for file_name in os.listdir(folder_path):
                files.append(file_name)
                #print(  file_name+" \n")
            data = {u'論文名稱': files }

            df = pd.DataFrame(data)
            #print(df)
            #print("Length of all PDFs : " + str(len(file_name)))
            df.to_excel(excel_path, index=False)
        finally:
            print("All Done. Listing all files into the Excel.")


if __name__ == "__main__":
    ls_files.main()



        
