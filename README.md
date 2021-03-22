##Huruf Bergantian

'''python
def hurufBergantian(inputString):
    output = 0
    i = 0
    testString = []
    for huruf in inputString:
        testString.append(huruf)
        if huruf == testString[i - 1] and i != 0:
            output += 1
        i += 1
    print("Input: \"{}\"".format(inputString))
    print("Output: {}".format(output))
    return output
    
def main():
    hurufBergantian("PCPPCPPP")

if __name__ == "__main__":
    main()
'''
