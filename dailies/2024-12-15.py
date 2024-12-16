# 3264. Final Array State After K Multiplication Operations I
class Solution:
	def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
					for i in range(k):
									smallest = 0
									for i in range(len(nums)):
													if(smallest == 0 or nums[i] < smallest):
																	index = i
																	smallest = nums[index]
									nums[index] = nums[index] * multiplier 
					return nums