#include <iostream>


int main() {

    //cria um arquivo sh
    system("touch exemplo.sh");
    //chama o arquivo sh como processo filho em nohup
    system("nohup bash exemplo.sh");
    
    return 0;

} 