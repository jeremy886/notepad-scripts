old=editor.getText()
new=old.replace(":", "-").replace(".", "").title()
editor.setText(new)