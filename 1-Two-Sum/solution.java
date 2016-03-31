public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[] {0,0};
        for(int i=0;i<nums.length;i++){
            result[0] = i;
            for(int j=i+1;j<nums.length;j++){
                if(nums[j]==target-nums[i]){
                    result[1] = j;
                    break;
                }
            }
            if(result[1]!=0){
                break;
            } 
                
            
        }
        return result;
    }
}