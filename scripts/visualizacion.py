import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("ANÁLISIS Y VISUALIZACIÓN")
print("=" * 50)

# CARGAR DATASETS

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

# CREAR NOMBRE COMPLETO CLIENTES

ventas_cliente["cliente"] = (
    ventas_cliente["nombre"] + " " +
    ventas_cliente["apellido"]
)

# MOSTRAR RESULTADOS

print("\n============= CLIENTES =============")
print(ventas_cliente)

print("\n============= VENTAS POR CANAL =============")
print(ventas_canal)

print("\n============= PRODUCTOS =============")
print(productos)

# GRÁFICO CLIENTES

plt.figure(figsize=(14, 6))

barras = plt.bar(
    ventas_cliente["cliente"],
    ventas_cliente["total_venta"]
)

plt.title("Ventas Totales por Cliente")
plt.xlabel("Clientes")
plt.ylabel("Ventas Totales")

plt.xticks(rotation=25)

# Mostrar valores arriba
for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f'{altura:,.0f}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()

plt.savefig(
    "../data/processed/grafico_top_clientes.png"
)

plt.close()

# GRÁFICO VENTAS POR CANAL

plt.figure(figsize=(8, 6))

barras = plt.bar(
    ventas_canal["canal"],
    ventas_canal["total"]
)

plt.title("Ventas por Canal")
plt.xlabel("Canal")
plt.ylabel("Ventas Totales")

# Mostrar valores arriba
for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f'{altura:,.0f}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()

plt.savefig(
    "../data/processed/grafico_ventas_canal.png"
)

plt.close()

# =====================================================
# GRÁFICO PRODUCTOS MÁS VENDIDOS
# =====================================================

plt.figure(figsize=(12, 6))

barras = plt.bar(
    productos["nombre_producto"],
    productos["cantidad"]
)

plt.title("Productos Más Vendidos")
plt.xlabel("Producto")
plt.ylabel("Cantidad Vendida")

plt.xticks(rotation=20)

# Mostrar valores arriba
for barra in barras:
    altura = barra.get_height()

    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura,
        f'{altura:.0f}',
        ha='center',
        va='bottom'
    )

plt.tight_layout()

plt.savefig(
    "../data/processed/grafico_productos.png"
)

plt.close()

print("\n[OK] Gráficos generados correctamente")

print("\n" + "=" * 50)
print("VISUALIZACIÓN FINALIZADA")
print("=" * 50)