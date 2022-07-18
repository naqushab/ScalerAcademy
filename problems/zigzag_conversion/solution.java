class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1)
            return s;
        StringBuilder sb = new StringBuilder();
        ArrayList<ArrayList<Character>> rowWiseText = new ArrayList<>();
        for(int i = 0; i < numRows; i++)
            rowWiseText.add(new ArrayList<>());
        
        int row = 0;
        boolean goingDown = true;
        for(int i = 0; i < s.length(); i++){
            rowWiseText.get(row).add(s.charAt(i));
            if(goingDown){
                if(row == numRows-1){
                    goingDown = false;
                    row--;
                }
                else
                    row++;
            }
            else{
                if(row == 0){
                    goingDown = true;
                    row++;
                }
                else
                    row--;
            }
            
           
        }
        for(int i = 0; i < rowWiseText.size(); i++){
            for(Character ch : rowWiseText.get(i)){
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}