"""
You're given a string of length 12 or smaller, containing only digits. Write a function that returns all the possible IP addresses that can be created by inserting three . sin the string. 
An IP address is a sequence of four positive integers that are separated by . s, where each individual integer is within the range 0 - 255 , inclusive. 
An IP address isn't valid if any of the individual integers contains leading e s. For example, "192.168.0.1 " is a valid IP 
address, but "192. 168.00.1" and " 192.168. 0. 01" are not valid IP addresses, because they contain "0" as the first integer in a group.
example of a valid IP address is "99 .1.1.10" ; conversely, "991.1.1. 0" isn't valid, because "991" is greater than 255. 
Your function should return the IP addresses in string format and in no particular order. If no valid IP addresses can be created from the string, your function should return an empty list. 
Note: check out our Systems Design Fundamentals on Systems Expert to learn more about IP addresses! 
For this problem, you can assume that input string will always be valid.



Sample Input:
string = "1921680"


Sample Output:
[
  "
    1. 9. 216. 80",
    "
    1. 92. 16. 80",
    "
    1. 92. 168. 0",
    "
    19. 2. 16. 80",
    "
    19. 2. 168. 0",
    "
    19. 21. 6. 80",
    "
    19. 21. 68. 0",
    "
    19. 216. 8. 0",
    "
    192. 1. 6. 80",
    "
    192. 1. 68. 0",
    "
    192. 16. 8. 0"
    ]
    // The IP addresses could be ordered differently.

"""

def validIPAddresses(string):
    validIPAddressesFound = []

    for i in range(1, min(len(string), 4)):
        currentIPAddressParts = ["", "", "", ""]

        currentIPAddressParts[0] = string[:i]
        if not isValidPart(currentIPAddressParts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i:j]
            if not isValidPart(currentIPAddressParts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k]
                currentIPAddressParts[3] = string[k:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    validIPAddressesFound.append(".".join(currentIPAddressParts))


    return validIPAddressesFound

def isValidPart(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False

    return len(string) == len(str(stringAsInt)) # check for leading 0s

print(validIPAddresses("1921680"))

# Time Complexity: O(1)

# Space Complexity: O(1)


