# encoding=utf8
lines = [line.strip() for line in editor.getText().splitlines() if line.strip() != ""]

new = "\n".join(lines)
editor.setText(new)