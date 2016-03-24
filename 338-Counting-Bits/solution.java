public class Solution {
    public int[] countBits(int num) {
        int []count = new int[num+1];
        count[0]=0;
        for(int i=1;i<=num;i++){
            if(i%2!=0){
                count[i] = count[i-1] + 1;
            } else if((i&(i-1))==0) {
                count[i] = 1;
            } else{
                count[i] = count[i>>1] ;
            }
        }
        return count;
    }
}