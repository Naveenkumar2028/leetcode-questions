class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int best = prices[0];
        int maxprofit = 0;
        for(int i =0;i<n;i++){
            best = Math.min(best,prices[i]);
            int profit = prices[i]-best;
            maxprofit = Math.max(maxprofit,profit);
        }
        return maxprofit;
        
    }
}