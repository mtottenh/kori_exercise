# Extended Problem - Valid Parentheses

Given a string `s` containing just the characters `'(', ')', '{', '}', '['` and `']'`, determine if the input string is valid.

An input string is valid if:

* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Every close bracket has a corresponding open bracket of the same type.

## Example 1

```
Input: s = "()"
Output: true
```

## Example 2

```
Input: s = "()[]{}"
Output: true
```

## Example 3

```
Input: s = "(]"
Output: false
```


# Extension

Assume that any character could be added to the input sequence, the validator should still only consider a string correct if the brackets are balanced as in the above (IOW extra characters should simply be ignored).

