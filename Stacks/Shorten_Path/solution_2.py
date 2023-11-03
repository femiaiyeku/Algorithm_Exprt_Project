"""

Write a function that takes in a non-empty string representing a valid Unix-shell path and returns a shortened
version of that path.
A path is a notation that represents the location of a file or directory in a file system.
A path can be an absolute path, meaning that it starts at the root directory in a file system, or a relative path,
meaning that it starts at the current directory in a file system.
In a Unix-like operating system, a path is bound by the following rules:
• The root directory is represented by a /. This means that if a path starts with /, It's an absolute path; if it
doesn't, it's a relative path.
• The symbol / otherwise represents the directory separator. This means that the path /foo/bar is the
location of the directory bar inside the directory foo, which is itself located inside the root directory.
• The symbol.. represents the parent directory. This means that accessing files or directories in
/foo/bar/.. is equivalent to accessing files or directories in /foo.
• The symbol represents the current directory. This means that accessing files or directories in
/foo/bar/. is equivalent to accessing files or directories in /foo/bar.
The symbols / and can be repeated sequentially without consequence; the symbol.. cannot,
however, because repeating it sequentially means going further up in parent directories. For example,
/foo/bar/baz/././. and /foo/bar/baz are equivalent paths, but /foo/bar/baz/../../../ and
/foo/bar/baz definitely aren't. The only exception is with the root directory: /../../.. and / are
equivalent, because the root directory has no parent directory, which means that repeatedly accessing
parent directories does nothing.
Note that the shortened version of the path must be equivalent to the original path. In other words, it must point
to the same file or directory as the original path.

Sample Input:
path = "/foo/../test/../test/../foo//bar/./baz"

Sample Output:

"/foo/bar/baz" # This path is equivalent to the input path.


""" 


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return str(self.stack)
    
    def __len__(self):
        return len(self.stack)
    
    def __getitem__(self, idx):
        return self.stack[idx]
    
    def __setitem__(self, idx, value):

        self.stack[idx] = value
        return self.stack[idx]
    
    def __delitem__(self, idx):

        del self.stack[idx]
        return self.stack[idx]
    
    def __iter__(self):
        return iter(self.stack)

def shortenPath(path):
    startsWithSlash = path[0] == "/"
    tokens = filter(isImportantToken, path.split("/"))
    stack = []
    if startsWithSlash:
        stack.append("")
    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":
                stack.append(token)
            elif stack[-1] != "":
                stack.pop()
        else:
            stack.append(token)

    if len(stack) == 1 and stack[0] == "":
        return "/"
    
    return "/".join(stack)



def isImportantToken(token):
    return len(token) > 0 and token != "."

