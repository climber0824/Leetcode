class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        append the beginWord to queue
        find 1 diff word in wordList
        -> remove from wordList
        -> append to queue, length+=1
        -> until find endword        
        """
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        q = deque([(beginWord, 1)])
        chars = "abcdefghijklmnopqrstuvwxyz"        
        while q:
            word, leng = q.popleft()            
            if word == endWord:
                return leng
            for i in range(len(word)):
                for c in chars:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        q.append([nextWord, leng + 1])
        return 0
