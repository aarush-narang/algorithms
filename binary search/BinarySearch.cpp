// binary search algorithm
// 1. find the middle element
// 2. if the middle element is the target, return the index
// 3. if the middle element is greater than the target, search the left half
// 4. if the middle element is less than the target, search the right half
// 5. repeat 1-4 until the target is found or the search space is exhausted
// 6. if the target is not found, return -1
// 7. if the search space is exhausted, return -1
// 8. return the index of the target

#include <iostream>
#include <vector>

using namespace std;

int binarySearch(vector<int> &nums, int target)
{
    int left = 0;
    int right = nums.size() - 1;
    int mid = 0;

    while (left <= right)
    {
        mid = left + (right - left) / 2;
        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] > target)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }

    return -1;
}

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target = 5;
    int index = binarySearch(nums, target);
    cout << "index: " << index << endl;

    return 0;
}
