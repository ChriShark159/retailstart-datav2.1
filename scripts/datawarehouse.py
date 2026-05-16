import pandas as pd

print("=" * 50)
print("GENERACIÓN DATA WAREHOUSE")
print("=" * 50)

# CARGAR DATASET PRINCIPAL

ventas = pd.read_csv(
    "../data/processed/ventas_completas.csv"
)

ventas_online = pd.read_csv(
    "../data/raw/ventas_online.csv"
)

print("[OK] Datos cargados")

# DIM_CLIENTE

dim_cliente = ventas[[
    "id_cliente",
    "nombre",
    "apellido",
    "segmento",
    "ciudad"
]].drop_duplicates()

# DIM_PRODUCTO

dim_producto = ventas[[
    "id_producto",
    "nombre_producto",
    "categoria",
    "proveedor"
]].drop_duplicates()

# DIM_TIEMPO

dim_tiempo = pd.DataFrame()

dim_tiempo["fecha"] = pd.to_datetime(
    ventas["fecha"]
)

dim_tiempo["anio"] = dim_tiempo["fecha"].dt.year
dim_tiempo["mes"] = dim_tiempo["fecha"].dt.month
dim_tiempo["dia"] = dim_tiempo["fecha"].dt.day

dim_tiempo = dim_tiempo.drop_duplicates()

# DIM_CANAL

dim_canal = pd.DataFrame({
    "id_canal": [1, 2],
    "canal": ["tienda", "online"]
})

# FACT_VENTAS

fact_ventas = ventas[[
    "id_venta",
    "id_cliente",
    "id_producto",
    "fecha",
    "cantidad",
    "total_venta"
]]

fact_ventas["canal"] = "tienda"

# EXPORTAR DIMENSIONES

dim_cliente.to_csv(
    "../data/processed/dim_cliente.csv",
    index=False
)

dim_producto.to_csv(
    "../data/processed/dim_producto.csv",
    index=False
)

dim_tiempo.to_csv(
    "../data/processed/dim_tiempo.csv",
    index=False
)

dim_canal.to_csv(
    "../data/processed/dim_canal.csv",
    index=False
)

fact_ventas.to_csv(
    "../data/processed/fact_ventas.csv",
    index=False
)

print("[OK] Data Warehouse generado")

# RESUMEN

print("\n============= RESUMEN DW =============")

print(f"Dim Cliente: {dim_cliente.shape}")
print(f"Dim Producto: {dim_producto.shape}")
print(f"Dim Tiempo: {dim_tiempo.shape}")
print(f"Dim Canal: {dim_canal.shape}")
print(f"Fact Ventas: {fact_ventas.shape}")

print("\n" + "=" * 50)
print("DATA WAREHOUSE FINALIZADO")
print("=" * 50)