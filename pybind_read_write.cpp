#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void pybind_read_write(string input_path, string output_path) {
    ifstream input;
    input.open(input_path);
    if (input.fail())
    {
        cout << "Failed to open " << input_path << endl;
        return;
    }
    input.close();

    string line;
    vector<string> book;

    while (getline(input, line))
    {
    	book.push_back(line);
    }

    ofstream output_file (output_path);
    vector<string>::size_type i = 0;
    while (output_file.is_open() && i < book.size())
    {
        output_file << book.at(i) << "\n";
        i++;
        
    }
    output_file.close();
    
}

