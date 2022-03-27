new = editor.getText().replace("    Chapter ", "\n\n## ").replace(".", "").replace("Semester review 1\n", "").replace("Semester review 2\n", "")
editor.setText(new)