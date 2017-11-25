import webbrowser

# Read or write and report bookmark
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
    begin = input("Enter first page index: ")
    end = begin + 10
    while begin < len(lines):
        # Report pages to view
        message = "Viewing page(s) " + str(begin)
        if begin != len(lines) - 1:
            message += "-" + str(min(end - 1, len(lines) - 1))
        print (message)

        # View pages
        for page_index in range(begin, min(end, len(lines))):
            url = lines[page_index]
            webbrowser.open_new_tab(url)

        # Ask to continue if appropriate
        if end < len(lines):
            response = ""
            while response != "y" and response != "n":
                response = raw_input("Continue? (y/n): ")
            if response == "y":
                begin += 10
                end += 10
            else:
                bookmark = end
                write_bookmark = True
                break
        else:
            break

# Write bookmark or report end
if write_bookmark:
    print ("Writing first unviewed page index (" + str(bookmark) + ") to bookmark.txt")
    with open("bookmark.txt", "w") as txt:
        txt.write(str(bookmark))
else:
    print ("There are no more pages")
    
print ("Finished")
