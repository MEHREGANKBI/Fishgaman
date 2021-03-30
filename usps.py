import os
conf_dict = {'username' : input('user? '), 
	'userpass' : input('pass? '),
	'chromedriver_path' : input('chromedriver path? '),
	'font_path' : 'DejaVuSans.ttf',
	'pre_wallpaper_path' : 'ubuntu-rgb-sm.png',
	'edited_wallpaper_path' : 'ubuntu-patched-finale.png' ,
	'logfile_path' : 'netlog.log',
	'cwd': os.getcwd()}
	

# Replace the inputs with YOUR credentials and paths. 
# If you wish to change the wallpaper to be another image, change the pre-wallpaper path
