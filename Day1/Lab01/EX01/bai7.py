print("Nhap cac dong van ban (Write 'done' to end):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nCac dong chu da nhap chuyen sang in hoa:\n")
for line in lines:
    print(line.upper())