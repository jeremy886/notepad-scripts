# encoding=utf8
old = editor.getText()
new = old.replace("• ", "\n• ").replace("  Your strengths", "\n\nYour strengths")
editor.setText(new)