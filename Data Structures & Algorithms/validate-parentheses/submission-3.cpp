class Solution {
public:
    bool isValid(string s) {
        stack<char> verify;
        for (char c : s) {
            if (c == '[' || c == '(' || c == '{') {
                verify.push(c);
                continue;
            } else if (verify.empty()) return false;
            if (c == ']' && verify.top() != '[') {
                return false;
            } else if (c == ')' && verify.top() != '(') {
                return false;
            } else if (c == '}' && verify.top() != '{') {
                return false;
            }
            verify.pop();
        }
        if (verify.empty()) return true;
        else return false;
    }
};
