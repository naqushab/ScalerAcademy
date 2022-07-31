/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    HashMap<Integer, List<Integer>> map = new HashMap<>();
    public List<List<Integer>> findLeaves(TreeNode root) {
        buildHeight(root);
        List<List<Integer>> result = new ArrayList<>();
        int height = 0;
        while(map.containsKey(height)){
            result.add(map.get(height));
            height++;
        }
        return result;
        
    }
    
    public int buildHeight(TreeNode root){
        if(root == null)
            return -1;
        int heightLeft = buildHeight(root.left);
        int heightRight = buildHeight(root.right);
        int heightRoot = Math.max(heightLeft, heightRight) + 1;
        if(!map.containsKey(heightRoot))
            map.put(heightRoot, new ArrayList<Integer>());
        map.get(heightRoot).add(root.val);
        return heightRoot;
    }
}