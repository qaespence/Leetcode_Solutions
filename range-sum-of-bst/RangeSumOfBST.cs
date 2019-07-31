namespace LeetCode
{
    class TreeNode
    {
        public int val;
        public TreeNode left, right;

        public TreeNode(int data)
        {
            this.val = data;
            left = null;
            right = null;
        }
    }

    class BinaryTreeImp
    {
        public TreeNode root;
        public BinaryTreeImp()
        {
            root = null;
        }

        public TreeNode addNode(int data)
        {
            TreeNode newNode = new TreeNode(data);

            if (root == null)
            {
                root = newNode;
            }
            return newNode;
        }

        public void insertNode(TreeNode root, TreeNode newNode)
        {
            TreeNode temp;
            temp = root;

            if (newNode.val < temp.val)
            {
                if (temp.left == null)
                {
                    temp.left = newNode;
                } else
                {
                    temp = temp.left;
                    insertNode(temp, newNode);
                }
            } else if (newNode.val > temp.val)
            {
                if (temp.right == null)
                {
                    temp.right = newNode;
                } else
                {
                    temp = temp.right;
                    insertNode(temp, newNode);
                }
            }
        }
    }

    class RangeSumOfBST
    {
        public int RangeSumOfBSTSolution(TreeNode root, int L, int R) {

            if (root == null)
                return 0;
            if (L <= root.val && root.val <= R)
                return root.val + RangeSumOfBSTSolution(root.left, L, R) + RangeSumOfBSTSolution(root.right, L, R);

            return RangeSumOfBSTSolution(root.left, L, R) + RangeSumOfBSTSolution(root.right, L, R);
    }
    }
}
