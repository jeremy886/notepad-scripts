# encoding=utf-8

# lines = [line.strip() for line in editor.getText().splitlines() if line.strip() != ""]
names1 = [line.strip() for line in editor.getText().splitlines()]

new_text = ""
for name in names1:
    first_name = name.split()[0]
    last_name = name.split()[1]
    new_text += f"{first_name}\t{last_name}\n"

print(new_text)
editor.setText(new_text)