public class Solution {
    public int missingNumber(int[] nums) {
        int sum = (1+nums.length)*nums.length/2;
        int count = 0;
        for(int i=0;i<nums.length;i++){
            count += nums[i];
        }
        int num = sum - count;
        
        
        return num;
    }
}