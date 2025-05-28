#include<iostream>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

class Solution {
public:

    std::vector<std::string> res;

    void backtrack(std::string s, int last_i, int last_j, std::vector<char> p) {
        int bal = 0;

        for (int k = last_i; k < s.length(); k++) {
            if (s[k] == p[0])
                bal++;
            else if (s[k] == p[1])
                bal--;
            
            if (bal >= 0) {
                continue;
            }
            
            for (int x = last_j; x <= k; x++) {
                if (s[x] == p[1] && (x == last_j || s[x-1] != p[1])) {
                    std::string next_s = s.substr(0, x) + s.substr(x + 1);
                    backtrack(next_s, k, x, p);
                }
            }
            return;
        }

        std::reverse(s.begin(), s.end());

        if (p[0] == '(') {
            backtrack(s, 0, 0, {')', '('});
        } else {
            res.push_back(s);
        }
    }

    std::vector<std::string> removeInvalidParentheses(std::string s) {
        backtrack(s, 0, 0, {'(', ')'});
        return res;
    }
};