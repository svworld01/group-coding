/*
Solution By - Saurabnh Verma
*/
class Solution {
    public int findMinFibonacciNumbers(int k) {
        //generate  fib series upto k
        List<Integer> list = new ArrayList<>();
        int n1= 1, n2 = 1, n3,i;
        list.add(1);
        list.add(1);
        while(list.get(list.size() -1) < k){
            n3 = n1 + n2;
            list.add(n3);
            n1 = n2;
            n2 = n3;
        }
        i = list.size() - 1;
        int count = 0;
        while(k!=0){
            int tmp = list.get(i);
            if(k >= tmp){
                count++;
                k -= tmp;
            }
            i--;
        }
        return count;
    }
}
