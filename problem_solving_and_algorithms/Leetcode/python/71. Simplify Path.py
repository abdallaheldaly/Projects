class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        st = ['/']
        path = path.split("/")
        
        for i in path:
            if i == '..':
                if len(st) > 1:
                    st.pop()
                else:
                    continue
            elif i == '.':
                continue              
            elif i != '':
                st.append("/" + str(i))               
        if len(st) == 1:
            return "/"
        
        return "".join(st[1 : ])