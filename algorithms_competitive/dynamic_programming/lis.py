class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        end_arr = []
        for i in range(len(a)):
            # element smallest among all end
            if len(end_arr) == 0 or a[i] < min(end_arr):
                # start new active list with element
                end_arr.append(a[i])
            # element largest among all end
            elif a[i] > max(end_arr):
                # clone longest active list and extend with element
                end_arr.append(a[i])
            # element in between
            else:
                # iterate over end elements
                for j in range(len(a)):
                    # find ceil value
                    if a[j] > a[i]:
                        # replace ceil with elemet
                        a[j] = a[i]
                        break
        return end_arr



if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split(',') ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))