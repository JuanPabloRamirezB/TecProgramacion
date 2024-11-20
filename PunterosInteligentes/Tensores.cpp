#include <iostream>
#include <vector>
#include <memory>
class tensor{

    private:
        size_t lado1, lado2, lado3;
        std::unique_ptr<std::unique_ptr<std::unique_ptr<int[]>[]>[]> tensor3D;
        std::unique_ptr<std::unique_ptr<int[]>[]> tensor2D;
        std::unique_ptr<int[]> tensor1D;


    public:
        tensor(size_t lado1, size_t lado2, size_t lado3):
            lado1(lado1), lado2(lado2), lado3(lado3){
                tensor3D = std::make_unique<std::unique_ptr<std::unique_ptr<int[]>[]>[]>(lado1);
                for(size_t i = 0; i < lado1; i++){
                    tensor3D[i] = std::make_unique<std::unique_ptr<int[]>[]>(lado2);
                    for(size_t j = 0; j < lado2; j++){
                        tensor3D[i][j] = std::make_unique<int[]>(lado3);
                    }
                }
            }
        
        tensor(size_t lado1, size_t lado2):
            lado1(lado1), lado2(lado2){
                tensor2D = std::make_unique<std::unique_ptr<int[]>[]>(lado1);
                    for(size_t i = 0; i < lado1; i++){
                        tensor2D[i] = std::make_unique<int[]>(lado2);
                    }
            }

        tensor(size_t lado1):
            lado1(lado1){
                tensor1D = std::make_unique<int[]>(lado1);
            }

            // Método para acceder a los elementos del tensor
        int& at3D(size_t i, size_t j, size_t k){
            return tensor3D[i][j][k];
        }

        int& at2D(size_t i, size_t j){
            return tensor2D[i][j];
        }

        int& at1D(size_t i){
            return tensor1D[i];
        }

        void print3D() const {
            for (size_t i = 0; i < lado1; ++i) {
                for (size_t j = 0; j < lado2; ++j) {
                    for (size_t k = 0; k < lado3; ++k) {
                        std::cout << tensor3D[i][j][k] << " ";
                    }
                    std::cout << std::endl;
                }
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }

        void print2D() const {
            for (size_t i = 0; i < lado1; ++i) {
                for (size_t j = 0; j < lado2; ++j) {
                    std::cout << tensor2D[i][j] << " ";
                }
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }

        void print1D() const {
            for (size_t i = 0; i < lado1; ++i) {
                std::cout << tensor1D[i] << " ";
            }
            std::cout << std::endl;
        }

};

int main() {

    std::cout << "Tensor 3D" << std::endl;
    // Definir las dimensiones del tensor
    size_t dim1 = 3, dim2 = 3, dim3 = 3;
    
    // Crear un tensor de 3x3x3
    tensor tensor3d(dim1, dim2, dim3);
    

    // Inicializar el tensor con algunos valores
    for (size_t i = 0; i < dim1; ++i) {
        for (size_t j = 0; j < dim2; ++j) {
            for (size_t k = 0; k < dim3; ++k) {
                tensor3d.at3D(i, j, k) = i * dim2 * dim3 + j * dim3 + k;
            }
        }
    }

    // Imprimir el tensor
    tensor3d.print3D();

    std::cout << "Tensor 2D" << std::endl;

    tensor tensor2d(dim1, dim2);

    // Inicializar el tensor con algunos valores
    for (size_t i = 0; i < dim1; ++i) {
        printf("%d ", int(i));
        for (size_t j = 0; j < dim2; ++j) {
                tensor2d.at2D(i, j) = i * dim1 + j  ;            
        }
    }
    std::cout << std::endl;

    // Imprimir el tensor
    tensor2d.print2D();

    std::cout << "Tensor 1D" << std::endl;

    tensor tensor1d(dim1);
    // Inicializar el tensor con algunos valores
        for (size_t i = 0; i < dim1; ++i) {
                tensor1d.at1D(i) = i ; 
                
        }

    // Imprimir el tensor
    tensor1d.print1D();

    return 0;
}
