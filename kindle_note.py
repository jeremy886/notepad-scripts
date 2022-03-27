lines=editor.getText().splitlines()

lines_without_empty_lines=[line.strip() for line in lines if line.strip() != ""]
lines_without_note_labels=[
    line.replace(".", "").replace(",", "") for line in lines_without_empty_lines if not line.startswith("Pink")
    ]
editor.setText("\r\n".join(lines_without_note_labels))