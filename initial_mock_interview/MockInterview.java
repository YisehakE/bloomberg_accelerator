package com.prep.bloomberg.accelerator.initial_mock_interview;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;


/*
 * Java solution to "find smallest kth element in BST"
 */
public class MockInterview {

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

    int temp = TreeNode.nodeDict.get(k);
    resetTreeNodeStatics();

    return temp;
  }

  public static int kthSmallestInteger(TreeNode root, int k) {
    findKthSmallest(root, 0, k);

    int temp = TreeNode.smallest;
    resetTreeNodeStatics();

    return temp;
  }


  public static int findKthSmallest(TreeNode node, int pos, int k) {
    if (node == null) { return pos; }

    int prevPos = findKthSmallest(node.left, pos, k);
    TreeNode.nodeDict.put(prevPos + 1, node.value);

    if (prevPos + 1 == k) { TreeNode.smallest = node.value; }

    if (TreeNode.smallest != Integer.MAX_VALUE) { return prevPos + 1;}

    return findKthSmallest(node.right, prevPos + 1, k);
  }

  public static void resetTreeNodeStatics(){

    TreeNode.nodeDict.clear();
    TreeNode.smallest = Integer.MAX_VALUE;
  }

  public static void testKthSmalllest(TreeNode root, int k, int value) {

    int actual1 = MockInterview.kthSmallestMap(root, k);
    int actual2 = MockInterview.kthSmallestInteger(root, k);

    System.out.println("MAP || #" + k + " smallest element || " + actual1);
    System.out.println("INT || #" + k + " smallest element || " + actual2);

    assert(actual1 == value);
    assert(actual2 == value);
  }


  public static void main(String[] args) {
 

    System.out.println("-------------------------------------- Case 1: Single node");
    /* 
              10
    */


    TreeNode root = new TreeNode(10, null, null);
    testKthSmalllest(root, 1, 10);


    // TODO: add more tests 
  }
}




