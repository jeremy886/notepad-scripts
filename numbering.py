lines=editor.getText().splitlines()

for n, line in enumerate(lines, 1):
    print(f"{n} {line}")