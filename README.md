[![Loading Image](/src/assets/images/mapping_selection.png)]

# Gitlab-Explorer
Used to pull Gitlab projects and branches from older on-premise installation (tested on GitLab 6.4.3)

Written by Brandon Volesky

Gitlab Explorer is a tool that is used to quickly clone down mappings because the web version is turtle slow.
The tool takes in a query and searches all *public* projects and uses the results to pull down mappings automatically.
Just double-click the python script from anywhere to run

	Navigation:
		On any screen you can type 'back' to go to the previous screen
		On any screen you can type 'exit' to quit the explorer


Settings:
	Query Locking (v1+):
		Right off the bat Gitlab Explorer will prompt you for what type of mapping you want to choose. This is used for filtering
		queries and dramatically increases performance in certain situations. If you're tired of always getting asked this and if you're
		the type of person that never really pulls standard mappings, or the opposite where you almost never pull custom mappings you can
		bypass this first prompt by LOCKING your query type by following the instructions below:

			1.) Navigate to your home directory (C:\users\ab123456)
			2.) Open your settings.pb file. If you don't have one, copy one from Gitlab Explorer folder and place it in your home directory
			3.) Add one of the following entries below on a new line of your settings.pb file to LOCK the mapping type for filtering queries then save:
			
						gitlab_explorer=standard
								OR
						gitlab_explorer=custom
								OR
						gitlab_explorer=all
	
	Custom Output Paths(v2+):
		You can now specify what folder you want your mappings to pull down to.
			1.) Navigate to your home directory (C:\users\ab123456)
			2.) Open your settings.pb file. If you don't have one, copy one from Gitlab Explorer folder and place it in your home directory
			3.) Add the following entry below on a new line of your settings.pb file to specify the output path then save:
			
						gitlab_explorer_output_path="C:\Enter\Your\Path\Here"
	
	Branch Support (v2+):
		Branch support allows you to check out a specific branch when you pull a mapping. Output schemes have been deprecated and LISTS mode will be the only default. No settings modification needed.
