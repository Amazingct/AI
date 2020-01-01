#include <iostream>
using namespace std;

class Neural
{
    private:
    float _sigmoid (float x)
    {
        return x*2;
    }
    float _sigmoid_deriv(float x)
    {
        return x/2;
    }
    float _value;
    

    public:
    float weights;
    Neural(int x)
    {
        //derive your initial random weights here
        _value=x;
    }
    void train(float x)
    {
        
        _value = x*_sigmoid(x);
        weights=x*_sigmoid_deriv(x);
    }

    float predict(float x)
    {
        return (x*_value*_sigmoid_deriv(x));
    }


};


Neural bola(2);
int main()
{
bola.train(5);
cout<<bola.weights<<"\n";

return 0;
}