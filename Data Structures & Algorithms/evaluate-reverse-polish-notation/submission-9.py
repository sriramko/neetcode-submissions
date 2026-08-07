class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["+","-","*","/"])
        def calculate(char: str, stack: List[str]) -> None:
            int1 = str(stack[-1])
            int2 = str(stack[-2])
            string = int2 + char + int1
            result = eval(string)
            if type(result) == float:
                result = int(result)
            stack.pop()
            stack.pop()
            stack.append(result)
            return
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                calculate(token, stack)
        return int(stack[0])
            
