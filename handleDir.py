import subprocess
import os


def main():
	dir_set = [173, 94, 164, 7, 3, 189, 21, 10, 77, 99, 167, 45, 59, 22, 182]
	#subprocess.call('mkdir res101', shell = True
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qemu.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log/9th/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log/9th/', shell = True)


if __name__ == '__main__':
	main()

