class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            else:
                l=st.pop()
                f=st.pop()
                if i=="+":
                    st.append(f+l)
                elif i=="-":
                    st.append(f-l)
                elif i=="*":
                    st.append(f*l)
                else:
                    st.append(int(f/l))
        return st[0]  
