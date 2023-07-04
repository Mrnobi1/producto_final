from reportlab.pdfgen import canvas
from venta import Venta
from ventas_detalle import VentaDetalle
class BoletaVentaPDF:
    def __init__(self, venta):
        self.venta = venta

    def generar_boleta_venta(self):
        c = canvas.Canvas("boleta_venta.pdf")
        self.dibujar_encabezado(c)
        self.dibujar_informacion_venta(c)
        self.dibujar_detalles_venta(c)
        c.save()

    def dibujar_encabezado(self, c):
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, "BOLETA DE VENTA")

    def dibujar_informacion_venta(self, c):
        c.setFont("Helvetica", 12)
        c.drawString(100, 700, f"Número de Venta: {self.venta.numero}")
        c.drawString(100, 680, f"Fecha: {self.venta.fecha}")

    def dibujar_detalles_venta(self, c):
        detalles = self.venta.detalle
        y = 600
        c.setFont("Helvetica", 10)
        c.drawString(100, y, "Producto")
        c.drawString(250, y, "Cantidad")
        c.drawString(350, y, "Precio Unitario")
        c.drawString(450, y, "Total")
        y -= 20
        for detalle in detalles:
            c.drawString(100, y, detalle.producto)
            c.drawString(250, y, str(detalle.cantidad))
            c.drawString(350, y, str(detalle.precio_unitario))
            c.drawString(450, y, str(detalle.total))
            y -= 20

venta_detalles = [VentaDetalle(numero=1, producto="Producto 1", cantidad=2, precio_unitario=10.0, total=20.0),
    VentaDetalle(numero=2, producto="Producto 2", cantidad=3, precio_unitario=15.0, total=45.0)]

# Ejemplo de uso
venta_ejemplo = Venta(numero=1, fecha="02/07/2023", detalle=venta_detalles, total=100.0)
boleta_venta = BoletaVentaPDF(venta_ejemplo)
boleta_venta.generar_boleta_venta()





venta_ejemplo = Venta(numero=1, fecha="02/07/2023", detalle=venta_detalles, total=100.0)
