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
    static bool LoadParams(string* params, string resultsFile, int numParams, bool showParams) {
        /*
        The format is "...:(space)value(line break)"
        Exms: 
        "Experimental data: K-63-RT_exp_corrct.dat" -> "K-63-RT_exp_corrct.dat"
        "N_LRS: 0.2" -> "0.2"
        "t_0 gener-recomb: 5e-06 s" -> "5e-06 s"
        */
        char arrChar[1000];
        ifstream inFile(resultsFile);
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
        if(!showParams) return true;

        cout << "The parameters are:" << endl;
        for(int n = 0; n < numParam; n++) {
            cout << params[n] << endl;
        }
        return true;

    };
    static streampos ObtainLastPosFile(string file) {
        streampos lastPosFile;
        ifstream inFile(file);
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