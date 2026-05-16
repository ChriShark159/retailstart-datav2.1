import pandas as pd
import json
import xml.etree.ElementTree as ET

print("=" * 50)
print("INICIO PROCESO DE INGESTA DE DATOS")
print("=" * 50)

# CARGA ARCHIVOS CSV

ventas_pos = pd.read_csv("../data/raw/ventas_pos.csv")

productos_erp = pd.read_csv("../data/raw/productos_erp.csv")

clientes_crm = pd.read_csv("../data/raw/clientes_crm.csv")

ventas_online = pd.read_csv("../data/raw/ventas_online.csv")

callcenter = pd.read_csv("../data/raw/callcenter.csv")

proveedores = pd.read_csv("../data/raw/proveedores.csv")

multimedia = pd.read_csv("../data/raw/multimedia.csv")

print("\n[OK] Archivos CSV cargados correctamente")

# CARGA ARCHIVOS JSON

with open("../data/raw/eventos_app.json", "r", encoding="utf-8") as f:
    eventos_app = json.load(f)

eventos_app_df = pd.DataFrame(eventos_app)

with open("../data/raw/redes_sociales.json", "r", encoding="utf-8") as f:
    redes_sociales = json.load(f)

redes_sociales_df = pd.DataFrame(redes_sociales)

print("[OK] Archivos JSON cargados correctamente")

# CARGA ARCHIVO XML

tree = ET.parse("../data/raw/logistica.xml")
root = tree.getroot()

pedidos = []

for pedido in root.findall("pedido"):
    pedidos.append({
        "id_pedido": pedido.find("id").text,
        "id_cliente": pedido.find("cliente").text,
        "estado": pedido.find("estado").text
    })

logistica_df = pd.DataFrame(pedidos)

print("[OK] Archivo XML cargado correctamente")

# CARGA ARCHIVO TXT

with open("../data/raw/logs_sistema.txt", "r", encoding="utf-8") as f:
    logs = f.readlines()

logs_df = pd.DataFrame(logs, columns=["log"])

print("[OK] Archivo TXT cargado correctamente")


# MOSTRAR INFORMACIÓN GENERAL


print("\n================ DATASETS =================")

print(f"Ventas POS: {ventas_pos.shape}")
print(f"Productos ERP: {productos_erp.shape}")
print(f"Clientes CRM: {clientes_crm.shape}")
print(f"Ventas Online: {ventas_online.shape}")
print(f"Eventos App: {eventos_app_df.shape}")
print(f"Logística: {logistica_df.shape}")
print(f"Logs Sistema: {logs_df.shape}")
print(f"Redes Sociales: {redes_sociales_df.shape}")
print(f"Call Center: {callcenter.shape}")
print(f"Proveedores: {proveedores.shape}")
print(f"Multimedia: {multimedia.shape}")

# UNIFICACIÓN DE DATOS PRINCIPALES

ventas_completas = ventas_pos.merge(
    clientes_crm,
    on="id_cliente",
    how="left"
)

ventas_completas = ventas_completas.merge(
    productos_erp,
    on="id_producto",
    how="left"
)

# =====================================================
# CREAR CAMPO TOTAL VENTA
# =====================================================

ventas_completas["total_venta"] = (
    ventas_completas["cantidad"] *
    ventas_completas["precio_unitario"]
)

print("\n[OK] Integración de datos completada")

# =====================================================
# GUARDAR ARCHIVOS PROCESADOS
# =====================================================

ventas_completas.to_csv(
    "../data/processed/ventas_completas.csv",
    index=False
)

eventos_app_df.to_csv(
    "../data/processed/eventos_app_procesado.csv",
    index=False
)

redes_sociales_df.to_csv(
    "../data/processed/redes_sociales_procesado.csv",
    index=False
)

logistica_df.to_csv(
    "../data/processed/logistica_procesado.csv",
    index=False
)

logs_df.to_csv(
    "../data/processed/logs_procesado.csv",
    index=False
)

print("[OK] Archivos procesados guardados")

# =====================================================
# VISTA PREVIA
# =====================================================

print("\n============= VENTAS COMPLETAS =============")
print(ventas_completas.head())

print("\n============= EVENTOS APP =============")
print(eventos_app_df.head())

print("\n============= LOGISTICA =============")
print(logistica_df.head())

print("\n============= REDES SOCIALES =============")
print(redes_sociales_df.head())

print("\n============= LOGS SISTEMA =============")
print(logs_df.head())

print("\n" + "=" * 50)
print("PROCESO DE INGESTA FINALIZADO")
print("=" * 50)