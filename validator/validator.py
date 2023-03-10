from sys import stdin



def validate_parens(input: str) -> bool:
    '''
    Input: String to validate
    Output: True/False
    '''

    return True

if __name__ == "__main__":
    for line in stdin:
        print(f"Valid: {validate_parens(line)}")