public class Solution {
    public int[] plusOne(int[] digits) {
        digits[digits.length-1]++;
        for(int i=digits.length-1;i>=0;i--){
            if(digits[i]==10){
                if(i==0){
                    int[] newDigits= new int [digits.length+1];
                    digits[i]=0;
                    for(int j=digits.length-1;j>0;j--){
                        newDigits[j+1]=digits[j];
                    }
                    newDigits[0]=1;
                    return newDigits;
                }
                digits[i]=0;
                digits[i-1]++;
            }
            
            
        }
        return digits;
    }
}