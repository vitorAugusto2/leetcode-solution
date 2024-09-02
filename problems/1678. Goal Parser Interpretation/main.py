class Solution:
    def interpret(command: str) -> str:
        arr = []
        
        for i in range(len(command)):
            if "G" in command[i]:
                arr.append("G")
            elif "(" in command[i]:
                if ")" in command[i+1]:
                    arr.append("o")
                else:
                    arr.append("al")
                    
        return "".join(arr)


"""
Another Approach
----------------

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
        
* Time complexity: O(n)
"""