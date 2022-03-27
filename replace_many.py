# encoding=utf-8

# lines = [line.strip() for line in editor.getText().splitlines() if line.strip() != ""]
lines = [line.strip() for line in editor.getText().splitlines()]

new1 = "\n".join(lines)

new2 = new1.replace("", ""
    ).replace("{{", "{"
    ).replace("}}", "}"
    ).replace(".He", "['He']"
    ).replace(".he", "['he']"
    ).replace(".his", "['his']"
    ).replace(".His", "['His']"
    ).replace(".him", "['him']"
    ).replace(".himself", "['himself']"
    )

editor.setText(new2)