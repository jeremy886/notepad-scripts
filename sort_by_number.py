# encoding=utf8
lines = [line for line in editor.getText().splitlines() if line.strip() != ""]
num_lines = [line for line in lines if line.split()[0].isdigit()]
print(num_lines)
lines_new = sorted(num_lines, key=lambda e: int(e.split()[0]))
print(lines_new)
new = "\n".join(lines_new)
# print(new)
editor.setText(new)
