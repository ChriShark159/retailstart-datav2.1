import pandas as pd
import json
import xml.etree.ElementTree as ET

# CARGA ARCHIVOS CSV

ventas = pd.read_csv("../data/raw/ventas_pos.csv")
clientes = pd.read_csv("../data/raw/clientes_crm.csv")
productos = pd.read_csv("../data/raw/productos_erp.csv")
online = pd.read_csv("../data/raw/ventas_online.csv")

print("Ventas POS")
print(ventas.head())

print("\nClientes CRM")
print(clientes.head())

# CARGA JSON

with open("../data/raw/eventos_app.json", "r", encoding="utf-8") as f:
    eventos = json.load(f)

eventos_df = pd.DataFrame(eventos)

print("\nEventos App")
print(eventos_df.head())

# CARGA XML

tree = ET.parse("../data/raw/logistica.xml")
root = tree.getroot()

pedidos = []

for pedido in root.findall("pedido"):
    pedidos.append({
        "id": pedido.find("id").text,
        "cliente": pedido.find("cliente").text,
        "estado": pedido.find("estado").text
    })

logistica_df = pd.DataFrame(pedidos)

print("\nLogística")
print(logistica_df.head())

# UNIFICAR DATOS

ventas_clientes = ventas.merge(
    clientes,
    on="id_cliente",
    how="left"
)

ventas_completas = ventas_clientes.merge(
    productos,
    on="id_producto",
    how="left"
)

# GUARDAR DATASET PROCESADO

ventas_completas.to_csv(
    "../data/processed/ventas_clientes.csv",
    index=False
)

print("\nDataset unificado generado correctamente")