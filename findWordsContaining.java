class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        ArrayList<Integer> arrayList= new ArrayList<>();
        for (int i = 0; words.length > i; i++){
            if (words[i].contains(String.valueOf(x))) {
                arrayList.add(i);
            }
        }
        return arrayList;
    }
}
