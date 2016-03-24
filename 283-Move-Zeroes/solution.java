public class Solution {
    public void moveZeroes(int[] nums) {
        int count=0;// break loop
        for(int i=0;i<nums.length-count;){
            if(nums[i]==0){
                for(int j=i+1;j<nums.length;){
                    nums[j-1]=nums[j];
                    j++;
                }
                nums[nums.length-1]=0;
                count++;
                
                
            } else{
                i++;
            }
            
        }
    }
}