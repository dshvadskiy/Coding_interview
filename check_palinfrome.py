class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) -1
        while start < end:
            #print(start,end)
            while not (s[start].isalpha() or s[start].isdigit()) and (start < end):
                start+= 1
                print('increment start')
            while not (s[end].isalpha() or s[end].isdigit())and (start < end):
                end -= 1
                print('decrement end')
            if s[start].lower() != s[end].lower():
                print(start,end)
                return False
            start += 1
            end -= 1
        return True

def main():
    s = Solution()
    print(s.isPalindrome("0P"))

main()
