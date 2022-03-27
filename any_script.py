import re


lines=editor.getText().splitlines()
good_lines=[line.strip() for line in lines if line.strip() != ""]
text="\r\n".join(good_lines)

numberings = re.findall(r"\d+\.", text)
# print(numberings)

for numbering in numberings:
    new = numbering[:-1]
    # print(numbering, new)
    text = text.replace(numbering, new)

# print(text)
editor.setText(text)
#editor.setText("\r\n\r\n".join(good_lines))