class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:

            if flowerbed[0] == 0:
                return True

            elif n == 0:
                return True

            else:
                return False

        a = flowerbed.count(1)

        for i in range(len(flowerbed)):

            if i == 0:
                if flowerbed[1] == 0:
                    flowerbed[0] = 1

            elif i == len(flowerbed)-1:
                if flowerbed[len(flowerbed)-2] == 0:
                    flowerbed[len(flowerbed)-1] = 1

            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1

        return flowerbed.count(1) - a >= n
