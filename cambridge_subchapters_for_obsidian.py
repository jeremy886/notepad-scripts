# encoding=utf8

old = editor.getText().replace("Progress quiz", "").replace("Applications and problem-solving", "").replace("Investigation", "")

lines = [line for line in old.splitlines() if line.strip() != ""]
lines_new = sorted(lines)
# print(lines_new)
only_chapters = "- " + "\n- ".join(lines_new)
# print(only_chapters)

editor.setText(only_chapters)