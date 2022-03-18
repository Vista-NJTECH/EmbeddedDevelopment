from random import seed


with open('Python/3.FilesIO/test.txt', 'r',encoding = 'utf-8') as f:
  print("文件名是{0}".format(f.name))
  print(f.tell())
  f.seek(15,0)
  print(f.tell())