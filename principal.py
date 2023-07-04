from cliente import Cliente
from producto import Producto
from venta_detalle import VentaDetalle
from venta import Venta
from pdf_clientes import PDFGenerator

# CRUD CLIENTE

data_clientes:list = [
    {"numero_documento":"72405377",
    "razon_social":"Jack Denys Mamani Ramirez",
    "direccion":"Jr. Tacna 368",
    "telefono":"931208902"},
    {"numero_documento":"72405344",
    "razon_social":"Paul Jhon Coaquira Ramos",
    "direccion":"Av. El sol 343",
    "telefono":"937773737"},
    {"numero_documento":"74744578",
    "razon_social":"Juan Anthony Rojas Sanca",
    "direccion":"Jr. Ramon Castilla 654",
    "telefono":"981639021"} ]

clientes: Cliente = []

def cargar_datos_clientes():
    for data in data_clientes:
        clientes.append(Cliente(
            data["numero_documento"],
            data["razon_social"],
            data["direccion"],
            data["telefono"]
        ))
    return clientes

def insertar_cliente():
    numero_documento: str = input("Ingrese el numero de documento del cliente: ")
    razon_social: str = input("Ingrese la razon social del cliente: ")
    direccion: str = input("Ingrese la direccion del cliente: ")
    telefono: str = input("Ingrese telefono del cliente: ")
    clientes.append(Cliente(numero_documento, razon_social, direccion, telefono))
    return clientes

def listar_clientes():
    print("==========================================================")
    print("**================== LISTA DE CLIENTES ==================**")
    print("==========================================================")
    print("..|NUMERO DE DOC.| RAZON SOCIAL | DIRECCION | TELEFONO |...")
    print("...........................................................")
    for cliente in clientes:
        print("---------------------------------------------------------")
        print(cliente.convertir_a_texto())
    return clientes

def buscar_cliente():
    numero_documento: str = input("Ingrese el numero de documento para buscar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento == numero_documento:
            print(cliente.convertir_a_texto())
            return cliente

def editar_cliente():
    listar_clientes()
    numero_documento: str = input("Ingrese el numero de documento para editar cliente: ")
    for cliente in clientes:
        if cliente.numero_documento == numero_documento:
            print(cliente.convertir_a_texto())
            cliente.razon_social = input("Ingrese nueva razon social del cliente: ")
            cliente.direccion = input("Ingrese nueva direccion del cliente: ")
            cliente.telefono = input("Ingrese nuevo telefono del cliente: ")
    listar_clientes()
    return clientes

def eliminar_cliente():
    listar_clientes()
    numero_documento: str = input("Ingrese el numero de documento del cliente para eliminar: ")
    for indice, cliente in enumerate(clientes):
        if cliente.numero_documento == numero_documento:
            clientes.pop(indice)
    listar_clientes()
    return clientes
def reporte_pdf_clientes():
    data:list=[]
    for cliente in clientes:
        data.append( {"numero_documento": cliente.numero_documento, "razon_social": cliente.razon_social, "direccion": cliente.direccion, "telefono": cliente.telefono},)
    reporte:PDFGenerator=PDFGenerator("reporte_clientes.pdf",data)
    reporte.generar_reporte_clientes()


# CRUD PRODUCTO

data_productos: list = [
    {"codigo":"H001",
    "nombre":"Delicia de Fresa",
    "precio":8.50},
    {"codigo":"H002",
    "nombre":"Cremoso Chocolate",
    "precio":9.75},
    {"codigo":"H003",
    "nombre":"Vainilla Tentación",
    "precio":7.90},
    {"codigo":"H004",
    "nombre":"Nuez y Caramelo",
    "precio":10.25},
    {"codigo":"H005",
    "nombre":"Mango Tropical",
    "precio":8.95},
    {"codigo":"H006",
    "nombre":"Menta Refrescante",
    "precio":7.50},
    {"codigo":"H007",
    "nombre":"Dulce de Leche Suave",
    "precio":9.25},
    {"codigo":"H008",
    "nombre":"Avellana Crocante",
    "precio":10.50},
    {"codigo":"H009",
    "nombre":"Limón Exótico",
    "precio":7.25},
    {"codigo":"H0010",
    "nombre":"Coco Helado",
    "precio":8.75},
    {"codigo":"H0011",
    "nombre":"Nieve de fresa con trozos de chocolate",
    "precio":12.00},
    {"codigo":"H0012",
    "nombre":"Helado de vainilla con caramelo salado",
    "precio":14.00},
    {"codigo":"H0013",
    "nombre":"Sorbete de limón",
    "precio":10.00},
    {"codigo":"H0014",
    "nombre":"Helado de chocolate oscuro con almendras",
    "precio":16.00},
    {"codigo":"H001 5",
    "nombre":"Nieve de menta con chispas de chocolate",
    "precio":12.00},
    {"codigo":"H0016",
    "nombre":"Helado de dulce de leche con nueces",
    "precio":14.00},
    {"codigo":"H0017",
    "nombre":"Sorbete de frutas tropicales",
    "precio":10.00},
    {"codigo":"H0018",
    "nombre":"Helado de café con chocolate blanco",
    "precio":16.00},
    {"codigo":"H0019",
    "nombre":"Nieve de mango con trozos de fruta",
    "precio":12.00},
    {"codigo":"H0020",
    "nombre":"Helado de pistacho con trozos de almendra",
    "precio":14.00}]

productos: Producto = []

def cargar_datos_productos():
    for data in data_productos:
        productos.append(Producto(data["codigo"], data["nombre"], data["precio"]))
    return productos

def insertar_producto():
    codigo: str = input("Ingrese codigo del producto: ")
    nombre: str = input("Ingrese nombre del producto: ")
    precio: str = input("Ingrese precio del producto: ")
    productos.append(Producto(codigo, nombre, precio))
    return productos

def listar_productos():
    for producto in productos:
        print(producto.convertir_a_texto())
    return productos

def buscar_producto():
    codigo: str = input("Ingrese codigo del producto para buscar producto: ")
    for producto in productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_texto())
            return producto

