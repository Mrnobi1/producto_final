from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class PDFGenerator:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def generar_reporte_clientes(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter)
        table_data = []
        table_data.append(["Número de Documento", "Razón Social", "Dirección", "Teléfono"])
        for cliente in self.data:
            table_data.append([
                cliente["numero_documento"],
                cliente["razon_social"],
                cliente["direccion"],
                cliente["telefono"]
            ])

        table = Table(table_data)
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        table.setStyle(style)
        elements = [table]
        doc.build(elements)

data_clientes = [
    {"numero_documento": "72457858", "razon_social": "jack denys", "direccion": "Jr tupac", "telefono": "984562145"},
    {"numero_documento": "64545245", "razon_social": "jazel", "direccion": "Jr ares", "telefono": "931313131"},
    {"numero_documento": "1234578", "razon_social": "Elias", "direccion": "Jr and", "telefono": "934547898"}
]

pdf = PDFGenerator("reporte_clientes.pdf", data_clientes)
pdf.generar_reporte_clientes()
