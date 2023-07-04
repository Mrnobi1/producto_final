class Cliente:
    """Clase que implementa cliente"""
    
    def __init__(self,numero_documento, razon_social, direccion, telefono) -> None:
        self.numero_documento = numero_documento
        self.razon_social = razon_social
        self.direccion = direccion
        self.telefono = telefono
        pass
    
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|" .format(self.numero_documento, 
                                       self.razon_social,
                                       self.direccion,
                                       self.telefono)
   
class Producto:
    """Clase que implementa productos"""
    def __init__ (self, codigo, nombre, precio)-> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        pass
    def convertir_a_texto(self):
        return "|{}|{}|{}|".format(self.codigo,
                                   self.nombre,
                                   self.precio)
        
class VentaDetalle:
    """ Clase que implementa detalle de una venta"""
    def __init__ (self, item, codigo, descripcion, cantidad, precio_unitario) -> None:
        self.item = item
        self.codigo = codigo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.base_imponible = (cantidad * precio_unitario) / 1.18
        self.igv = (cantidad * precio_unitario) - ((cantidad * precio_unitario) / 1.18)
        self.total = cantidad * precio_unitario
        pass
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.item,
                                                  self.codigo,
                                                  self.descripcion,
                                                  self.cantidad,
                                                  self.precio_unitario,
                                                  self.base_imponible,
                                                  self.igv,
                                                  self.total)
from cliente import Cliente
from ventas_detalle import VentaDetalle

class Venta:
    """ Clase que implementa venta """
    def __init__(self, numero, cliente:Cliente, detalle:VentaDetalle=[], total=0 )-> None:
        self.serie = "F005"
        self.numero = numero
        self.cliente:Cliente = cliente
        self.detalle:list = detalle
        self.base_imponible = total / 1.18
        self.igv = total - (total/ 0.18)
        self.total = total
        pass
    
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|{}|" .format(self.serie,
                                             self.numero,
                                             self.cliente.razon_social,
                                             round(self.base_imponible,2),
                                             round(self.igv, 2),
                                             round(self.total, 2))
        

from cliente import Cliente
from producto import Producto
from ventas_detalle import VentaDetalle
from venta import Venta
# CRUD CLIENTE

data_clientes:list = [{"numero_documento": "72457858",
                       "razon_social": "jack denys",
                       "direccion" : "Jr tupac",
                       "telefono" : "984562145"},
                      {"numero_documento": "64545245",
                       "razon_social": "jazel",
                       "direccion" : "Jr ares",
                       "telefono" : "931313131"},
                       {"numero_documento": "1234578",
                       "razon_social": "Elias",
                       "direccion" : "Jr and",
                       "telefono" : "934547898"}]

clientes:Cliente = []
def cargar_datos_clientes():
    for data in data_clientes:
        clientes.append(Cliente(data["numero_documento"],
                                data["razon_social"],
                                data["direccion"],
                                data["telefono"]))
        return clientes


def insertar_cliente():
    numero_documento:str = input("Ingrese el numero de documento del cliente: ")
    razon_social:str = input("Ingrese la razon social del Cliente: ")
    direccion:str = input("Ingrese la direccion del cliente: ")
    telefono:str = input("Ingrese el telefono del Cliente: ")
    clientes.append(Cliente(numero_documento, razon_social, direccion, telefono))  
    return clientes
      
def listar_clientes():
    print("==========================================================")
    print("**================== LISTA DE CLIENTES==================**")
    print("==========================================================")
    print(" |NUMERO DE DOC.| RAZON SOCIAL | DIRECCION ° TELEFONO |")
    for cliente in clientes:
        print("---------------------------------------------------------")
        print(cliente.convertir_a_texto())
    return clientes

