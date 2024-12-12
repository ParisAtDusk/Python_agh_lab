from collections import deque as dq

class TrieNode:
    def __init__(self):
        self.goto = {} 
        self.output = 0 
        self.fail = None

class Trie:
    def __init__(self):
        self.root = TrieNode() 
        self.state_count = 1  # States in the trie, starting with the root
    
    def add_word(self, word, index):
        """
        Adds a word to the trie and updates the output function for the corresponding node
        """
        current_node = self.root
        for char in word:
            if char not in current_node.goto:
                current_node.goto[char] = TrieNode()
                self.state_count += 1
            current_node = current_node.goto[char]
        # Set the output function at the last node for this word
        current_node.output |= (1 << index)
    
    def build_failure_function(self):
        """
        Builds the failure function using BFS and links the nodes to their failure state.
        """
        queue = dq()
        
        # Initialize the fail links for the depth-1 nodes (direct children of root)
        for char, node in self.root.goto.items():
            node.fail = self.root
            queue.append(node)
        
        # Breadth-First Search to build the failure function for all nodes
        while queue:
            current_node = queue.popleft()
            
            for char, child_node in current_node.goto.items():
                # Find the failure state for the child node
                fail_node = current_node.fail
                while fail_node is not None and char not in fail_node.goto:
                    fail_node = fail_node.fail
                
                # Set the fail link
                if fail_node is None:
                    child_node.fail = self.root
                else:
                    child_node.fail = fail_node.goto[char]
                
                # Merge the output from the fail state
                child_node.output |= child_node.fail.output
                
                queue.append(child_node)

class AhoCorasick:
    def __init__(self):
        self.trie = Trie()  # Trie to store the states and transitions

    def build_matching_machine(self, words):
        """
        Builds the Aho-Corasick automaton using the list of words
        """
        for index, word in enumerate(words):
            self.trie.add_word(word, index)
        
        # Build the failure function for the Trie
        self.trie.build_failure_function()

    def find_next_state(self, current_node, next_input):
        """
        Returns the next state (node) the machine will transition to
        """
        while current_node is not None and next_input not in current_node.goto:
            current_node = current_node.fail
        if current_node is None:
            return self.trie.root
        return current_node.goto[next_input]

    def search_words(self, words, text):
        """
        Finds all occurrences of the words in the given text using the Aho-Corasick automaton.
        """
        self.build_matching_machine(words)

        current_node = self.trie.root
        matches = []

        for i, char in enumerate(text):
            current_node = self.find_next_state(current_node, char)

            if current_node.output != 0:
                for j in range(len(words)):
                    if current_node.output & (1 << j):
                        matches.append((words[j], i - len(words[j]) + 1, i))

        return matches


if __name__ == "__main__":
    words = ["he", "she", "hers", "his", "here", "hi", "eel"]
    text = "ahisheresihestisheel"

    ac = AhoCorasick()
    matches = ac.search_words(words, text)

    for word, start, end in matches:
        print(f"Word '{word}' appears from index {start} to {end}")
