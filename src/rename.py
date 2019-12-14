import Metashape
import os

tt_path = "T:/Topografia - Arquivo/Crea_Sede Salgueiro/Recursos/Processados/24-07-2019/"

os.chdir(tt_path)

i = 1

for file in os.listdir():
	if file.count("Nuvem_Interpolada") >= 1:
		src = file
		dst = "Nuvem_Interpolada_" + str(i) + ".las"
		os.rename(src,dst)
		i = i + 1 
for file in os.listdir():
	if (file.count("Chunk ") >= 1) and (file.count("SUBSAMPLED") >= 1) and (file.count(".las") >= 1)  :
		src=file
		dst="Nuvem_Interpolada.las"
		os.rename(src,dst)
