  class kadane {
    static int maxSubArraySum(int arr[]) {
// initializing variables 
        int length = arr.length;
        int maximumsum = 0, currentsum = 0;
 
// for loop step 4 to 6
        for (int i = 0; i < length; i++) {
            currentsum = currentsum + arr[i];
            if (maximumsum < currentsum)
                maximumsum = currentsum;
            if (currentsum < 0)
                currentsum = 0;
            System.out.println("For i = "+i);
            System.out.println("currentsum = "+currentsum);
            System.out.println("maximumsum = "+maximumsum);
            System.out.println();
        }
//return maximumsum as the answer 
        return maximumsum;
    }
 
    public static void main(String[] arg) {
        int [] arr = {-4, 1, 3, -2, 16, 2, -8, -9,-4};
        System.out.println("Maximum sum is " +
                maxSubArraySum(arr));
 
 
    }
}
