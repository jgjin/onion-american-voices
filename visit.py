import webbrowser

bookmark = 0
try:
    with open("bookmark.txt", "r") as txt:
        bookmark = int(txt.read())
except IOError:
    with open("bookmark.txt", "w") as txt:
        txt.write("0")
print ("Last recorded first unviewed page index: " + str(bookmark))

write_bookmark = False
with open("urls.txt", "r") as txt:
    lines = txt.readlines()
    begin = int(input("Enter first page index: "))
    end = begin + 10
    while begin < len(lines):
        message = "Viewing page(s) " + str(begin)
        if begin != len(lines) - 1:
            message += "-" + str(min(end - 1, len(lines) - 1))
        print (message)
        for page_index in range(begin, end):
            try:
                url = "http://www.theonion.com" + lines[page_index]
                webbrowser.open_new_tab(url)
            except IndexError:
                break
        if end < len(lines):
            response = ""
            while response != "y" and response != "n":
                response = input("Continue? (y/n): ")
            if response == "y":
                begin += 10
                end += 10
            else:
                bookmark = end
                write_bookmark = True
                break
        else:
            break

if write_bookmark:
    print ("Recording first unviewed page index (" + str(bookmark) + ")")
    with open("bookmark.txt", "w") as txt:
        txt.write(str(bookmark))
else:
    print ("There are no pages")
    
print ("Finished")
