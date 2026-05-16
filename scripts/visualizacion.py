import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("ANÁLISIS Y VISUALIZACIÓN")
print("=" * 50)

# CARGAR DATASETS ANALÍTICOS

ventas_cliente = pd.read_csv(
    "../data/processed/ventas_por_cliente.csv"
)

ventas_canal = pd.read_csv(
    "../data/processed/ventas_por_canal.csv"
)

productos = pd.read_csv(
    "../data/processed/productos_mas_vendidos.csv"
)

print("[OK] Datos cargados")

# MEJORES CLIENTES

top5_clientes = ventas_cliente.head(5)

print("\n============= TOP CLIENTES =============")
print(top5_clientes)

# CANAL MÁS VENDIDO

print("\n============= VENTAS POR CANAL =============")
print(ventas_canal)

# PRODUCTOS MÁS VENDIDOS

top_productos = productos.head(5)

print("\n============= PRODUCTOS MÁS VENDIDOS =============")
print(top_productos)

# GRÁFICO TOP CLIENTES

plt.figure(figsize=(10, 5))

plt.bar(
    top5_clientes["nombre"],
    top5_clientes["total_venta"]
)

plt.title("Top 5 Clientes")
plt.xlabel("Clientes")
plt.ylabel("Ventas Totales")

plt.tight_layout()

plt.savefig("../data/processed/grafico_top_clientes.png")

plt.close()

# GRÁFICO VENTAS POR CANAL

plt.figure(figsize=(6, 5))

plt.bar(
    ventas_canal["canal"],
    ventas_canal["total"]
)

plt.title("Ventas por Canal")
plt.xlabel("Canal")
plt.ylabel("Ventas")

plt.tight_layout()

plt.savefig("../data/processed/grafico_ventas_canal.png")

plt.close()

# GRÁFICO PRODUCTOS MÁS VENDIDOS

plt.figure(figsize=(10, 5))

plt.bar(
    top_productos["nombre_producto"],
    top_productos["cantidad"]
)

plt.title("Productos Más Vendidos")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("../data/processed/grafico_productos.png")

plt.close()

print("\n[OK] Gráficos generados correctamente")

print("\n" + "=" * 50)
print("VISUALIZACIÓN FINALIZADA")
print("=" * 50)