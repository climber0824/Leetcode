class TrieNode {
public:
    bool isWord;
    TrieNode *children[26];

    // initialize TrieNode
    TrieNode() {
        isWord = false;
        memset(children, 0, sizeof(children));
    }
};


class Trie {
private:
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode *node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) {                 // if char not exists
                node->children[idx] = new TrieNode();   // add to trie
            }
            node = node->children[idx];
        }
        node->isWord = true;
    }
    
    bool search(string word) {
        TrieNode *node = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!node->children[idx]) {
                return false;
            }
            node = node->children[idx];
        }
        return node->isWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode *node = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!node->children[idx]) {
                return false;
            }
            node = node->children[idx];
        }
        return true;
    }
};
