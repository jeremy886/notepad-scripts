lines=editor.getText().splitlines()

good_lines=[line.strip().replace("+", "    -") for line in lines if line.strip() != ""]

editor.setText("\r\n".join(good_lines))