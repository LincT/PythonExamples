import sys

if len(sys.argv) > 1:
    test = " ".join(sys.argv[1:])
else:
    test = input("enter a string to calculate pythagorean values:\n")
while test != "":
    val_list = []
    for each in test:
        if each != " ":
            # 97 = a
            val_list.append(ord(each.lower())-96)

    print(val_list)
    total = sum(val_list)
    print(total)
    while len(str(total)) > 1:
        val_list = [int(each) for each in str(total)]
        total = sum(val_list)
    print(total)
    test = input("enter a string to calculate pythagorean values:\n")
print("Thank you for using this app. Goodbye.")
