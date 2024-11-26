
python = ""
while True:
    line = input(">>> ").replace("\r", "")
    if "__EOF__" in line:
        python += 'print("thx :)")'
        break
    print(line)
    python += f"# {line}\n"  # comment :)

print(python)
