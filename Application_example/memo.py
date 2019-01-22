import os

file_tr = 0

class file_create:
    def create_file(self, filename):
        self.fn = filename
        file_check = os.path.isfile(self.fn)
        if file_check == True:
            print("이미 %s 이름의 파일이 존재합니다." % filename)
            global file_tr
            file_tr = True
            if file_tr == True:
                print("기존 파일을 이어서 작성합니다.\n")
                assist_file = input("Insert : ")
                q = open(filename, 'a')
                q.write(assist_file)
                q.close()
        elif self.fn != os.path.isfile(self.fn):
            ofp = open(self.fn, 'w')
            ofp.close()

class file_write(file_create):
    def write_txt_file(self, wr):
        global file_tr
        if file_tr == False:
            self.write = wr
            p = open(filename, 'w')
            p.write(self.write)
            p.close()
        elif file_tr == True:
            pass

crt = file_create()
filename = input("Insert filename : ")
crt.create_file(filename)

wrf = file_write()
if file_tr == False:
    file_write = input("Insert content : ")
    wrf.write_txt_file(file_write)