def editar_producto():
    listar_productos()
    codigo: str = input("Ingrese codigo del producto para editar producto: ")
    for producto in productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_texto())
            producto.nombre = input("Ingrese nuevo nombre del producto: ")
            producto.precio = float(input("Ingrese nuevo precio del producto: "))
           
    listar_productos()
    return productos

def eliminar_producto():
    listar_productos()
    codigo: str = input("Ingrese codigo del producto para eliminar producto: ")
    for indice, producto in enumerate(productos):
        if producto.codigo == codigo:
            productos.pop(indice)
    listar_productos()
    return productos

# CRUD VENTA

ventas: Venta = []
venta_detalles: VentaDetalle = []

def agregar_productos():
    producto: Producto = buscar_producto()
    cantidad: float = float(input("Ingrese la cantidad del producto: "))
    venta_detalles.append(VentaDetalle(
        len(venta_detalles) + 1,
        producto.codigo,
        producto.nombre,
        cantidad,
        producto.precio
    ))
    return venta_detalles


def insertar_venta():
    cliente: Cliente = buscar_cliente()
    continuar_venta: bool = True
    while continuar_venta:
        opcion: str = input("1: para agregar producto, 2 para guargar venta: ")
        match opcion:
            case "1":
                agregar_productos()
            case "2":
                continuar_venta = False
    total: float = 0
    for venta_detalle in venta_detalles:
        total += venta_detalle.total
    ventas.append(Venta(len(ventas) + 1, cliente, venta_detalles, total))
    return ventas

def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_texto())
    return ventas

