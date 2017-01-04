class TrieNode {
    
    public char nodeValue;
    public Dictionary<char, TrieNode> nodeChildren;
    public bool isLeaf;
    
    // Initialize your data structure here.
    public TrieNode() {
        nodeValue = '\0';
        nodeChildren = new Dictionary<char, TrieNode>();
        isLeaf = false;
    }
    
    
}

public class Trie {
    private TrieNode root;
    private TrieNode parentNode;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void Insert(String word) {
        
        if(string.IsNullOrEmpty(word))
        {
            return;
        }
        var parent = root;
        var children = root.nodeChildren;
        int index = 0;
        TrieNode childNode;
        do
        {
            if(children.TryGetValue(word[index], out childNode))
            {
                children = childNode.nodeChildren;
            }
            else
            {
                childNode = new TrieNode();
                childNode.nodeValue = word[index];
                parent.nodeChildren.Add(word[index], childNode);
            }
            
            parent = childNode;
            children = childNode.nodeChildren;
            index++;
            
        }while(index < word.Length);
        
        childNode.isLeaf = true;
        //get the dc for root , create a new trienode with that letter and add it as child of root
        //go to next work, create a new trienode
    }

    // Returns if the word is in the trie.
    public bool Search(string word) {
        
       if(StartsWith(word) && parentNode.isLeaf)
           return true;
        
        return false;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public bool StartsWith(string word) {
        
        if(string.IsNullOrEmpty(word))
        {
            return false;
        }
        
        int index = 0;
        parentNode = root;
        var children = root.nodeChildren;
        TrieNode childNode;
        
        while(index < word.Length)
        {
            char c = word[index];
            if(children.TryGetValue(c, out childNode))
            {
                parentNode = childNode;
                children = childNode.nodeChildren;
            }
            else
            {
                return false;
            }
            index++;
        }
        
        return true;
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.Insert("somestring");
// trie.Search("key");