import os
from PIL import Image, ExifTags


class picture_sorter:

    def __init__(self,path_to_folder):
        self.__folder_path = path_to_folder

        self.__base_path = "C:\\"+os.environ["HOMEPATH"]+"\\Desktop\\tmp"
        os.makedirs(self.__base_path)

        self.__month      = ["01_Jan","02_Fev","03_Mar","04_Avr","05_Mai","06_Jun","07_Jui","08_Aou","09_Sep","10_Oct","11_Nov","12_Dec"]
        self.__month_list = []
        self.__year_list  = []
        self.__pict_list  = []

    def __retrive_pict(self):
        pict_list = os.listdir(self.__folder_path)

        for i_pict in range(len(pict_list)):
            self.__pict_list.append(img_container(self.__folder_path + "\\" + pict_list[i_pict]))

            month = self.__month[int(self.__pict_list[i_pict].get_month())-1]
            year  = self.__pict_list[i_pict].get_year()

            if year not in self.__year_list:
                self.__year_list.append(year)
                path_tmp = self.__base_path + "\\" + str(year)
                os.makedirs(path_tmp)

            if month not in self.__month_list:
                self.__month_list.append(month)
                path_tmp_2 = self.__base_path + "\\" + str(year) + "\\" + month
                os.makedirs(path_tmp_2)

    def __move_pict(self):
        for i_pict in range(len(self.__pict_list)):
            year_path       = "\\" + self.__pict_list[i_pict].get_year()
            month_path      = "\\" + self.__month[int(self.__pict_list[i_pict].get_month())-1]
            pict_name_path  = "\\" + self.__pict_list[i_pict].get_name()

            old_path = self.__pict_list[i_pict].get_path()
            new_path = self.__base_path + year_path + month_path + pict_name_path
            os.rename(old_path, new_path)

    def run(self):
        self.__retrive_pict()
        self.__move_pict()

class img_container:

    def __init__(self,img_path):
        self.__path = img_path
        img = Image.open(self.__path)
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
        date_time = exif["DateTimeOriginal"]
        self.__year = date_time[:4]
        self.__month = date_time[5:7]

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_path(self):
        return self.__path

    def get_name(self):
        return os.path.basename(self.__path)



test = picture_sorter("C:\Users\ltsago3\Desktop\\test")
test.run()

