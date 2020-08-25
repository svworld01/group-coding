*****************//Approch Explain link:https://www.youtube.com/watch?v=iSBgmQCTN8g
*******Akash*************8

class Solution {
    public int[][] diagonalSort(int[][] mat) {
       HashMap<Integer,List<Integer>> map = new HashMap<>();
       int m=mat.length;
        int n=mat[0].length;
        
        //Fill Hash Map With Key And Values
        for(int i = 0;i<m;i++){
            for(int j=0;j<n;j++){
                int diff = i-j;
                List<Integer> list = map.getOrDefault(diff,new ArrayList<Integer>());
                //#getOrDefault Method:Returns the value to which the specified key is mapped, or defaultValue if this map contains no mapping for the key.
                
                list.add(mat[i][j]);
                map.put(diff,list);
            }
        }
        for(Integer key: map.keySet()){
            int i=0,j=0;
            if(key>0) i=key;
            if(key<0) j=-key;
            List<Integer> list = map.get(key);
            
            //sort The List
            Collections.sort(list);
            //Insert The Value In The matrix 
            for(Integer value:list)
                mat[i++][j++] = value;
        }
        return mat;
    }
}
