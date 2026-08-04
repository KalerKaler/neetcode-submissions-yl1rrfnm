class Solution {
    public int singleNonDuplicate(int[] nums) {

        int l = 0, r = nums.length - 1, mid;

        while (l < r){
            mid = l + (r - l) / 2;

            if ((mid % 2 == 0 && nums[mid] == nums[mid + 1]) || (mid % 2 == 1 && nums[mid] == nums[mid - 1])){
                l += 1;
            }
            else{
                r -= 1;
            }
        }
        return nums[l];
    }
}