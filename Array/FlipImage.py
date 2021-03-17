class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        upto = n//2 if n%2 == 0 else n//2+1
        for i in range(n):
            for j in range(upto):
                temp = image[i][j]
                image[i][j] = int(not image[i][n-1-j])
                image[i][n-1-j] = int(not temp)
        
        return image
