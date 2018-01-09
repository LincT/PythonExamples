# small program to change a sentence to camel case.


def main():
    preformat = input("type a sentence to format ")
    formatting = preformat.split()
    formattedString = formatting[0]

    for i in range(len(formatting)):
        if i > 0:
            formattedString += (formatting[i])[0].capitalize()
            formattedString += (formatting[i])[1:].lower()
    print(formattedString)


main()
