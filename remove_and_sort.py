# Remove empty lines
# Remove line starts with 6
begin_ch = "6"
# Remove "    - "
remove_text = "- "
lines=editor.getText().splitlines()
lines=[line.strip() for line in lines if line.strip() != ""]
lines = [line.replace(remove_text, "") for line in lines if not line.startswith(begin_ch)]
lines = sorted(lines, key=lambda x: int(x[2:4]))
editor.setText("\r\n".join(lines))