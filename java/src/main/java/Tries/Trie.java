package main.java.Tries;

public class Trie {
    // 存储无意义字符
    private TrieNode root = new TrieNode('/');
    //往Trie树中插入一个字符串
    public void insert(char[] text) {
        TrieNode p = root;
        for (char c : text) {
            int index = c - 'a';
            if (p.children[index] == null) {
                TrieNode newNode = new TrieNode(c);
                p.children[index] = newNode;
            }
            p = p.children[index];
        }
        p.isEndingChar = true;
    }
    // 在Trie树中查找一个字符串
    public boolean find(char[] pattern) {
        TrieNode p = root;
        for (char c : pattern) {
            int index = c - 'a';
            if (p.children[index] == null) {
                //不存在pattern
                return false;
            }
            p = p.children[index];
        }
        //不能完全匹配，只是前缀
        if(p.isEndingChar == false ) return false;
        else return true; //找到pattern
    }
}
