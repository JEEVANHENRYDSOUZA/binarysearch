class Solution(object):
    def searchMatrix(self, matrix, target):
        start=0
        end=len(matrix[0])-1
        while(end>=0 and start <=len(matrix)-1):
            mid=start+(end-start)/2
            if(matrix[start][end]==target):
                return True
            elif(matrix[start][end]<target):
                start+=1
                
                
            else:
                end-=1
        return False
#complexity log(m*n)----m =number of rows.n=number of columns
