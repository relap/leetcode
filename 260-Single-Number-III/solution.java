public class Solution {
    public int[] singleNumber(int[] nums) {
        int result = 0;
        int temp = 1;
        int count = 0;
        int[] singleNum = new int[] {0,0};
        if(nums.length<=2){
            return nums;
        }
        for(int i=0;i<nums.length;i++){
            result ^=nums[i]; 
        }
        while(result%2==0){
            result >>= 1;
            count++;
        }
            
        for(int i=0;i<nums.length;i++){
                
            if((nums[i]>>count)%2!=0){
                    singleNum[0] ^= nums[i];
                   
            } else {
                    singleNum[1] ^= nums[i]; 
                    
            }
                
            }
            
        
        
        return singleNum;
    }
}