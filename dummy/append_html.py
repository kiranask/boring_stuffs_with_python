
image_path = '/Users/kkatte/Documents/h_griffin/dyno/bin/230619_105224.png '
htmlfile = open("log.html", "a");
htmlfile.write("<html>\n")
htmlfile.write('<img src = "' + image_path + '" alt ="cfg">\n')
htmlfile.write("</html>\n")
htmlfile.close()





