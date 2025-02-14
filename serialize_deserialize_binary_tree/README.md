## Serialize and Deserialize Binary Tree

### Description
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

A function to serialize and deserialize a binary tree.
 Example
Input:
Binary Tree:
      1
     / \
    2   3
       / \
      4   5
      Serialized String: "1,2,3,null,null,4,5"
Deserialized Tree: Same as the input tree.

### File
- [serialize_deserialize_binary_tree.py](serialize_deserialize_binary_tree.py)
Run the code in VS Code by pressing F5 or by clicking the "Run" button in the top-right corner.
Verify the output:
Serialized Tree: 1,2,null,null,3,4,null,null,5,null,null,
Deserialized Tree Pre-order: 1 2 null null 3 4 null null 5 null null
