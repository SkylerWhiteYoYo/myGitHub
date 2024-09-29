#include <iostream>
#include <string>



int main() {
    std::string song("노래제목이 뭔지모름. 근데 뭔지알잖아");
    std::string singer("부른사람 ㅋ");

    std::cout << song + "이라는 노래를 부른사람은?" ;
    std:: cout << "(힌트 첫글자는 :" + singer[0] << " 입니다." <<std::endl;

    std:: string input;
    std::getline(std::cin,input);

}