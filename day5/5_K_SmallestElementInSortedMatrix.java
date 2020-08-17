/*
Auther - Saurabh Verma
Problem link - 
Aproach - Using Priority Queue to storing values
*/
class Solution {
  //node for priority queue for storing value along with row and col
    class Node {
        int x;
        int y;
        int val;
        public Node(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }

    public int kthSmallest(int[][] matrix, int k) {
       
        int n = matrix.length;
        //creating a priority queue with custom comparator for Node class
        Queue<Node> queue = new PriorityQueue<Node>(new Comparator<Node>(){ 
            public int compare(Node a, Node b){
                return a.val - b.val;
            }
        });
        
        // Initialize the queue with head elements
        for (int i = 0; i < n; i++) {
            queue.offer(new Node(i, 0, matrix[i][0]));
        }
        //poll one node and if it is not desired move to next column valuea and decrease k
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            if (k == 1) {
                return node.val;
            }
            if (node.y + 1 < n) {
                queue.offer(new Node(node.x, node.y + 1, matrix[node.x][node.y + 1]));
            }
            k--;
        }

        return 0;
    }
}
