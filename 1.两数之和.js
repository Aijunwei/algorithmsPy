/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const len = nums.length;
    let i = 0;
    let findIndex;
    for (; i < len; i++) {
        findIndex = nums.lastIndexOf(target - nums[i]);
        if (findIndex > -1 && findIndex != i) {
            return [i, findIndex]
        }
    }
    return []
};
// @lc code=end

