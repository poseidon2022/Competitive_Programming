class Solution:
    def flipAndInvertImage(self, images: List[List[int]]) -> List[List[int]]:
        for i in range(len(images)):
            j, k = 0, len(images[i])-1
            while j<=k:
                if j<k: images[i][j], images[i][k] = int(not images[i][k]), int(not images[i][j])
                else: images[i][j] = int(not images[i][j])
                j, k = j+1, k-1
        return images
        