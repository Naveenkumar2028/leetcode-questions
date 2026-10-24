public class SearchInRotatedSortedArrayTest {
    private static void check(int[] nums, int target, int expected) {
        int actual = new Solution().search(nums, target);
        if (actual != expected) {
            throw new AssertionError(
                "target=" + target + ", expected=" + expected + ", actual=" + actual
            );
        }
    }

    public static void main(String[] args) {
        check(new int[] {4, 5, 6, 7, 0, 1, 2}, 0, 4);
        check(new int[] {4, 5, 6, 7, 0, 1, 2}, 3, -1);
        check(new int[] {1}, 0, -1);
        check(new int[] {1}, 1, 0);
        check(new int[] {1, 3, 5, 7, 9}, 7, 3);
        check(new int[] {6, 7, 8, 1, 2, 3, 4, 5}, 6, 0);
        check(new int[] {3, 1}, 1, 1);
        check(new int[] {}, 5, -1);
        System.out.println("All SearchInRotatedSortedArray checks passed.");
    }
}
