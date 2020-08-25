/*
*************************Auther Akash**************

Approch:
Loop till Exist Minimum 10 Char String In given String From i****

create  Array Lisyt For Result And Use HashSet Object For Storing Uniqe String And CHeck if It Is Avalilevle in Resut Array List Or Not If Those 10 char String NOt Available Then Add In The Result .
*/

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> list=new ArrayList();
        Set<String> uniqeSet=new HashSet();
        if(s==null||s.length()<10)
            return list;
        
        for(int i=0;i<=s.length()-10;i++)
        {
            if(!uniqeSet.add(s.substring(i,i+10))&&!list.contains(s.substring(i,i+10)))
            list.add(s.substring(i,i+10));
        }
       
        return list;
    }
}
