# encoding=utf-8

# lines = [line.strip() for line in editor.getText().splitlines() if line.strip() != ""]
lines = [line.strip() for line in editor.getText().splitlines()]

new1 = "\n".join(lines)

new2 = new1.replace("", ""
    ).replace("- ", ""
    ).replace("+", "-"
    ).replace(" (CONSOLIDATING)", "🍰"
    ).replace(" (EXTENDING)", "🚀"
    ).replace(" (Consolidating)", "🍰"
    ).replace(" (Extending)", "🚀"
    ).replace("Example ", "Ex"
    ).replace("\n\n", "\n"
    )

editor.setText(new2)

