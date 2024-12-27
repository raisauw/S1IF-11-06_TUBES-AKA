import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi Rekursif
def catalan_recursive(n):
    if n <= 1:
        return 1
    
    result = 0
    for i in range(n):
        result += catalan_recursive(i) * catalan_recursive(n-1-i)
    return result

# Fungsi Iteratif
def catalan_iterative(n):
    if n <= 1:
        return 1

    catalan = [0] * (n + 1)
    catalan[0] = catalan[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-1-j]
            
    return catalan[n]

n_values = []
recursive_times = []
iterative_times = []

# Update Grafik
def update_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, recursive_times, label='Recursive', marker='o', linestyle='-', color='blue')
    plt.plot(n_values, iterative_times, label='Iterative', marker='o', linestyle='-', color='green')
    plt.title('Perbandingan Performa: Rekursif vs Iteratif (Bilangan Catalan)')
    plt.xlabel('Input (n)')
    plt.ylabel('Waktu Eksekusi (detik)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.show()

# Cetak Table
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["n", "Nilai Catalan", "Waktu Rekursif (s)", "Waktu Iteratif (s)"]
    min_len = min(len(n_values), len(recursive_times), len(iterative_times))
    
    for i in range(min_len):
        catalan_value = catalan_iterative(n_values[i])
        table.add_row([
            n_values[i],
            catalan_value,
            f"{recursive_times[i]:.6f}",
            f"{iterative_times[i]:.6f}"
        ])
    print(table)

# Main
print("Tugas Besar Mata Kuliah Analisis Kompleksitas Algoritma")
print("Anggota Kelompok:")
print("Raifanka Raisa Ramadhan (2311102205)")
print("Muhammad Amir Saleh (2311102233)")
print("=======================================================")
print("Program Perbandingan Perhitungan Bilangan Catalan")
print("=======================================================")
print("\nn adalah indeks atau urutan dari bilangan Catalan yang ingin kita hitung.")

while True:
    try:
        n = int(input("\nMasukkan nilai n (input -1 untuk keluar): "))
        
        if n == -1:
            print("\nProgram selesai. Terima kasih!")
            break
            
        if n < 0:
            print("nilai n tidak boleh negatif!")
            continue
            
        n_values.append(n)
        
        # Rekursif
        start_time = time.time()
        catalan_recursive(n)
        recursive_time = time.time() - start_time
        recursive_times.append(recursive_time)
        
        # Iteratif
        start_time = time.time()
        catalan_iterative(n)
        iterative_time = time.time() - start_time
        iterative_times.append(iterative_time)
        
        # Hasil
        print("\nHasil Perbandingan:")
        print_execution_table()
        update_graph()
            
    except ValueError:
        print("Nilai n harus berupa bilangan bulat.")
    except RecursionError:
        print("\nRekursi terlalu dalam, gunakan nilai n yang lebih kecil.")
        n_values.pop()
