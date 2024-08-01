
class Producto:
    def __init__(self, pCodigo, pNombre, pMarca, pPrecio, pExistencias, pProveedor):
        self.codigo = pCodigo
        self.nombre = pNombre
        self.marca = pMarca
        self.precio = pPrecio
        self.existencias = pExistencias
        self.proveedor = pProveedor

def listaProductos():
    global inventario

    for producto in inventario:
        print(f"Codigo: {producto.codigo}, Nombre: {producto.nombre}, Marca: {producto.marca}, Precio: {producto.precio}, Existencias: {producto.existencias}, Proveedor: {producto.proveedor["nombre"]}")

def agregarProducto():
    global inventario
    print("Insertar producto")
    codigo = input("Ingrese el codigo: ")
    nombre = input("Ingrese el nombre: ")
    marca = input("Ingrese la marca: ")
    precio = int(input("Ingrese el precio: "))
    existencias = int(input("Ingrese la existencias: "))
    codigoProveedor = input("Ingrese el codigo de proveedor: ")
    nombreProveedor = input("Ingrese el nombre de proveedor: ")
    paisProveedor = input("Ingrese el pais de proveedor: ")

    proveedor = {
        "codigo": codigoProveedor,
        "nombre": nombreProveedor,
        "pais": paisProveedor
    }

    producto = Producto(codigo, nombre, marca, precio, existencias, proveedor)
    inventario.append(producto)
def eliminarProducto():
    global lstProductos,producto
    codigo = int(input("Ingrese el codigo del producto que desea eliminar: "))
    for buscarC in lstProductos:
        if codigo == codigo:
            del [Producto]


def actualizarProducto(producto, nombre, cantidad):
    if nombre in producto:
        producto[nombre].cantidad += cantidad
        print(f"Producto de '{nombre}' actualizado.")
    else:
        print(f"Error: Producto '{nombre}' no encontrado en el inventario.")


def listaProducto():
    print("producto:")
    for producto in lstProductos.values():
        print(f" Codigo: {producto.codigo}, Nombre: {producto.nombre}, Marca: {producto.marca} Precio: {producto.precio}, Existencia: {producto.existencia}, Proveedor: {producto.proveedor}")

def buscarProducto():
    for c in lstProductos:
        print(f"Nombre: {c["nombre"]} Codigo: {c["codigo"]} Precio: {c["precio"]} \n")

    try:
        Producto= int(input("El producto buscado es: "))
        loEncontre = False

        for c in lstProductos:

            if buscarProducto() == c["codigo"]:
                print(f"Nombre: {c["nombre"]}")
                loEncontre = True
        else:
             print(f"Esta persona no cumple: {c["nombre"]}")

        if (not loEncontre):
            print(f"No cumple con el: {Producto}")
    except ValueError:
        print("El codigo es invalido. intentelo de nuevo")


def guardarInventario():
    global inventario

    textoInventario = ""
    for producto in inventario:
        textoProveedor = f"{producto.proveedor["codigo"]}:{producto.proveedor["nombre"]}:{producto.proveedor["pais"]}"
        textoProducto = f"{producto.codigo},{producto.nombre},{producto.marca},{producto.precio},{producto.existencias},{textoProveedor}"
        textoInventario += textoProducto

    with open("inventario.txt", "w") as archivo:
        archivo.write(textoInventario)


def cargarInventario():
    global inventario
    archivo = open("inventario.txt")
    for linea in archivo.readlines():
        atributosProducto = linea.split(",")
        atributosProveedor = atributosProducto[5].split(":")
        proveedor = {
            "codigo": atributosProveedor[0],
            "nombre": atributosProveedor[1],
            "pais": atributosProveedor[2]
        }

        producto = Producto(atributosProducto[0], atributosProducto[1], atributosProducto[2], int(atributosProducto[3]),
                            int(atributosProducto[4]), proveedor)

        inventario.append(producto)


def menuPrincipal():
    global inventario
    inventario = []
    while True:
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Lista de productos")
        print("5. Buscar producto")
        print("6. Cargar inventario")
        print("7. Guardar inventario")
        print("8. Salir")

        opcion = input("Elegir opcion: ")
        if opcion == "1":
            agregarProducto()
        elif opcion == "2":
            eliminarProducto()
        elif opcion == "3":
            actualizarProducto()
        elif opcion == "4":
            listaProductos()
        elif opcion == "5":
            buscarProducto()
        elif opcion == "6":
            cargarInventario()
        elif opcion == "7":
            guardarInventario()
        elif opcion == "8":
            break

if __name__=="__main__":
    menuPrincipal()