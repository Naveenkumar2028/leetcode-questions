class Solution {
    public int maxSubArray(int[] nums) {

        int maxs= nums[0];
       
        int n = nums.length;
         int currentsum=0;
        for(int i =0;i<n;i++){
            currentsum+=nums[i];
            maxs = Math.max(maxs,currentsum);
            if(currentsum <0){
                currentsum = 0;
                }
            }
        return maxs;
        
    }
}