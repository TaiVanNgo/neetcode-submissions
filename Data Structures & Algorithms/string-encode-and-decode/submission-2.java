class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();

        //append them into the result
        for(String s : strs){
            res.append(s.length()).append("#").append(s);
        }

        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        
        int i = 0;

        while(i < str.length()){
            int j = i; //initialize the pointer j

            //find the index of the character'#'
            while(str.charAt(j) != '#'){
                j ++;
            }

            //move i to the actual first character of the word
            int length = Integer.parseInt(str.substring(i, j));
            
            i = j + 1;
           

            String word = str.substring(i, i + length);
            res.add(word);

            i += length;
        }

        return res;
    }
}
