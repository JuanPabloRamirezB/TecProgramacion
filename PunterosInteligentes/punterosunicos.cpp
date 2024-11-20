#include <iostream>
#include <memory>

class Punto {
    public:
        Punto() : x(0), y(0) {}//Constructor por defecto
        Punto(int x, int y) : x(x), y(y) {}

        void imprimir() {
            std::cout << "(" << x << ", " << y << ")" << std::endl;
        }

        private:
            double x{}, y{};
    };

int main() {

    //Los punteros únicos cuentan con la función std::make_unique 
    // que se puede utilizar en lugar del operadores new y que ofrece 
    // algunas ventajas como la seguridad de que no obtener nunca una 
    // pérdida de memoria cuando, en comparación, new si puede potencialmente 
    // fallar si el sistema no es capaz de reservar la memoria necesaria 
    // correctamente. 


    // std::unique_ptr<int> num {new int(100)};
    // std::unique_ptr<std::string> str{new std::string("Hola")};
    // std::unique_ptr<Punto> punto{new Punto(3, 7)};

    // Se recomienda utilizar esta forma siempre excepto si se necesita un 
    // destructor personalizado o se está adoptando un puntero sin formato:

    std::unique_ptr<int> num = std::make_unique<int>(100);
    std::unique_ptr<std::string> str = std::make_unique<std::string>("Hola");
    std::unique_ptr<Punto> punto = std::make_unique<Punto>(3, 7);

    std::cout << *num << " , " << *str << "\n";

    std::cout << num.get() << " , " << str.get() << "\n";

    punto->imprimir();

    std::cout << punto.get() << "\n";

    // Tal como hemos dicho un puntero único no se puede copiar, así 
    // previene que múltiples punteros apunten a la misma dirección de 
    // memoria:

    std::unique_ptr<int> num1 = std::make_unique<int>(100);
    //std::unique_ptr<int> num2 = num1; Error

    // Lo que sí permiten es transferir la propiedad mediante std::move, de 
    // manera que el puntero origanal pierde el acceso y lo transfiere a otro:
    std::cout << "num1.get(): " << num1.get() << std::endl;
    std::cout << " " << std::endl;

    //transferir la propiedad
    std::unique_ptr<int> num2 = std::move(num1);
    std::cout << "Transferir la propiedad " << std::endl;
    std::cout << "num1.get(): " << num1.get() << std::endl;
    std::cout << "num2.get(): " << num2.get() << std::endl;
    std::cout << " " << std::endl;

    //También permiten reiniciarlos y establecerlos a un puntero nullptr:
    std::cout << "Reiniciar puntero " << std::endl;
    num1 = std::make_unique<int>(100);
    std::cout << "num1.get(): " << num1.get() << std::endl;
    num1.reset();
    std::cout << "num1.get(): " << num1.get() << std::endl;

    // Es posible crear un arreglo de objetos dinámicos con std::make_unique, 
    // sin embargo no podemos inicializarlos directamente y esto solo 
    // funcionará si tenemos un constructor por defecto:
    
    // auto arr_ptr = std::make_unique<Punto[]>(3); \\Error
    // for(size_t i{0};i < 3; i++) { 
    //     arr_ptr[i].imprimir();
    // }

    auto arr_ptr = std::make_unique <Punto[]> (3); 
    //Es necesario un cosntructor por defecto para que funcione
    
    arr_ptr[0] = Punto(1, 2);
    arr_ptr[1] = Punto(3, 4);
    arr_ptr[2] = Punto(5, 6);

    for(size_t i{0};i < 3; i++) { 
        arr_ptr[i].imprimir();
    }

    return 0;
}