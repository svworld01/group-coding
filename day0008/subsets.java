************************Auther --Akash **********************

class Solution {
    public List<List<Integer>> subsets(int[] nums) {
       List<List<Integer>> res = new ArrayList<>();

        for(int val : nums){
            List<Integer> v = new ArrayList<>();
            v.add(val);
            List<List<Integer>> r = new ArrayList<>();

            for(List<Integer> l : res){
                List<Integer> t  = new ArrayList<>(l);
                t.addAll(v);
                r.add(t);
            }
            res.addAll(r);
            res.add(v);
        }
        res.add(new ArrayList<>());
        return res;
}
}
