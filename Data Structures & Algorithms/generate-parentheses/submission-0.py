class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curset = []
        res = []

        def generate(lcount, rcount):
            
            if lcount == rcount == n:
                res.append("".join(curset))
                return

            if lcount<n:
                curset.append("(")
                generate(lcount+1,rcount)
                curset.pop()

            if rcount<lcount:
                curset.append(")")
                generate(lcount,rcount+1)
                curset.pop()


        generate(0,0)
        return res