def buscar_venta():
    numero: int = int(input("Ingrese el número de la venta para buscar: "))
    for venta in ventas:
        if venta.numero == numero:
            print("+===========================================+")
            print("|               ** BOLETA **                |")
            print("|              === CLIENTE ===               |")
            print("|   Número de documento: ", venta.cliente.numero_documento)
            print("|                                         ")
            print(venta.convertir_a_texto())
            print("|                                         ")
            print("+===========================================+")
            print("|           === DETALLE DE VENTA ===         |")
            for venta_detalle in venta.detalle:
                print(venta_detalle.convertir_a_texto())
                print("+===========================================+")
                from reportlab.pdfgen import canvas
                from reportlab.lib.pagesizes import letter
                def imprimir_pdf(nombre_archivo):
                    w, h = letter
                    c = canvas.Canvas(nombre_archivo)
                    c.setLineWidth(.2)    
                    c.setFont('Helvetica',10)
                    c.rect(100, 100,  420,650)
                    c.drawString(250, 700, "INFORMACION DE LA TIENDA:")
                    c.drawString(150, 660, "Tienda Física: LOS CREMOSITOS")
                    c.drawString(150, 640, "Dirección: Jr. Solecito charizard 356")
                    c.drawString(150, 620, "✆Teléfono: 966127345")
                    c.drawString(150, 600, "Horario: Lunes a Viernes de 9:00 AM a 6:00 PM")
                    c.drawString(100, 580, "========================================================================")
                    c.drawString(250, 560, "BOLETA ELECCTRONICA")
                    c.drawString(250, 540, "RUC DE VOLETA: B001")
                    c.drawString(100, 520, "========================================================================")
                    c.drawString(110, 500, f"NOMBRE: {venta.cliente.razon_social}")
                    c.drawString(110, 480, "DIRECCION: JULIACA - SAN ROMAN                          fecha:04/07/2023")
                    c.drawString(100, 460, "========================================================================")
                    c.drawString(110, 440, f"ID: {venta_detalle.codigo}    | PRODUCTO: {venta_detalle.descripcion} ")
                    c.drawString(110, 420, f"CANTIDAD: {venta_detalle.cantidad}  || P. UNIT: S/.{venta_detalle.precio_unitario}  || IMPORTE: S/.{round(venta_detalle.base_imponible,2)}  || IGV: {round(venta_detalle.igv,2)} ")
                    c.drawString(410, 380, f"TOTAL: S/.{venta_detalle.total} ")
                    c.save()
                    print("PDF generado correctamente.")
                nombre_archivo_pdf = "mi_archivo.pdf"

                imprimir_pdf(nombre_archivo_pdf)
            return venta
    print("No se encontró la venta con el número ingresado.")
    return None


def menu_texto():
    print("+----------------------------------------------------+")
    print("|                                                    |")
    print("| ===============TIENDA CREMOSITOS ===============   |")
    print("|================ CRUD CLIENTE ======================|")
    print("|    1: para Insertar Cliente                        |")
    print("|    2: para listar Cliente                          |")
    print("|    3: para Buscar Cliente                          |")
    print("|    4: para Editar Cliente                          |")
    print("|    5: para Eliminar Cliente                        |")
    print("|                                                    |")
    print("+----------------------------------------------------+")
    print("|================CRUD PRODUCTO=======================|")
    print("|    6: para Insertar Producto                       |")
    print("|    7: para listar Producto                         |")
    print("|    8: para Buscar Producto                         |")
    print("|    9: para Editar Producto                         |")
    print("|   10: para Eliminar Producto                       |")
    print("|                                                    |")
    print("+----------------------------------------------------+")
    print("|==================CRUD VENTA========================|")
    print("|   11: para Insertar Venta                           |")
    print("|   12: para Listar Venta                             |")
    print("|   13: para buscar Venta                             |")
    
    print("|   14: imprimir cliente                             |")
    print("|                                                    |")
    print("+----------------------------------------------------+")
    print("|   30: para terminar                                 |")
    print("+----------------------------------------------------+")


def menu():
    continuar: bool = True
    while continuar:
        menu_texto()
        opcion: str = input("Ingrese la opcion: ")
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
                insertar_producto()
            case "7":
                listar_productos()
            case "8":
                buscar_producto() 
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
            case "14":
                reporte_pdf_clientes()  
            case "30":
                continuar = False    


def main():
    cargar_datos_clientes()
    cargar_datos_productos()
    menu()
    print("Iniciando programa")
    return True

if __name__ == '__main__':
    main()
