import os

projectpath = "/tmp/MyProject"
pathcss = "/tmp/MyProject/css"
pathjs = "/tmp/MyProject/js"
namecss = "/tmp/MyProject/css/style.css"
namejs = "/tmp/MyProject/js/app.js"
namehtml = "/tmp/MyProject/index.html"
try:
    os.makedirs(projectpath)
    os.makedirs(pathcss)
    os.makedirs(pathjs)
    open(namecss, "w")
    open(namejs, "w")
    open(namehtml, "w")
    my_file = open(namecss, "w")
    my_file.write("/* this source generate automatically */ \n"
                  "html {\n"
                  "}\n"
                  "body {\n"
                  "}\n"
                  ".content {\n"
                  "}\n"
                  ".content h1 {\n"
                  "}")

    my_file.close()

    my_file2 = open(namejs, "w")
    my_file2.write("/* this source generate automatically */")
    my_file2.close()

    my_file3 = open(namehtml, "w")
    my_file3.write("<!DOCTYPE html>\n"
                   "<html lang=""eng"">\n"
                   "<head>\n"
                   " <meta charset=""UTF-8"">\n"
                   "<title>Title</title>\n"
                   "<link rel=""stylesheet"" href=""css/style.css""/>\n"
                   "</head>\n"
                   "<body>\n"
                   "<div class=""content"">\n"
                   " <h1>Hello! I'm ready for edit! :)</h1>\n"
                   "</div>\n"
                   "<script src=""js/app.js""></script>\n"
                   "</body>\n"
                   "</html>\n")
    my_file3.close()
except OSError:
    print("Создать директорию %s не удалось" % projectpath)
else:
    print("Успешно создана директория %s" % projectpath)
