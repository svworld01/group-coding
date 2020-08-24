**************Auther:Akash**********

class Solution {
    public String reverseVowels(String s) {

    ArrayList<Character> vowels= new ArrayList<Character>();
    vowels.add('a');
    vowels.add('e');
    vowels.add('i');
    vowels.add('o');
    vowels.add('u');
    vowels.add('A');
    vowels.add('E');
    vowels.add('I');
    vowels.add('O');
    vowels.add('U');
 
    char[] resultString = s.toCharArray();
 
    int i=0; 
    int j=s.length()-1;
 
    while(i<j){
        if(!vowList.contains(resultString[i])){
            i++;
            continue;
        }
 
        if(!vowels.contains(resultString[j])){
            j--;
            continue;
        }
 
        char t = resultString[i];
        resultString[i]=resultString[j];
        resultString[j]=t;
 
        i++;
        j--; 
    }
 
    return new String(resultString);
}
    
}
