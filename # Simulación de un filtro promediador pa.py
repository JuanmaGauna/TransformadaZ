from random import uniform
import matplotlib.pyplot as plt

# Simulación de 10 lecturas de temperatura (valores fluctuantes)
sensor_readings = [round(uniform(40, 70), 2) for _ in range(10)]  # Temperaturas entre 40°C y 70°C
smoothed_readings = []

# Tamaño del filtro promediador
N = 6
buffer = []

# Aplicación del filtro promediador
for reading in sensor_readings:
    buffer.append(reading)
    if len(buffer) > N:
        buffer.pop(0)  # Mantener solo las últimas N lecturas

    # Calcular promedio del buffer
    promedio = round(sum(buffer) / len(buffer), 2)
    smoothed_readings.append(promedio)

# Mostrar resultados en consola
print(f"{'Índice':<8} {'Lectura Original (°C)':<25} {'Lectura Suavizada (°C)':<25}")
print("-" * 60)
for i, (original, smoothed) in enumerate(zip(sensor_readings, smoothed_readings)):
    print(f"{i:<8} {original:<25.2f} {smoothed:<25.2f}")

# Graficar las lecturas originales y suavizadas
plt.figure(figsize=(10, 6))
plt.plot(sensor_readings, label='Lecturas Originales', marker='o', linestyle='--', color='r')
plt.plot(smoothed_readings, label='Lecturas Suavizadas', marker='o', linestyle='-', color='b')

# Añadir detalles al gráfico
plt.title("Filtro Promediador: Lecturas Originales vs Suavizadas")
plt.xlabel("Índice de Lectura")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
