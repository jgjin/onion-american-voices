import webbrowser

bookmark = 0
try:
    with open("bookmark.txt", "r") as txt:
        bookmark = int(txt.read())
except IOError:
    with open("bookmark.txt", "w") as txt:
        txt.write("0\n")
print "Last recorded first unviewed page index: " + str(bookmark)

lines = []
with open("urls.txt", "r") as txt:
    lines = txt.readlines()
    begin = int(raw_input("Enter first page index: "))
    end = begin + 10
    bookmark = end
    response = "420 blayz it"
    while begin < len(lines):
        if begin == len(lines) - 1:
            print "Viewing page " + str(begin)
        else:
            print "Viewing pages " + str(begin) + \
                "-" + str(min(end - 1, len(lines) - 1))
        for page_index in range(begin, end):
            try:
                url = "http://www.theonion.com" + lines[page_index]
                webbrowser.open_new_tab(url)
            except IndexError:
                begin = page_index
                bookmark = end
                break
        if end == len(lines):
            begin = len(lines)
            bookmark = end
        elif end < len(lines):
            response = ""
            while response != "y" and response != "n":
                response = raw_input("Continue? (y/n): ")
            if response == "y":
                begin += 10
                end += 10
            else:
                bookmark = end
                break
        else:
            break
    if response != "n":
        print "There are no pages starting from page index " + str(begin)
        
if bookmark < len(lines):
    print "Recording first unviewed page index (" + str(bookmark) + ")"
    with open("bookmark.txt", "w") as txt:
        txt.write(str(bookmark))

print "Finished"
