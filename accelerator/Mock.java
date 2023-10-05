package com.prep.bloomberg.accelerator;

import java.util.HashMap;
import java.util.Map;

public class Mock {

  public static class TreeNode {
    public int value;
    public TreeNode left;
    public TreeNode right;

    public static HashMap<Integer, Integer> nodeDict = new HashMap<>();
    public static int smallest = Integer.MAX_VALUE;

    public TreeNode(int value, TreeNode left, TreeNode right) {
      this.value = value;
      this.left = left;
      this.right = right;
    }
  }


  public static int kthSmallestMap(TreeNode root, int k) {
    findKthSmallest(root, 0, k);
    return TreeNode.nodeDict.get(k);
  }

  public static int kthSmallestInteger(TreeNode root, int k)


  public static int findKthSmallest(TreeNode node, int pos, int k) {
    if (node == null) { return pos; }

    int prevPos = findKthSmallest(node.left, pos, k);

    TreeNode.nodeDict.put(prevPos + 1, node.value);
    if (prevPos + 1 == k) { TreeNode.smallest = node.value; }

    return findKthSmallest(node.right, prevPos + 1, k);
  }


  public static void testKthSmalllest(TreeNode root, int k) {




    assert(k == 1);
    assert(k == 1);
  }


  public static void main(String[] args) {
    TreeNode leftSub = new TreeNode(5, new TreeNode(3, null, null), new TreeNode(9, null, null));
    TreeNode rightSub = new TreeNode(15,  new TreeNode(13, null, null), new TreeNode(17, null, null));

    TreeNode root = new TreeNode(10, leftSub, rightSub);

    int first = Mock.kthSmallest(root, 1);

    System.out.println("Smallest k: " + first);


  }
}




