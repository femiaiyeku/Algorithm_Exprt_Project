"""

Write a function that takes in a pos tive integer numberOfTags and returns a list of all the valid strings that you can generate with that number of matched <div></di v> tags. 
A string is valid and contains matched <div></div> tags if for every opening tag <div> , there's a closing tag </div> that comes after the opening tag and that isn't used as a closing tag for another opening tag. Each output string should contain exactly numberOfTags opening tags and numberOfTags closing tags. 
For example, given numberOfTags = 2 , the valid strings to return would be: 

["<div></div><div></div>", "<div><div></div></div>"]

Note that the output strings don't need to be in any particular order.


Sample Input

numberOfTags = 3

Sample Output
    
    [
    "<div><div><div></div></div></div>",
    "<div><div></div><div></div></div>",
    "<div><div></div></div><div></div>",
    "<div></div><div><div></div></div>",
    "<div></div><div></div><div></div>"
    ]

    // The strings could be ordered differently.

    // For example, the following order would also be valid:



"""

def generateDivTags(numberOfTags):
    divs = []
    def backtrack(open, close, tags, curr_div):
        if tags == 0:
            divs.append(curr_div)
            return
        if open > 0:
            backtrack(open-1, close, tags-1, curr_div + "<div>")
        if close > open:
            backtrack(open, close-1, tags-1, curr_div + "</div>")
    backtrack(numberOfTags, numberOfTags, 2*numberOfTags, "")
    return divs

print(generateDivTags(3))


