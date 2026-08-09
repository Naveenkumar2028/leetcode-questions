import java.util.*;
class Solution {
    public long weightedSum(int[] parent, int[] nums) {
       
        int n = parent.length;

        // Build tree
        List<List<Integer>> tree = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            tree.add(new ArrayList<>());
        }

        for (int i = 1; i < n; i++) {
            tree.get(parent[i]).add(i);
        }

        // Find height
        int height = getHeight(tree, 0);

        // Calculate weights
        return calculateWeight(tree, nums, 0, 1, height);
    }

    private int getHeight(List<List<Integer>> tree, int node) {
        int height = 1;

        for (int child : tree.get(node)) {
            height = Math.max(height, 1 + getHeight(tree, child));
        }

        return height;
    }

    private long calculateWeight(
            List<List<Integer>> tree,
            int[] nums,
            int node,
            int depth,
            int height) {

        long weight = (long) nums[node] * (height - depth + 1);

        for (int child : tree.get(node)) {
            weight += calculateWeight(
                tree, nums, child, depth + 1, height
            );
        }

        return weight;
    }
}
        
    
