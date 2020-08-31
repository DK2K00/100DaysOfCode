class d36_binary
{

    int binary_search(int arr[], int l, int h, int x)
    {
        if(h >= 1)
        {
                int mid = (l + (h-1)) / 2;

                if(arr[mid] == x)
                    return mid;

                if(arr[mid] < x)
                    return binary_search(arr, mid + 1, h, x);
                
                else
                    return binary_search(arr, l, mid - 1, x);
        }

        return -1;
    }

    public static void main(String args[])
    {
        int[] arr = {1, 2, 5, 13, 24, 33, 45, 58, 67, 71, 80, 99};
        int len = arr.length;

        int x = 80;

        d36_binary bs = new d36_binary();
        int res = bs.binary_search(arr, 0, len-1, x);

        if(res == -1)
            System.out.println("Element not present in the list");

        else
            System.out.println("Element is present in the list at index: " + res);
    }
}