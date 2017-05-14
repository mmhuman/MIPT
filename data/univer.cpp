#include <bits/stdc++.h>

using namespace std;

#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)

int next_number(string& st, int& i) {
    while (!(st[i] >= '0' && st[i] <= '9')) {
        ++i;
    }
    int number = 0;
    while (st[i] >= '0' && st[i] <= '9') {
        number = number * 10 + (st[i] - '0');
        ++i;
    }
    return number;
}

int main() {
    fin("universities.txt");
    fout("neerc2017.txt");
    string st, prev_st;
    while (getline(cin, st)) {
        if (st.size() < 40) {
            prev_st = st;
            continue;
        }
        string univer = "";
        int i = 0;
        while (st[i] == ' ' || (st[i] >= '0' && st[i] <= '9')) {
            ++i;
        }
        while (!((st[i] >= '0' && st[i] <= '9')) && st[i] != '(') {
            univer += st[i];
            ++i;
        }
        if (univer.size() < 10)
            continue;

        while (univer[(int)univer.size() - 1] == ' ') {
            univer.pop_back();
        }

        int number;
        if (st[i] >= '0' && st[i] <= '9') {
            number = next_number(st, i);
        } else {
            number = 1;
        }

        string contestant[3];
        contestant[0] = "";
        contestant[1] = "";
        contestant[2] = "";

        for (int j = 0; j <= 2; ++j) {
            while (!((st[i] >= 'a' && st[i] <= 'z') || (st[i] >= 'A' && st[i] <= 'Z'))) {
                ++i;
            }
            while ((st[i] >= 'a' && st[i] <= 'z') || (st[i] >= 'A' && st[i] <= 'Z')) {
                contestant[j] += st[i];
                ++i;
            }
        }

        int i0 = 0;
        int problems_solved, x;
        while (i0 < prev_st.size()) {
            problems_solved = x;
            x = next_number(prev_st, i0);
        }
        cout << univer << ";" << number << ";" << problems_solved << ";" <<
            contestant[0] << ";" << contestant[1] << ";" << contestant[2] << endl;
    }
    return 0;
}