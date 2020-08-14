/*
Auther - Saurabh Verma
Problem link -   https://leetcode.com/problems/3sum/
Explanation - https://www.youtube.com/watch?v=qJSPYnS35SE
*/
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class Solution{
    public List<List<Integer>> threeSum(int[] a){
        List<List<Integer>> res = new LinkedList<>();
        Arrays.sort(a);
        for(int i=0; i<a.length-2; i++){
            if(i==0 || (i>0 && a[i] != a[i-1])){
                int low = i+1;
                int high = a.length - 1;
                int sum = -a[i];
                while(low < high){
                    if(a[low] + a[high] == sum){
                        res.add(Arrays.asList(a[i], a[low], a[high]));
                        while(low < high && a[low] == a[low+1]) low++;
                        while(low < high && a[high] == a[high-1]) high--;
                        low++;
                        high--;
                    }else if(a[low] +  a[high] > sum){
                        high--;
                    }else{
                        low++;
                    }
                }
            }
        }
        return res;
    }
}
