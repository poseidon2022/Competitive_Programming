class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val 
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = Node(homepage)

    def visit(self, url: str) -> None:
        added = Node(url)
        self.node.next = added
        added.prev = self.node
        self.node = added

    def back(self, steps: int) -> str:
        
        while steps>0 and self.node.prev:
            self.node = self.node.prev
            steps-=1
        
        return self.node.val



    def forward(self, steps: int) -> str:
        
        while steps>0 and self.node.next:
            self.node = self.node.next
            steps-=1
        
        return self.node.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)