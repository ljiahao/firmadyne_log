import subprocess
import os


def main():
<<<<<<< HEAD
	dir_set = 
	subprocess.call('mkdir res101', shell = True)
=======
	dir_set = [10]
	#subprocess.call('mkdir res101', shell = True)
>>>>>>> f50bd965ce4dd4b3a7e60805c177b0be475853c3
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qemu.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
<<<<<<< HEAD
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log//', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log//', shell = True)
=======
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log/2th/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log/2th/', shell = True)
>>>>>>> f50bd965ce4dd4b3a7e60805c177b0be475853c3

if __name__ == '__main__':
	main()

