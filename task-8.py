import subprocess as sp
import webbrowser as web
#import pyttsx3
import os
from time import sleep as slp
from os import system 

def cls():
	ab = sp.getoutput('clear')
	print(ab)

def clr(i):
	c = i
	a = sp.getoutput('tput setaf {}'. format(c))
	print(a)
	return a

'''
def #speak(i):
	x = #sp.getoutput("espeak-ng -ven-us+m1 -s155 '{}'". format(i))
	print(x)
	print(i)
	return i
'''
def cmdrun(i):
	c = i
	cmd = sp.getoutput(c)
	print(cmd)
	return cmd

def opt():

	print('   Launching Option mode...')
	#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Lauching Option mode'")
	slp(1)
	print('   Option mode lauched successfully...')
	slp(1)
	print('   Please enter serial no. with tag...')
	##sp.getoutput("espeak-ng -ven-us+m1 -s150 'Please enter serial number with tag'")
	while True :
		menu()
		no = input('Enter your choice : ')
		if ('51'in no) and ('other'in no or 'Other'in no):
			print('51. Exit from this program')
			print('   Please wait....')
			print('   OK...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			slp(0.5)
			print('   Bye...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'bye'")
			clr(7)
			cls()
			break
			slp(1)


		if ('50'in no) and ('other'in no or 'Other'in no):
			print('50*. Launch Manual Mode')
			print('   Please wait....')
			slp(1)
			man()		
	

		elif ('49'in no) and ('other'in no or 'Other'in no):
			print('49*.Launch Command Mode (CMD Mode) ')
			print('   Please wait....')
			slp(1)
			print('   Launching cmd mode...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'launching CMD mode'")
			print('   CMD mode has been launched', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'CMD mode has been launched'")
			print('[ Root@localhost ]@ ', end='')
			cmdmode = input()
			cmdrun(cmdmode)
			while True :
				print('[ Root@localhost ]@ ' , end='')
				cmdmode = input()
				if 'exit' in cmdmode or 'close' in cmdmode :
					print('   Ok', end='')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
					print('   Turning off CMD mode...', end='')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'turning off CMD mode'")
					print('   Turned off CMD mode', end='')
					break
				else:
					cmdrun(cmdmode)
			slp(3)

		elif ('48'in no) and ('other'in no or 'Other'in no):
			print('48. Show all running processes status')
			print('   Please wait....')
			slp(1)
			cmdrun('ps -aux')
			slp(3)
		elif ('47'in no) and ('other'in no or 'Other'in no):
			print('47. Check CPU time')
			print('   Please wait....')
			slp(1)
			prog = input('Enter program command to run : ')
			cmdrun('time {}'. format(prog))
			slp(3)
		elif ('46'in no) and ('other'in no or 'Other'in no):
			print('46. Launch another terminal')
			print('   Please wait....')
			slp(1)
			cmdrun('gnome-terminal')
			slp(3)
		elif ('45'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('45. Delete any file on hadoop')
			print('   Please wait....')
			slp(1)
			filename1 = input('Enter your file name : ')
			cmdrun('hadoop fs -rm /{}'. format(filename1))
			slp(3)
		elif ('44'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('44. Show all uploaded file on hadoop ')
			print('   Please wait....')
			slp(1)
			cmdrun('hadoop fs -ls /')
			slp(3)

		elif ('43'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('43. Upload empty file on hadoop cluster')
			print('   Please wait....')
			slp(1)
			filename2 = input('Enter file name : ')
			cmdrun('hadoop fs -touchz /{}'. format(filename2))
			slp(3)
		elif ('42'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('42. Upload file on hadoop cluster')
			print('   Please wait....')
			slp(1)
			filename = input('Enter your file name or file path : ')
			cmdrun('hadoop fs -put {}'. format(filename))
			slp(3)
		elif ('41'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('41. Check namenode/datanode status')
			print('   Please wait....')
			slp(1)
			cmdrun('jps')
			slp(3)
		elif ('40'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('40. Start hadoop datanode')
			print('   Please wait....')
			slp(1)
			cmdrun('hadoop-daemon.sh start datanode')
			slp(3)
		elif ('39'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('39. Start hadoop namenode')
			print('   Please wait....')
			slp(1)
			cmdrun('hadoop-daemon.sh start namenode')
			slp(3)
		elif ('38'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('38. Show hadoop report in short')
			print('   Please wait....')
			slp(1)
			print("   Press 'q' for quit")
			cmdrun('hadoop dfsadmin -report | less')
			slp(3)
		elif ('37'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('37. Show hadoop report')
			print('   Please wait....')
			slp(1)
			print("Press 'q' for quit")
			cmdrun('hadoop dfsadmin -report')
			slp(3)
		elif ('36'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('36. Format hadoop namenode')
			print('   Please wait....')
			slp(1)
			cmdrun('hadoop namenode -format')
			print('   Namonode has been formatted...')
			#slp(3)
			
		elif ('35'in no) and ('hadoop'in no or 'Hadoop'in no):
			print('35. Configure hadoop')
			print('   Please wait....')
			slp(1)
			typ = input('You want to configure for namenode(n) or datanode(d)? (n/d) : ')
			if 'n' in typ or 'N' in typ :
				print('   You have to create another directory for namenode...')
				#sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
				dire = input('Enter name for namenode directory : ')
				cmdrun('mkdir {}'. format(dire))
				
				datafile = open('hadop.xml', 'w')
				datafile.write(f'''
				<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
				<!-- Put site-specific property overrides in this file. -->
				
				<configuration>
					
				<property>
				<name>dfs.name.dir</name>
				<value>/n1</value>
				</property>
				
				</configuration>
				
				''')
				
				
				datafile1 = open('hadop.xml', 'w')
				datafile1.write(f'''
				<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
				<!-- Put site-specific property overrides in this file. -->
				
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://192.168.0.129:9001</value>
				</property>
				</configuration>
				''')

				print('   Your hadoop namenode has been successfully configured...')		
				#sp.getoutput("espeak-ng -ven-us+m1 -s155 'Your hadoop namenode has been successfully configured'")
			elif 'd'in typ or 'D'in typ:
				print('   You have to create another directory for datanode...')
				#sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
				dire = input('Enter name for datanode directory : ')
				cmdrun('mkdir {}'. format(dire))
				
				datafile = open('hadop.xml', 'w')
				datafile.write(f'''
				<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
				<!-- Put site-specific property overrides in this file. -->
				
				<configuration>
					
				<property>
				<name>dfs.data.dir</name>
				<value>/d1</value>
				</property>
				
				</configuration>
				
				''')
				
				
				datafile1 = open('hadop.xml', 'w')
				datafile1.write(f'''
				<?xml version="1.0"?>
				<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
				
				<!-- Put site-specific property overrides in this file. -->
				
				<configuration>
				<property>
				<name>fs.default.name</name>
				<value>hdfs://192.168.0.129:9001</value>
				</property>
				</configuration>
				''')

				print('   Your hadoop datanode has been successfully configured...')		
				#sp.getoutput("espeak-ng -ven-us+m1 -s155 'Your hadoop datanode has been successfully configured'")		
			slp(3)

		elif ('34'in no) and ('docker'in no or 'Docker'in no):
			print('34. Delete all containers')
			print('   Please wait....')
			slp(1)
			cmdrun('docker container rm $(docker ps -aq)')
			slp(3)
		elif ('33'in no) and ('docker'in no or 'Docker'in no):
			print('33. Stop already running container')
			print('   Please wait....')
			slp(1)
			cmdrun('docker ps')
			runos = input('Enter nick name of currently running container : ')
			slp(3)
		elif ('32'in no) and ('docker'in no or 'Docker'in no):
			print('32. Start already launched container')
			print('   Please wait....')
			slp(1)
			cmdrun('docker ps')
			runos = input('Enter nick name of currently running container : ')
			cmdrun('docker start {}'. format(runos))
			slp(3)

		elif ('31'in no) and ('docker'in no or 'Docker'in no):
			print('31. Show all launched containers')
			print('   Please wait....')
			slp(1)
			cmdrun('docker ps -a')
			slp(3)
		elif ('30'in no) and ('docker'in no or 'Docker'in no):
			print('30. Launch already running container')
			print('   Please wait....')
			slp(1)
			cmdrun('docker ps')
			runos = input('Enter nick name of currently running container : ')
			slp(3)
		elif ('29'in no) and ('docker'in no or 'Docker'in no):
			print('29. Launch new container in background')
			print('   Please wait....')
			slp(1)
			os = input('Enter name of your OS or container : ')
			osname = input('Enter nick name for your OS or container')
			if osname == "" :
				print('   You not gave any nick name for your os...')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You have not give any nick name for your os'")
				cmdrun('docker run -dit {}'. format(os))
				print('   Your container has been launched in background...')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Your container has been launched in background'")
			
			else:
				print('   You gave nick name for your os =  {} '. format(osname))
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You gave nick name for your os =  {}'". format(osname))
				cmdrun('docker run -dit --name {} {}'. format(osname,os))
				print('   Your container has been launched in background...')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Your container has been launched in background'")
			slp(3)
		elif ('28'in no) and ('docker'in no or 'Docker'in no):
			print('28. Launch new container')
			print('   Please wait....')
			slp(1)
			os = input('Enter name of image : ')
			osname = input('Enter the name for your container')
			tab = input('You want to run container in current terminal(c) or new terminal(n)? (c/n) : ')
			if osname == "" :
				if ('c' in tab) and ('n'not in tab):
					print('   You not gave any name for your container...')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You have not give any nick name for your os'")
					cmdrun('docker run -it {}'. format(os))
				else:
					print('   You not gave any name for your container...')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You have not give any nick name for your os'")
					cmdrun('gnome-terminal -- docker run -it {}'. format(os))
			else:
				if ('c'in tab) and ('n'not in tab):
					print('   You gave name for your container =  {} '. format(osname))
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You gave nick name for your os =  {}'". format(osname))
					cmdrun('docker run -it --name {} {}'. format(osname,os))
				else:
					print('   You gave name for your container =  {} '. format(osname))
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You gave nick name for your os =  {}'". format(osname))
					cmdrun('gnome-terminal -- docker run -it --name {} {}'. format(osname,os))
			slp(3)
		elif ('27'in no) and ('docker'in no or 'Docker'in no):
			print('27. Show currently running container')
			print('   Please wait....')
			slp(1)
			cmdrun('docker ps')
			slp(3)
		elif ('26'in no) and ('docker'in no or 'Docker'in no):
			print('26. Show all docker images')
			print('   Please wait....')
			slp(1)
			cmdrun('docker images')
			slp(3)
		elif ('25'in no) and ('docker'in no or 'Docker'in no):
			print('25. Stop docker	')
			print('   Please wait....')
			slp(1)
			print('   turning off docker...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'turning off docker'")
			cmdrun('systemctl stop docker')
			print('   Now, docker has been stopped')
			slp(3)
		elif ('24'in no) and ('docker'in no or 'Docker'in no):
			print('24. Start docker')
			print('   Please wait....')
			slp(1)
			print('   turning on docker...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'turning on docker'")
			cmdrun('systemctl start docker')
			print('   Now, docker has been started')
			slp(3)

		elif ('23'in no) and ('docker'in no or 'Docker'in no):
			print('23. Show docker status')
			print('   Please wait....')
			slp(1)
			print('   Checking docker status...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'checking docker status'")
			cmdrun('systemctl status docker')
			slp(4)
		elif ('22'in no) and ('apache'in no or 'Apache'in no or 'httpd'in no or 'Httpd'in no):
			print('22. Stop httpd')
			print('   Please wait....')
			slp(1)
			print('   Stoping apache webserver...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'stoping apcahe webserver'")
			b = sp.getoutput('systemctl stop httpd')
			b = sp.getoutput('setenforce 1')
			print('   Now, apache webserver has been stopped')
			slp(3)
		elif ('21'in no) and ('apache'in no or 'Apache'in no or 'httpd'in no or 'Httpd'in no):
			print('21. Start httpd')
			print('   Please wait....')
			slp(1)
			print('   Starting apache webserver...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'starting apcahe webserver'")
			b = sp.getoutput('systemctl start httpd')
			b = sp.getoutput('setenforce 0')
			print('   Now, apache webserver has been started')
			slp(3)
		elif ('20'in no) and ('apache'in no or 'Apache'in no or 'httpd'in no or 'Httpd'in no):
			print('20. Show httpd status')
			print('   Please wait....')
			slp(1)
			print('   Checking apache webserver status...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'checking apache webserver status'")
			b = sp.getoutput('systemctl status httpd')
			slp(3)

		elif ('19'in no) and ('firewall'in no or 'Firewall'in no):
			print('19. Stop firewall')
			print('   Please wait....')
			slp(1)
			print('   truning off firewall...')
			slp(1)
			print('   Now, firewall has been turned off')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'now, firewall has been turned off'")
			slp(3)
		elif ('18'in no) and ('firewall'in no or 'Firewall'in no):
			print('18. Start firewall')
			print('   Please wait....')
			slp(1)
			print('   truning on firewall...')
			slp(1)
			print('   Now, firewall has been turned on')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'now, firewall has been turned on'")
			slp(3)
		elif ('17'in no) and ('firewall'in no or 'Firewall'in no):
			print('17. Show firewall status')
			print('   Please wait....')
			slp(1)
			print('   Checking firewall status...')
			slp(1)
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'checking firewall status'")
			cmdrun('systemctl status firewall.service')
			slp(3)


		elif ('16'in no) and ('ip'in no or 'IP'in no):
			print('16. Mount partition')
			print('   Please wait....')
			slp(1)
			o1 = input('You have seprate directory for this new patition? (y/n) : ')
			if 'y' in o1:
				print('   then, ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'then, ok'")
				d = input('Enter that directory name : ')
				p = input('Enter the name of new partition : ')
				cmdrun('mount {} {}'. format(p,d))
			else:
				print('   ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
				print('   Then I am creating new directory for you...')
				d = input('Enter name for this new directory : ')
				p = input('Enter the name of new partition : ')
				cmdrun('mount {} {}'. format(p,d))
			slp(3)



		elif ('15'in no) and ('ip'in no or 'IP'in no):
			print('15. Format partition')
			print('   Please wait....')
			slp(1)
			part = input('Enter partition name : ')
			cmdrun('mkfs.ext4 {}'. format(part))
			o = input('Want to mount partition? (y/n) : ')
			if 'y'in o:
				print('👍   ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
				o1 = input('You have seprate directory for this new patition? (y/n) : ')
				if 'y' in o1:
					print('   then, ok')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'then, ok'")
					d = input('Enter that directory name : ')
					p = input('Enter the name of new partition : ')
					cmdrun('mount {} {}'. format(p,d))
				else:
					print('   ok')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
					print('   Then I am creating new directory for you...')
					d = input('Enter name for this new directory : ')
					p = input('Enter the name of new partition : ')
					cmdrun('mount {} {}'. format(p,d))
			else:
				print('   ok')
				break
			slp(3)



		elif ('14'in no) and ('ip'in no or 'IP'in no):
			print('14. Partition of HD')
			print('   Please wait....')
			slp(1)
			print('''
			These command will help in partition:
			p = show details about HD
			n = create new partition
				p = primary partition
				e = extended partition
			d = delete partition
			w = save 
			q = quit		
				''')
			print('   Press enter for continue...', end='')
			ab = input()
			cmdrun('fdisk /dev/sda')
			o = input('Want to format partition? (y/n) : ')
			if ('y'in o):
				print('   ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
				part = input('Enter partition name : ')
				cmdrun('mkfs.ext4 {}'. format(part))
				o = input('Want to mount partition? (y/n) : ')
				if 'y'in o:
					print('   ok')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
					o1 = input('You have seprate directory for this new patition? (y/n) : ')
					if 'y' in o1:
						print('   then, ok')
						#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'then, ok'")
						d = input('Enter that directory name : ')
						p = input('Enter the name of new partition : ')
						cmdrun('mount {} {}'. format(p,d))
					else:
						print('   ok')
						#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
						print('   Then I am creating new directory for you...')
						d = input('Enter name for this new directory : ')
						p = input('Enter the name of new partition : ')
						cmdrun('mount {} {}'. format(p,d))
			else:
				print('   ok')
				break
			slp(3)



		elif ('13'in no) and ('ram'in no or 'RAM'in no):
			print('13. Show all partition(already created)')
			print('   Please wait....')
			slp(1)
			cmdrun('fdisk -l')
			slp(3)
		elif ('12'in no) and ('ram'in no or 'RAM'in no):
			print('12. Show RAM status')
			print('   Please wait....')
			slp(1)
			cmdrun('free -m')
			slp(3)

		elif ('11'in no) and ('ip'in no or 'IP'in no):
			print('11. Check tcp command')
			print('   Please wait....')
			slp(1)
			cmdrun('tcpdump -i enp0s3 -n')
			slp(3)
		elif ('10'in no) and ('ip'in no or 'IP'in no):
			print('10. Change IP')
			print('   Please wait....')
			slp(1)
			ip = input('Enter new ip : ')
			cmdrun('ifconfig enp0s3 {}'. format(ip))
			slp(3)
		elif ('9'in no) and ('ip'in no or 'IP'in no):
			print('9. Show main IP')
			print('   Please wait....')
			slp(1)
			cmdrun('ifconfig enp0s3')
			slp(3)
		elif ('8'in no)and ('ip'in no or 'IP'in no):
			print('8. Show all IP')
			print('   Please wait....')
			slp(1)
			cmdrun('ifconfig')
			slp(3)
		elif ('7'in no) and ('file'in no or 'File'in no):
			print('7. Open file of current directory')
			print('   Please wait....')
			slp(1)
			#x = sp.getoutput("espeak-ng -ven-us+m1 -s155 'please enter your file name..'")
			print('please enter your file name :  ' , end='')	
			fname = input()	
			b = sp.getoutput('vim {}'. format(fname))
			slp(3)
		elif ('6'in no) and ('file'in no or 'File'in no):
			print('6. Create directory')
			print('   Please wait....')
			slp(1)
			folder = input('Enter folder or directory name : ')
			cmdrun('mkdir {}'. format(folder))
			slp(3)
		elif ('5'in no) and ('file'in no or 'File'in no):
			print('5. Create empty file')
			print('   Please wait....')
			slp(1)
			#x = sp.getoutput("espeak-ng -ven-us+m1 -s155 'please enter file name '")
			print('please enter file name :  ' , end='')
			filename = input()
			cmdrun('touch {}' . format(filename))
			print('   your file has been successfully created...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'your file has been successfully created...'")
			slp(3)
		elif ('4'in no) and ('file'in no or 'File'in no):
			print('4. Show files in another directory')
			print('   Please wait....')
			slp(1)
			print('Enter directory name : ', end='')
			dtry = input()
			b = sp.getoutput('ls {}'. format(dtry))
			slp(3)
		elif ('3'in no) and ('file'in no or 'File'in no):
			print('3. Show all files in current directory')
			print('   Please wait....')
			slp(1)
			cmdrun('ls')
			slp(3)
		elif ('2'in no)  and ('program'in no or 'Program'in no):
			print('2. Show date and time')
			print('   Please wait....')
			slp(1)
			cmdrun('date')
			slp(3)
		elif ('1'in no) and ('program'in no or 'Program'in no):
			print('1. Open source code')
			print('   Please wait....')
			slp(1)
			cmdrun('gedit task-8.py')



def man():

	print('   Launching Manual mode...')
	#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Lauching Manual mode'")
	slp(1)
	print('   Manual mode launched successfully...')
	#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Manual mode launched successfully'")
	cls()

	while True:
		print()
		print('   What do you want :  ', end='')
		#c = sp.getoutput("espeak-ng -ven-us+m1 -s155 'What do you want'")
		x = input()

		if ('exit' in x):
			print('   OK...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			slp(0.5)
			print('   Bye...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'bye'")
			clr(7)
			break

	# Program:-
	
		elif ('open' in x and 'source code' in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			print('....')
			cmdrun('gedit menu.py')
		elif ('date' in x) or ('show' in x and 'date' in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('date')
		elif ('time' in x) or ('show' in x and 'time' in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			print('\t', end='')
			cmdrun('date +%T')
		
	# File and Directory
		elif ('show' in x and 'file' in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('ls')

		elif ('show' in x and 'file' in x) and ('directory' in x or 'folder' in x):
			print('Enter directory name : ', end='')
			dtry = input()
			b = sp.getoutput('ls {}'. format(dtry))

		elif (('create' in x and 'file' in x) or ('create' in x and 'file' in x and 'empty' in x)):
			print('   Sure')
			#b = sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")		
			#x = sp.getoutput("espeak-ng -ven-us+m1 -s155 'please enter file name '")
			print('please enter file name :  ' , end='')
			filename = input()
			cmdrun('touch {}' . format(filename))
			print('   your file has been successfully created...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'your file has been successfully created...'")
		elif ('create'in x and ('directory'in x or 'folder')):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			folder = input('Enter folder or directory name : ')
			cmdrun('mkdir {}'. format(folder))
		elif ('open' in x and 'file' in x):
			print('   Why not...')
			#b = sp.getoutput("espeak-ng -ven-us+m1 -s155 'why not'")	
			#x = sp.getoutput("espeak-ng -ven-us+m1 -s155 'please enter your file name..'")
			print('please enter your file name :  ' , end='')	
			fname = input()	
			if ('vi' in x):
				b = sp.getoutput('vi {}'. format(fname))
			elif ('vim'in x):
				b = sp.getoutput('vim {}'. format(fname))
			elif ('gedit'in x):
				b = sp.getoutput('gedit {}'. format(fname))
			else:
				b = sp.getoutput('gedit {}'. format(fname))	
			

	# IP
		elif ('show' in x and 'ip'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")		
			cmdrun('ifconfig')
		elif ('show' in x and 'main' in x and ('ip' in x or 'network card' in x)):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('ifconfig enp0s3')
		elif ('change'in x and ('ip'in x or ('main'in x and 'ip'in x))):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			ip = int(input('Enter new ip : '))
			cmdrun('ifconfig enp0s3 {}'. format(ip))

		elif ('check'in x) and ('tcp'in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			cmdrun('tcpdump -i enp0s3 -n')

	# RAM
		elif ('show' in x or 'check'in x) and ('ram'in x or 'memory'in x) and ('status' in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			cmdrun('free -m')
		elif ('clear'in x or 'clean'in x or 'kill'in x or 'delete'in x or 'free'in x) and ('cache'in x or ('cache'in x and 'memory'in x)):
			print('   Why not...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'why not'")	
			cmdrun('echo 3 > /proc/sys/vm/drop_caches')

	# Partition
		elif ('show'in x and 'directory'in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			cmdrun('df -h')
		elif ('show' in x) and ('partition'in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			cmdrun('fdisk -l')
		
		elif ('patiotion'in x) and (('hard'in x and 'disk'in x) or 'hd'in x or 'HD'in x or 'storage'in x or 'drive'in x):
			print('   Why not...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'why not'")	
			print('''
			These command will help in partition:
			p = show details about HD
			n = create new partition
				p = primary partition
				e = extended partition
			d = delete partition
			w = save 
			q = quit		
				''')
			print('Press enter for continue...', end='')
			ab = input()
			cmdrun('fdisk /dev/sda')
			o = input('Want to format partition? (y/n) : ')
			if ('y'in o):
				print('   ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
				part = input('Enter partition name : ')
				cmdrun('mkfs.ext4 {}'. format(part))
				o = input('Want to mount partition? (y/n) : ')
				if 'y'in o:
					print('   ok')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
					o1 = input('You have seprate directory for this new patition? (y/n) : ')
					if 'y' in o1:
						print('   then, ok')
						#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'then, ok'")
						d = input('Enter that directory name : ')
						p = input('Enter the name of new partition : ')
						cmdrun('mount {} {}'. format(p,d))
					else:
						print('   ok')
						#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
						print('   Then I am creating new directory for you...')
						d = input('Enter name for this new directory : ')
						p = input('Enter the name of new partition : ')
						cmdrun('mount {} {}'. format(p,d))
			else:
				print('   ok')
				break
		
		elif ('format'in x and 'partition'in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			part = input('Enter partition name : ')
			cmdrun('mkfs.ext4 {}'. format(part))
			o = input('Want to mount partition? (y/n) : ')
			if 'y'in o:
				print('   ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
				o1 = input('You have seprate directory for this new patition? (y/n) : ')
				if 'y' in o1:
					print('   then, ok')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'then, ok'")
					d = input('Enter that directory name : ')
					p = input('Enter the name of new partition : ')
					cmdrun('mount {} {}'. format(p,d))
				else:
					print('   ok')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
					print('   Then I am creating new directory for you...')
					d = input('Enter name for this new directory : ')
					p = input('Enter the name of new partition : ')
					cmdrun('mount {} {}'. format(p,d))
			else:
				print('   ok')
				break
		
		elif ('mount'in x and 'partition'):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			o1 = input('You have seprate directory for this new patition? (y/n) : ')
			if 'y' in o1:
				print('   then, ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'then, ok'")
				d = input('Enter that directory name : ')
				p = input('Enter the name of new partition : ')
				cmdrun('mount {} {}'. format(p,d))
			else:
				print('   ok')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
				print('   Then I am creating new directory for you...')
				d = input('Enter name for this new directory : ')
				p = input('Enter the name of new partition : ')
				cmdrun('mount {} {}'. format(p,d))
			
		


	# Firewall
		elif (('stop' in x) or ('kill' in x) or ('disable' in x) or ('turn off' in x)) and ('firewall' in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")	
			print('turning off firewall...')
			cmdrun('systemctl stop firewalld.service')
			print('Now, firewall has been turned off')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Now, firewall has been turned off'")	
		elif ('show' in x) and ('status' in x) and ('firewall' in x):
			print('Checking firewall status...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'checking firewall status'")
			cmdrun('systemctl status firewall.service')
		elif (('start' in x) or ('run' in x) or ('enable' in x)) and ('firewall' in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			print('truning on firewall...')
			print('Now, firewall has been turned on')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'now, firewall has been turned on'")	

	# Apache Httpd
		elif (('start'in x) or ('enable'in x) or ('run'in x)) and (('httpd'in x) or ('apache'in x) or ('webserver'in x)):
			print('   ok')
			print('Starting apache webserver...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'starting apcahe webserver'")
			b = sp.getoutput('systemctl start httpd')
			b = sp.getoutput('setenforce 0')
			print('Now, apache webserver has been started')
			
		elif (('stop' in x) or ('kill' in x) or ('disable' in x) or ('turn off' in x)) and ('apache' in x or 'webserver'in x or 'httpd'in x):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")	
			print('turning off httpd webserver...')
			cmdrun('systemctl stop httpd')
			print('Now, Httpd webserver has been turned off')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Now, HTTPD webserver has been turned off'")
			
		elif ('show' in x) and ('status' in x) and (('apache' in x) or ('webserver'in x) or ('httpd'in x)):
			print('Checking apache webserver status...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'checking apache webserver status'")
			b = sp.getoutput('systemctl status httpd')

	# Docker
		
		elif ('show' in x) and ('status' in x) and ('docker' in x):
			print('Checking docker status...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'checking docker status'")
			b = sp.getoutput('systemctl status docker')

		elif ('start' in x or 'run' in x or 'enable' in x ) and ('docker' in x):
			print('   ok')
			print('turning on docker...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'turning on docker'")
			cmdrun('systemctl start docker')
			print('Now, docker has been started')
		elif ('stop'in x or 'disable' in x or 'kill' in x) and ('docker' in x):
			print('   ok')
			print('turning off docker...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'turning off docker'")
			cmdrun('systemctl stop docker')
			print('Now, docker has been started')
		elif ('status' in x) and ('show' in x) and ('docker' in x or ('docker' in x and 'container')):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('docker ps')
		elif ('show'in x or 'check'in x) and ('docker'in x or 'container'in x or ('docker'in x and 'container'in x)):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('docker images')
		elif ('show'in x or 'check'in x) and ('running'in x) and ('container'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('docker ps')
		elif ('start'in x or 'launch'in x or 'run'in x) and ('docker'in x) and ('container'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			os = input('Enter name of your OS or container : ')
			osname = input('Enter nick name for your OS or container')
			tab = input('You want to run container in current terminal(c) or new terminal(n)? (c/n) : ')
			if osname == "" :
				if ('c' in tab) and ('n'not in tab):
					print('   You not gave any nick name for your os...')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You have not give any nick name for your os'")
					cmdrun('docker run -it {}'. format(os))
				else:
					print('   You not gave any nick name for your os...')
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You have not give any nick name for your os'")
					cmdrun('gnome-terminal -- docker run -it {}'. format(os))
			else:
				if ('c'in tab) and ('n'not in tab):
					print('   You gave nick name for your os =  {} '. format(osname))
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You gave nick name for your os =  {}'". format(osname))
					cmdrun('docker run -it --name {} {}'. format(osname,os))
				else:
					print('   You gave nick name for your os =  {} '. format(osname))
					#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You gave nick name for your os =  {}'". format(osname))
					cmdrun('gnome-terminal -- docker run -it --name {} {}'. format(osname,os))
		
		elif ('start'in x or 'launch'in x or 'run'in x) and ('docker'in x) and ('container'in x) and ('background'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			os = input('Enter name of your OS or container : ')
			osname = input('Enter nick name for your OS or container')
			if osname == "" :
				print('   You not gave any nick name for your os...')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You have not give any nick name for your os'")
				cmdrun('docker run -dit {}'. format(os))
				print('   Your container has been launched in background...')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Your container has been launched in background'")
		
			else:
				print('   You gave nick name for your os =  {} '. format(osname))
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'You gave nick name for your os =  {}'". format(osname))
				cmdrun('docker run -dit --name {} {}'. format(osname,os))
				print('   Your container has been launched in background...')
				#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Your container has been launched in background'")
					
		elif ('open'in x or 'attach'in x) and ('already'in x or 'current'in x) and ('container'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('docker ps')
			runos = input('Enter nick name of currently running container : ')
			cmdrun('docker attach {}'. format(runos))
		elif ('start'in x or 'run'in x) and ('already'in x or 'current'in x) and ('container'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('docker ps')
			runos = input('Enter nick name of currently running container : ')
			cmdrun('docker start {}'. format(runos))
		elif ('stop'in x or 'close'in x) and ('already'in x or 'current'in x) and ('container'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('docker ps')
			runos = input('Enter nick name of currently running container : ')
			cmdrun('docker stop {}'. format(runos))



	# Hadoop
		elif ('hadoop' in x) and ('configure' in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			print('This command will coming soon....')
		elif ('format'in x) and ('hadoop'in x or ('namenode'in x)):
			print('   Why not...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'why not'")	
			cmdrun('hadoop namenode -format')	
		elif ('show'in x) and ('hadoop'in x) and ('report'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			print("Press 'q' for quit")
			cmdrun('hadoop dfsadmin -report')
		elif ('show'in x) and ('hadoop'in x) and ('report'in x) and ('short'in x or 'less'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			print("Press 'q' for quit")
			cmdrun('hadoop dfsadmin -report | less')
		elif ('start'in x) and ('hadoop'in x) and ('namenode'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('hadoop-daemon.sh start namenode')
		elif ('start'in x) and ('hadoop'in x) and ('datanode'in x):
			print('   Sure')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Sure'")
			cmdrun('hadoop-daemon.sh start datanode')
		elif (('check'in x) and ('hadoop'in x) or ('status' in x)) or (('check'in x) and ('node'in x) or ('status'in x)):
			print('   ok')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			cmdrun('jps')
		elif ('upload'in x or 'put'in x or 'send'in x) and ('file'in x or 'data'in x or 'image'in x or 'program'in x) and ('hadoop'in x or 'cluster'in x):
			print('   Sure...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'sure'")
			filename = input('Enter your file name or file path : ')
			cmdrun('hadoop fs -put {}'. format(filename))

		elif ('upload'in x or 'put'in x or 'send'in x) and ('file'in x or 'data'in x or 'image'in x or 'program'in x) and ('hadoop'in x or 'cluster'in x) and ('empty'in x):
			print('   Sure...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'sure'")
			filename2 = input('Enter file name : ')
			cmdrun('hadoop fs -touchz /{}'. format(filename2))

		elif ('show'in x or 'open'in x or 'check'in x) and ('files'in x) and ('hadoop'in x or 'cluster'in x):
			print('   okk...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'okk'")
			cmdrun('hadoop fs -ls /')
		elif ('delete'in x or 'remove'in x) and ('file'in x or 'data'in x or 'image'in x or 'program'in x) and ('hadoop'in x or 'cluster'in x):
			print('   Sure...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'sure'")
			filename1 = input('Enter your file name : ')
			cmdrun('hadoop fs -rm /{}'. format(filename1))

	####################
		elif ('start'in x or 'run'in x) and ('another'in x) and ('terminal'in x):
			print('   okk...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'okk'")
			cmdrun('gnome-terminal')
		elif ('check'in x) and ('wait time'in x or 'cpu time'in x):
			print('   okk...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'okk'")
			prog = input('Enter program command to run : ')
			cmdrun('time {}'. format(prog))
		elif ('show'in x or 'check'in x) and ('running'in x) and ('process'in x or 'program'in x or 'app'in x or 'software'in x or 'function'in x or 'command'in x):
			print('   okk...')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'okk'")
			cmdrun('ps -aux')
		
		elif (('manunal'in x) or ('man'in x)) and ('mode'in x):
			print('   Ok', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			print('Launching Manual mode...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Launching Manual mode'")
			slp(1)
			man()
		elif ('option' in x) and ('mode'in x):
			print('   Ok', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			print('Launching Option mode...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Launching Option mode'")
			slp(1)
			opt()

		else :
			clr(4)
			print('   I did not understand.... ', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'i did not understand'")
			print('   Please write again.... ', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'please write again'")



def command():
	### CMD MODE
	print('   Sure...')
	print('Launching cmd mode...', end='')
	#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'launching CMD mode'")
	print('CMD mode has been launched', end='')
	#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'CMD mode has been launched'")
	print('[ Root@localhost ]@ ', end='')
	cmdmode = input()
	cmdrun(cmdmode)
	while True :
		print('[ Root@localhost ]@ ' , end='')
		cmdmode = input()
		if 'exit' in cmdmode or 'close' in cmdmode :
			print('   Ok', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			print('Turning off CMD mode...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'turning off CMD mode'")
			print('Turned off CMD mode', end='')
			break
		elif (('manunal'in cmdmode) or ('man'in cmdmode)) and ('mode'in cmdmode):
			print('   Ok', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			print('Launching Manual mode...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Launching Manual mode'")
			slp(1)
			man()
		elif ('option' in cmdmode) and ('mode'in cmdmode):
			print('   Ok', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'ok'")
			print('Launching Option mode...', end='')
			#b = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'Launching Option mode'")
			opt()
		else:
			cmdrun(cmdmode)



def menu():
	print('''
			*****_Menu of this program_*****
	# Program					# Firewall				# Hadoop 
	  1. Open source code				17. Show firewall status		35. Configure hadoop
	  2. Show date and time				18. Start firewall			36. Format hadoop namenode
							19. Stop firewall			37. Show hadoop report
	# Files											38. Show hadoop report in short
	  3. Show all files in current directory	# Apache Httpd				39. Start hadoop namenode
	  4. Show files in another directory		20. Show httpd status			40. Start hadoop datanode
 	  5. Create empty file				21. Start httpd				41. Check namenode/datanode status
	  6. Create directory				22. Stop httpd				42. Upload file on hadoop cluster
	  7. Open file of current directory							43. Upload empty file on hadoop cluster
	  						# Docker				44. Show all uploaded file on hadoop 
	# IP						23. Show docker status			45. Delete any file on hadoop
	  8. Show all IP				24. Start docker			
	  9. Show main IP				25. Stop docker				# Other
	 10. Change IP					26. Show all docker images		46. Launch another terminal
	 11. Check tcp command 				27. Show currently running container	47. Check CPU time
	 						28. Launch new container		48. Show all running processes status
	# RAM						29. Launch new container in background	49*.Launch Command Mode (CMD Mode) 
	 12. Show RAM status				30. Launch already running container	50*. Launch Manual Mode
	 13. Show all partition(already created)	31. Show all launched containers	51. Exit from this program
	 14. Partition of HD				32. Start already launched container	
	 15. Format partition				33. Stop already running container	
	 16. Mount partition				34. Delete all containers		
	 
	''')


clr(6)

print("""	
		 _              _    __________   _             ________     _____     _            _    _________
		| |     /\     | |  | _________| | |           / _______|   / ___ \   | \          / |  |  _______|
		| |    /  \    | |  | | 	 | |          / /          / /   \ \  |  \        /  |  | |
		| |   / /\ \   | |  | |_____	 | | 	     | |          | |     | | |   \      /   |  | |_____
		| |  / /  \ \  | |  | ______|	 | |         | |          | |     | | | |\ \    / /| |  |  _____| 
		| | / /	   \ \ | |  | |          | |         | |          | |     | | | | \ \  / / | |  | |
		| |/ /	    \ \| |  | |________	 | |_______   \ \_______   \ \___/ /  | |  \ \/ /  | |  | |________
		|___/	     \___|  |__________| |_________|   \________|   \_____/   |_|   \__/   |_|  |__________|     """)
				 

#x = #sp.getoutput("espeak-ng -ven-us+m1 -s155 'enter your name '")    
print('   Enter your name : ' , end='')
name = input()
print('   hello {}'. format(name))
#speak('hello {}' . format(name))

"""
0-black
1-red
2-green
3-yellow
4-blue
5-purple
6-light blue
7-white
"""

cls()
slp(1)
 
print('     Select your mode : ')
##sp.getoutput("espeak-ng -ven-us+m1 -s155 'Select your mode'")
print('''
     1). Option mode
     2). Manual mode
     3). Command mode
''') 
option = input('Choose your option : ')

if '1'in option or 'option'in option or 'Option'in option :
	opt()	
	
elif ('2'in option or 'manual'in option or 'Manual'in option) :
	man()

elif ('3'in option or 'command'in option or 'Command'in option) :
	command()
