
import subprocess
import os
FNULL = open(os.devnull, 'w')    #use this if you want to suppress output to stdout from the subprocess
full_path = (Metashape.app.document.path.split('/'))
i = 0
tt_path = ''
for i in range(len(full_path)) :
	if (i < (len(full_path)-1)):
		tt_path = tt_path + full_path[i] + "/"

es_curr_chunk = Metashape.app.document.chunk.label

param = " AUTO_SAVE off -o" + tt_path+es_curr_chunk+".laz SS DISTANCE 0.05 SAVE_CLOUDS " + tt_path+es_curr_chunk+"_subsampled.laz"
args = r'C:\Program Files\CloudCompare\cloudcompare.exe' + param
subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)