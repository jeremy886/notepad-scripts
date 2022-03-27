lines=editor.getText().splitlines()

good_lines=[line.strip() for line in lines if line.strip() != ""]

editor.setText("\r\n\r\n".join(good_lines))