public class Array2 {
    public static void main(String[] args) {
        // Array Operations.
        int num[][] = {
                // 2 by 3 Array.
                { 1, 2, 3 },
                { 4, 5, 6 }
        };
        int CountEven = 0;
        int CountOdd = 0;
        for (int i = 0; i < num.length; i++) {
            for (int j = 0; j < num[i].length; j++) {
                if (num[i][j] % 2 == 0) {
                    CountEven++;

                } else {
                    CountOdd++;
                }
            }
        }
        System.out.println("Even Numbers: " + CountEven);
        System.out.println("Odd Numbers: " + CountOdd);
        
    }
}
