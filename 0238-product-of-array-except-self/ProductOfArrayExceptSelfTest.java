import java.util.Arrays;

/** Standalone regression tests for the Product of Array Except Self solution. */
public class ProductOfArrayExceptSelfTest {
    private static void assertArrayEquals(int[] expected, int[] actual, String testName) {
        if (!Arrays.equals(expected, actual)) {
            throw new AssertionError(
                testName + " failed: expected " + Arrays.toString(expected)
                    + " but got " + Arrays.toString(actual)
            );
        }
        System.out.println("PASS: " + testName);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        assertArrayEquals(
            new int[] {24, 12, 8, 6},
            solution.productExceptSelf(new int[] {1, 2, 3, 4}),
            "standard positive values"
        );
        assertArrayEquals(
            new int[] {0, 0, 9, 0, 0},
            solution.productExceptSelf(new int[] {-1, 1, 0, -3, 3}),
            "one zero and negative values"
        );
        assertArrayEquals(
            new int[] {3, 2},
            solution.productExceptSelf(new int[] {2, 3}),
            "two elements"
        );
        assertArrayEquals(
            new int[] {0, 0},
            solution.productExceptSelf(new int[] {0, 0}),
            "two zeros"
        );
        assertArrayEquals(
            new int[] {-6, 3, -2},
            solution.productExceptSelf(new int[] {1, -2, 3}),
            "negative values"
        );
    }
}
