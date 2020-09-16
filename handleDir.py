import subprocess
import os


def main():
	dir_set = [63, 46, 31, 10, 64, 74, 78, 32]
	subprocess.call('mkdir res101', shell = True)
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qeum.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./res101/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./res101/', shell = True)

if __name__ == '__main__':
	main()

