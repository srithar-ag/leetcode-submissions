class Solution:
    def grayCode(self, n: int) -> List[int]:
        total_codes = 1 << n  
    
        gray_code_sequence = [i ^ (i >> 1) for i in range(total_codes)]
      
        return gray_code_sequence