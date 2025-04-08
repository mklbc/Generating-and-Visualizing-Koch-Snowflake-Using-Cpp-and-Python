import os
import matplotlib.pyplot as plt
import numpy as np

filename = "koch_snowflake.txt"


if os.path.isfile(filename):
 
  data = np.loadtxt(filename)
  x = data[:, 0]
  y = data[:, 1]

  plt.plot(x, y, marker='o', linestyle='-', color='green')
 
else:
  print("Hata: 'koch_snowflake.txt' dosyası bulunamadı. Lütfen verileri oluşturmak için önce C++ kodunu çalıştırın.")

plt.show()
