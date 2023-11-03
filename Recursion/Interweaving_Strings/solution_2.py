"""

Write a function that takes in three strings and returns a boolean representing whether the third string can be
formed by interweaving the first two strings.
To interweave strings means to merge them by alternating their letters without any specific pattern. For instance,
the strings "abe" and "123" can be interwoven as "a1b2c3", as "abc123", and as "ab1c23 (this list is
nonexhaustive).
Letters within a string must maintain their relative ordering in the interwoven string.

Sample Input:
one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"

Sample Output:
true


"""


def interweavingStrings(s1, s2, s3):
    S = False
    D = {}
    def r(i, j):
        if (i, j) in D:
            return D[(i, j)]
        k = i + j
        if k == len(s3):
            return True
        if i < len(s1) and s1[i] == s3[k]:
            S = r(i + 1, j)
            if S:
                return True
        if j < len(s2) and s2[j] == s3[k]:
            S = r(i, j + 1)
            return S
        return False

    return r(0, 0)


# o(nm) time | o(nm) space - where n and m are the lengths of the first two strings respectively
