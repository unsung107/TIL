import os

os.chdir(r'C:\Users\student\Startcamp\TIL\02_Day') #500개의 지원서가 있는곳으로 이동


filenames = os.listdir('.') #특정경로에 있는 모든 파일을 가져옴

for filename in filenames :
    #확장자가 .txt인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] #확장자만 따로 분리
    if extension == '.txt':
        
        os.rename(filename, filename.replace("SAMSUNG_SAMSUNG_","SSAFY_")) #첫번째 인자로 넘어간 이름을 두번째 인자로 넘어간 이름으로 바꾼다.


