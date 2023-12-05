#include <iostream>
#include <cmath>
#include <functional>

static double f(double x) {
    return sin(x);
};

double integrate(double x1, double x2, std::function<double(double)> F) {
    return F(x2)-F(x1);
}

int main() {
    std::cout << integrate(0,1,f) << std::endl;
}