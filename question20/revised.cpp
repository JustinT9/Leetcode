class Solution {
public:
    bool isValid(string s) {
        stack<char> valid; 
        if (s.size() % 2 != 0) return false; 
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '{' || s[i] == '[' || s[i] == '(') {
                valid.push(s[i]); 
            } else {
                if (valid.empty()) return false; 
                if ((s[i] == '}' && valid.top() != '{') || (s[i] == ']' && valid.top() != '[') 
                || (s[i] == ')' && valid.top() != '(')) return false; 
                valid.pop();  
            }
        } if (!valid.empty()) return false; 
        return true; 
    }
};