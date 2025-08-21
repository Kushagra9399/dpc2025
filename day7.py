'''
You are given an array height[] of non-negative integers where each element represents the height of a bar in a histogram-like structure. These bars are placed next to each other, and the width of each bar is 1 unit. When it rains, water gets trapped between the bars if there are taller bars on both the left and right of the shorter bars. The task is to calculate how much water can be trapped between these bars after the rain.

The amount of water trapped above any bar is determined by the difference between the height of the bar and the minimum height of the tallest bars on its left and right. For example, if a bar is surrounded by taller bars, the water will be trapped above it, filling the space up to the height of the shorter of the two taller bars.

Input:
An integer array height[] where each element represents the height of a bar in the histogram.
Example : 
height[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Output:
An integer representing the total units of water that can be trapped between the bars.
Water can be trapped in the following positions:
At index 2: Water trapped = 1 unit (bounded by heights 1 and 2).
At index 5: Water trapped = 2 units (bounded by heights 2 and 3).
At index 6: Water trapped = 1 unit (bounded by heights 2 and 3).
At index 9: Water trapped = 1 unit (bounded by heights 3 and 2).
The total amount of water trapped = 1 + 2 + 1 + 1 + 1 = 6 units.

'''
def day7_sol(height):
    left = 0
    right = len(height)-1
    left_max = 0
    right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

print(day7_sol([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
