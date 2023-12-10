// It is horrible to code in C++

#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <sstream>
#include <iterator>

using namespace std;

namespace
{
    const string INPUT_FILE = "/mnt/home/tha10/git_repos/advent-of-code-23/input-4-0.txt";
}

int main()
{
    ifstream myfile(INPUT_FILE);
    string line, card_id, reference, input;
    vector<string> all_data; // Create vector to hold all data

    // Read input file line by line
    int counter = 0;

    while (getline(myfile, line))
    { // keep reading until end-of-file
        all_data.push_back(line);
        counter++;
    }
    myfile.close();

    cout << "Number of lines in file: " << counter << "\n";

    return 0;
}
