# encoding=utf-8
DEBUG = False
text = editor.getText()

def line_treat(line):
    line2 = line.strip().replace("- ", "")
    return line2
    # new1 = "\n".join(lines)
    # new2 = new1.replace("", ""
    #     ).replace(" (CONSOLIDATING)", "🌉"
    #     ).replace(" (EXTENDING)", "🚀"
    #     ).replace("+", "-"
    #     ).replace("Example ", "Ex"
    #     ).replace("\n\n", "\n"
#     )


lines = [line_treat(line) for line in text.splitlines() if line.strip() != ""]


import re
def num_sort(test_string):
    print(test_string)
    num = list(map(int, re.findall(r'\d+', test_string)))[0]
    if DEBUG == True: print(num)
    return num
if DEBUG == True: print(f"{lines=}")

lines.sort(key=num_sort)

editor.setText("\n".join(lines))