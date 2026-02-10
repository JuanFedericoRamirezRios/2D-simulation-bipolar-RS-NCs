#include <iostream>
#include <cmath>
#include <random>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

class UTILS_FEDE {
private:

public:
    static bool LoadParams(string* params, string filePath, int numParams) {
        /*
        The format is "...:(space)value(line break)"
        Exms: 
        "Experimental data: K-63-RT_exp_corrct.dat" -> "K-63-RT_exp_corrct.dat"
        "N_LRS: 0.2" -> "0.2"
        "t_0 gener-recomb: 5e-06 s" -> "5e-06 s"
        */
        char arrChar[1000];
        ifstream inFile(filePath);
        if(!inFile) {
            cerr << "Error: File " << filePath << " does not exist" << endl;
            return false;
        }
        string numStr;
        int posI;
        int numParam = 0;
        while(!inFile.eof()) {
            inFile.getline(arrChar, 1000);
            numStr = "";
            if(arrChar[0] == '\0')
                continue;
            // initNum = false;
            for(int n = 0; n < 1000; n++) {
                if(arrChar[n] == ':') {
                    posI = n + 2;
                    break;
                }
            }
            for(int n = posI; n < 1000; n++) {
                if(arrChar[n] == '\0') {
                    params[numParam] = numStr;
                    numParam++;
                    break;
                } else {
                    numStr += arrChar[n];
                }
            }
        }
        inFile.close();
        
        if(numParam != numParams) return false;
        
        return true;
    };
    static streampos ObtainLastPosFile(string file) {
        streampos lastPosFile;
        ifstream inFile(file);
        if(!inFile) {
            cerr << "Error: File " << file << " does not exist" << endl;
            return lastPosFile;
        }
        string textLine;
        while (getline(inFile, textLine)) lastPosFile = inFile.tellg();
        inFile.close();
        return lastPosFile;
    };
    static string FloatToString(float num, int precision) {
        ostringstream oString;
        oString << std::setprecision(precision) << (num);
        return oString.str();
    };
    static string CppVersion() {
        long standard = __cplusplus;
        string version;
        if (standard == 199711L) version = "C++98/C++03";
        else if (standard == 201103L) version = "C++11";
        else if (standard == 201402L) version = "C++14";
        else if (standard == 201703L) version = "C++17";
        else if (standard == 202002L) version = "C++20";
        else if (standard == 202302L) version = "C++23";
        else if (standard > 202302L) version = "C++26 (or more actually)";
        else version = "Previous to C++98 or custom: " + to_string(standard) + " standard";
        return version;
    };
};
class RANDOM_FEDE {
private:
    ranlux24_base ranlux24engine;
    uniform_real_distribution<float> rndUniformFloat;
    uniform_int_distribution<int> rndUniformInt;

public:    
    RANDOM_FEDE(unsigned seed) {
        ranlux24engine.seed(seed);
    };
    float RndUnfFloat() {
        rndUniformFloat = uniform_real_distribution<float>(0.0f, 1.0f);
        return rndUniformFloat(ranlux24engine);
    };
    float RndUnfFloat(float start, float end) {
        if(start > end){ 
            rndUniformFloat = uniform_real_distribution<float>(end, start);
            return rndUniformFloat(ranlux24engine);
        }
        rndUniformFloat = uniform_real_distribution<float>(start, end);
        return rndUniformFloat(ranlux24engine);
    };
    int RndUnfInt(int start, int end) {
        if(start > end){ 
            rndUniformInt = uniform_int_distribution<int>(end, start);
            return rndUniformInt(ranlux24engine);
        }
        rndUniformInt = uniform_int_distribution<int>(start, end);
        return rndUniformInt(ranlux24engine);
    };


};