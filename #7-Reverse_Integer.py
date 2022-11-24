class Solution:
    def reverse(self, x: int) -> int:
        ptv=True
        if x<0:
            ptv=False
            x=-x
        if x>0:
            while x % 10 == 0:
                x = x/10
        x=int(x)
        str_x = str(x)
        n=len(str_x)
        tran_str_x = str_x[::-1]
        tran_x=int(tran_str_x)
        if ptv==False:
            tran_x=-tran_x        
        if tran_x>2**31-1:
            tran_x=0
        elif tran_x<-2**31:
            tran_x=0
        return tran_x