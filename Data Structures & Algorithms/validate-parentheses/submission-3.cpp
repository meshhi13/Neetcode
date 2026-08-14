#include <stack>
#include <unordered_map>

class Solution {
public:
    bool isValid(string s) {
        std::stack<char> paren_stack;
        std::unordered_map<char, char> paren_map = {{'{', '}'}, {'[', ']'}, {'(', ')'}};
        for (int i = 0; i < s.length(); i++ ){
            if (paren_map.contains(s[i])) {
                paren_stack.push(s[i]);
            }
            else {
                if (paren_stack.size() <= 0) {
                    return false;
                }
                if (paren_map[paren_stack.top()] == s[i]) {
                    paren_stack.pop();
                }
                else {
                    return false;
                }
            }
        }

        return paren_stack.size() == 0;
    }
};
