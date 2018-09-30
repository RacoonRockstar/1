import os
path1 = "/tmp/MyProject"
path2 = "/tmp/MyProject/css"
path3 = "/tmp/MyProject/js"
name = "/tmp/MyProject/css/style.css"
name2 = "/tmp/MyProject/js/app.js"
name3 = "/tmp/MyProject/index.html"
try:
    os.makedirs(path1)
    os.makedirs(path2)
    os.makedirs(path3)
    open(name, "w")
    open(name2, "w")
    open(name3, "w")
    my_file = open(name, "w")
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

    my_file2 = open(name2, "w")
    my_file2.write("/* this source generate automatically */")
    my_file2.close()

    my_file3 = open(name3, "w")
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
    print ("Создать директорию %s не удалось" % path1)
else:
    print ("Успешно создана директория %s" % path1)