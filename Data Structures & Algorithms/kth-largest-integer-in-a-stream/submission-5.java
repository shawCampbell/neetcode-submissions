class KthLargest {

    int k;
    int[] nums;
    PriorityQueue<Integer> minHeap;
    Integer max;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.nums = nums;
        // add biggest k to minHeap 
        Arrays.sort(nums);
        this.minHeap = new PriorityQueue<>();
        // System.out.println("i >= " + String.valueOf(Math.max(nums.length - 3, 0)));
        // System.out.println("i = " + String.valueOf(nums.length - 1));

        for (int i = nums.length - 1; i >= Math.max(nums.length - k, 0); i--){
            System.out.println("Adding: " + String.valueOf(nums[i]));
            minHeap.add(nums[i]);
        }
        
        if (nums.length > 0){
            this.max = nums[nums.length - 1];
        }
        else{
            max = null;
        }
        
    }
    
    public int add(int val) {
        // add and return kth largest
        if (minHeap.size() < k){
            minHeap.add(val);
            max = val;
            return minHeap.peek();
        }
        if (max == null){
            max = val;
        }
        System.out.println("User adding: " + String.valueOf(val));
        System.out.println("Heap: " + minHeap.toString());
        if (val >= max || val > minHeap.peek()){
            max = val;
            minHeap.poll(); // O(1)
            minHeap.add(val); // O(logn)
        }
        System.out.println("New Heap: " + minHeap.toString());
        return minHeap.peek(); // O(1)
    }
}
