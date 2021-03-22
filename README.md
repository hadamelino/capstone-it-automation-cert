# capstone-it-automation-cert
#### Week 1: Scale and Convert Images Using PIL
#### Week 2: Process Text Files with Python Dictionaries and Upload to Running Web Service
#### Week 3: Automatically Generate a PDF and sent it by Email
#### Week 4: Automate Updating Catalog Information


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
