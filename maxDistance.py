class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        c1=colors[0]
        c2=colors[len(colors)-1]
        m1=0
        m2=0
        for i in range(len(colors)-1,0,-1):
            if( colors[i]!=c1):
                m1=max(m1,i)
            if(colors[i]!=c2):
                m2=max(m2,len(colors)-i-1)
            m=max(m1,m2)
        return m

        
