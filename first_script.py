# editor.replace("old", "new")

text = editor.getText()

if "\r\n" in text:
    print("breakline by \\r\\n")