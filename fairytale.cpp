#include <iostream>
#include <string>
#include <map>
using namespace std;

#define endl "\n"

bool isVowel(char c) {
    string vowels = "AEIOU";
    for (int i = 0;i < vowels.length();i++) {
        if (c == vowels[i]) {
            return true;
        }
    }
    return false;
}

void solve() {
    int testCase = 1;
    cin >> testCase;
    int indexI = 1;
    while (testCase--) {
        string s;
        cin >> s;
        map<char, int> arr;
        int v = 0, cons = 0;
        for (int i = 0;i < s.length();i++) {
            arr[s[i]]++;
            if (isVowel(s[i])) {
                v++;
            }
            else {
                cons++;
            }
        }

        if (v == 0 || cons == 0) {
            int maxOccur = 0, sum = 0;
            for (auto i : arr) {
                if (i.second > maxOccur) {
                    maxOccur = i.second;
                }
                sum += i.second;
            }
            int res = sum - maxOccur;
            if (res == 0) {
                cout << "Case #" << indexI << ": " << 0 << endl;
                indexI++;
            }
            else {
                cout << "Case #" << indexI << ": " << sum << endl;
                indexI++;
            }

            continue;
        }

        bool shouldBeVowel = (v <= cons) ? true : false;

        int maxOccur = 0;
        for (auto i : arr) {
            if (isVowel(i.first) == shouldBeVowel) {
                if (i.second > maxOccur) {
                    maxOccur = i.second;
                }
            }
        }

        int sum = 0;
        for (auto i : arr) {
            if (isVowel(i.first) == shouldBeVowel) {
                sum += 2 * i.second;
            }
            else {
                sum += i.second;
            }
        }
        cout << "Case #" << indexI << ": " << sum - 2 * maxOccur << endl;
        indexI++;
    }
}

signed main() {
    solve();
    return 0;
}