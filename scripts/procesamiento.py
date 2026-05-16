import pandas as pd

print("=" * 50)
print("INICIO PROCESAMIENTO ETL / ELT")
print("=" * 50)

# CARGAR DATASETS PROCESADOS

ventas = pd.read_csv(
    "../data/processed/ventas_completas.csv"
)

ventas_online = pd.read_csv(
    "../data/raw/ventas_online.csv"
)

eventos_app = pd.read_csv(
    "../data/processed/eventos_app_procesado.csv"
)

print("\n[OK] Datasets cargados correctamente")

# LIMPIEZA DE DATOS

ventas = ventas.drop_duplicates()

ventas = ventas.dropna()

ventas_online = ventas_online.drop_duplicates()

ventas_online = ventas_online.dropna()

print("[OK] Limpieza de datos completada")

# ASEGURAR TOTAL_VENTA

ventas["total_venta"] = (
    ventas["cantidad"] *
    ventas["precio_unitario"]
)

print("[OK] Campo total_venta calculado")

# TOTAL VENTAS POR CLIENTE

ventas_por_cliente = ventas.groupby(
    ["id_cliente", "nombre", "apellido"]
)["total_venta"].sum().reset_index()

ventas_por_cliente = ventas_por_cliente.sort_values(
    by="total_venta",
    ascending=False
)

print("\n============= TOP CLIENTES =============")
print(ventas_por_cliente)

# CLIENTES FRECUENTES

clientes_frecuentes = ventas.groupby(
    ["id_cliente", "nombre"]
).size().reset_index(name="cantidad_compras")

clientes_frecuentes = clientes_frecuentes.sort_values(
    by="cantidad_compras",
    ascending=False
)

print("\n============= CLIENTES FRECUENTES =============")
print(clientes_frecuentes)

# PRODUCTOS MÁS VENDIDOS

productos_vendidos = ventas.groupby(
    ["id_producto", "nombre_producto"]
)["cantidad"].sum().reset_index()

productos_vendidos = productos_vendidos.sort_values(
    by="cantidad",
    ascending=False
)

print("\n============= PRODUCTOS MÁS VENDIDOS =============")
print(productos_vendidos)

# VENTAS POR CANAL

ventas_canal = ventas_online.groupby(
    "canal"
)["total"].sum().reset_index()

ventas_canal = ventas_canal.sort_values(
    by="total",
    ascending=False
)

print("\n============= VENTAS POR CANAL =============")
print(ventas_canal)

# EVENTOS APP MÁS FRECUENTES

eventos_frecuentes = eventos_app.groupby(
    "tipo"
).size().reset_index(name="cantidad")

print("\n============= EVENTOS APP =============")
print(eventos_frecuentes)

# EXPORTAR DATASETS ANALÍTICOS

ventas_por_cliente.to_csv(
    "../data/processed/ventas_por_cliente.csv",
    index=False
)

clientes_frecuentes.to_csv(
    "../data/processed/clientes_frecuentes.csv",
    index=False
)

productos_vendidos.to_csv(
    "../data/processed/productos_mas_vendidos.csv",
    index=False
)

ventas_canal.to_csv(
    "../data/processed/ventas_por_canal.csv",
    index=False
)

eventos_frecuentes.to_csv(
    "../data/processed/eventos_app_resumen.csv",
    index=False
)

print("\n[OK] Archivos analíticos generados")

# RESUMEN FINAL

print("\n============= RESUMEN GENERAL =============")

print(f"Total registros ventas: {len(ventas)}")
print(f"Total clientes únicos: {ventas['id_cliente'].nunique()}")
print(f"Total productos vendidos: {ventas['id_producto'].nunique()}")

print("\n" + "=" * 50)
print("PROCESAMIENTO ETL / ELT FINALIZADO")
print("=" * 50)