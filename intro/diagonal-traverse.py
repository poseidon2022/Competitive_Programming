class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(mat[0])):
            j, k = 0, i
            my_l = []
            while j<len(mat) and k>=0:
                my_l.append(mat[j][k])
                j+=1
                k-=1
            ans.append(my_l)
        for j in range(1, len(mat)):
            k, l = j, len(mat[0])-1
            my_l = []
            while k<len(mat) and l>=0:
                my_l.append(mat[k][l])
                k+=1
                l-=1
            ans.append(my_l)
        final = []
        for i in range(len(ans)):
            if i%2==0:
                final.extend(ans[i][::-1])
            else: final.extend(ans[i])
        
        return final
                                


        
        