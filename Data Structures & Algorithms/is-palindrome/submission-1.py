class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for st in s:
            if st.isalnum():
                res+=st.lower()

        return res == res[::-1]
        