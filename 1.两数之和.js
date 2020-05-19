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
    const map = {};
    let i = 0;
    let val;
    while (i < nums.length) {
        val = target - nums[i];
        if (map[val] !== undefined) {
            return [map[val], i];
        }
        map[nums[i]] = i;
        i++;
    }
    return []
};
// @lc code=end

