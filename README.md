# Launcher
 A simple script that launches all your working directories from the terminal

A simple script that launches all your working directories from the terminal

Its monotonous task to navigate to multiple working directories first thing in the morning after I boot my machine in office.
Hence, I wrote a quick script that will automatically launch all my pre-configured directories.

## Setup
1) Clone the repository in any directory.

2) In config.json, set your configurations as a key-value pair, something like this:
 
 ```
 {
	"project1": {
		"working-directory": "/home/user/someproject"
	},
	"project2": {
		"working-directory": "/home/user/x/y/project2"
	}
}
```
You can obviously add as many projects as you like. Make sure that your json syntax is correct.

3) (optional but strongly recommeded) Once the config.json is done, add an alias in your .bashrc file(~/.bashrc) as 
`alias launchtabs='python /path/to/launcher.py'`
You can set the name of the alias to any name you want.


## Running
(Assuming you have set the alias in .bashrc and the name of the alias is launchtabs. if you have set any other alias name, 
then replace launchtabs with that name wherever applicable).

1.  You can run the script in two ways:

   1.  Default mode:
   
        `$launchtabs`

        This will open all the directories mentioned in your config.json file
    
   2.  Specific directory:
   
        If you wish to open only a specific directory of all the directories in config.json, then you can pass the argument as
   
        `$launchtabs project1`
    
        You can pass multiple directories as arguments
      `$launchtabs project1 project2 project3`

2.  If you have not set the alias in .bashrc, then you need to navigate to the launcher.py file and then run the script as
`python launcher.py`. You can also pass the arguments the same way as mentioned above.

Thanks.