def buscar_cliente():
    numero_documento:str=input("Ingrese el numero de documento para buscar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento == numero_documento:
            print(cliente.convertir_a_texto())
            listar_clientes()
            return cliente

def editar_cliente():
    numero_documento:str=input("Ingrese el numero de documento para buscar cliente: ")
    for cliente in clientes:
        if cliente.numero.documento == numero_documento:
            print(cliente.convertir_a_texto())
            cliente.razon_social = input("INgrese nueva razon social del CLiente: ")
            cliente.direccion = input("ingrese nueva direccion del cliente: ")            
            cliente.telefono = input("Ingrese nuevo numero del cliente: ")
            listar_clientes()
            return cliente
        
def eliminar_cliente():
    numero_documento:str = input("ingrese el numero de documento del Cliente a eliminar: ")
    for indice, cliente in enumerate(clientes):
        if cliente.numero_documento == numero_documento:
            clientes.pop(indice)
            
            
#CRUD PRODUCTO

data_productos:list = [{"codigo": "001",
                       "nombre": "salteña",
                       "precio" : 2.00},
                       {"codigo": "002",
                       "nombre": "agua",
                       "precio" : 1.50},
                       {"codigo": "003",
                       "nombre": "gaseosa de 2 litros",
                       "precio" : 8.00}]

productos:Producto = []
def cargar_datos_productos():
    for data in data_productos:
        productos.append(Producto(data["codigo"],
                                  data["nombre"],
                                  data["precio"]))
        return productos


def insertar_productos():
    codigo:str = input("Ingrese el codigo del Producto: ")
    nombre:str = input("Ingrese el nombre del Producto: ")
    precio:str = input("Ingrese el precio del Producto: ")
    productos.append(Producto(codigo, nombre, precio))  
    return productos
      
def listar_productos():
        for producto in productos:
            print(producto.convertir_a_texto())
            return productos

def buscar_productos():
    codigo:str=input("Ingrese el codigo para buscar Producto: ")
    for producto in productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_texto())
            listar_productos()
            return producto

def editar_producto():
    codigo:str=input("Ingrese el codigo para editar el Producto: ")
    for producto in productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_texto())
            producto.nombre = input("ingrese nuevo nombre del Producto: ")            
            producto.precio = input("Ingrese nuevo precio del Producto: ")
            listar_productos()
            return producto
        
def eliminar_producto():
    codigo:str = input("ingrese el codigo del producto a elmiinar: ")
    for indice, producto in enumerate(productos):
        if producto.codigo == codigo:
            productos.pop(indice)
            
# CRUD VENTA
ventas:Venta = []
venta_detalles:VentaDetalle = []
def agregar_productos():
    producto:Producto = buscar_productos()
    cantidad:float = float(input("Ingrese la cantidad del producto: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,
                                       producto.codigo,
                                       producto.nombre,
                                       cantidad,
                                       producto.precio))
    return venta_detalles
    

def insertar_venta():
    cliente:Cliente = buscar_cliente()
    continuar_venta:bool=True
    while continuar_venta:
        opcion:str = input("1: para agregar producto, 2 para guardar venta: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                continuar_venta=False
    total:float=0
    for venta_detalle in venta_detalles:
        total = total + venta_detalle.total
    ventas.append(Venta(len(ventas)+1, cliente, venta_detalles, total))
    venta_detalles=[]
    return ventas

def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_texto())
        return ventas
    
def buscar_venta():
    numero:int = int(input("Ingrese el numero de la venta para buscar: "))
    for venta in ventas:
        if venta.numero == numero:
            print("==============** FACTURA **==============")
            print("================ CLIENTE ================")
            print(venta.cliente.numero_documento)
            
            print(venta.convertir_a_texto())
            print("============================")
            for venta_detalle in venta.detalle:
                print(venta_detalle.convertir_a_texto())
            return venta    
        

def menu_texto():
    print("===============MENU==============")
    print("=======CRUD CLIENTE========")
    print("1: para insertar Cliente: ")
    print("2: para listar Cliente: ")
    print("3: para buscar Cliente: ")
    print("4: para editar Cliente: ")
    print("5: para eliminar Cliente")
    print("=======CRUD PRODUCTO========")
    print("6: para insertar Producto: ")
    print("7: para listar Producto: ")
    print("8: para buscar Producto: ")
    print("9: para editar Producto: ")
    print("10: para eliminar Producto: ")
   
    print("=======CRUD VENTA========")
    print("11: para Insertar Venta: ")
    print("12: para Listar Venta: ")
    print("13: para Buscar Venta: ")
    
    print("30: para terminar el programa: ")


def menu ():
    continuar:bool = True
    while continuar:
        menu_texto()
        opcion:str = input("Ingrese la opcion: ")
    
        match opcion:
            case "1":
                insertar_cliente()
            case "2":
                listar_clientes()
            case "3":
                buscar_cliente()
            case "4":
                editar_cliente()
            case "5":
                eliminar_cliente()
            case "6":
                insertar_productos()
            case "7":
                listar_productos()
            case "8":
                buscar_productos()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta()
            case "30":
                print("salir programa")
                continuar=False
                

def main():
    cargar_datos_clientes()
    cargar_datos_productos()
    menu()
    print("iniciando programa")
    return True
if __name__ == '__main__':
    main()                        