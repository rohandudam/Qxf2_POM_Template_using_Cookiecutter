--------------------
About the Repo
--------------------
Cookiecutter is a command line utility that creates projects from templates i,e cookiecutter. This repo is created to help you to customize and setup the Qxf2 Framework for your project. This repo will eliminate the need to edit manually various references which you will need when using our framework in your project.

--------------------
Cookiecutter setup
--------------------
The setup is fairly simple. Don't get fooled by the length of this section. We have documented the setup instructions in detail so even beginners can get started. 

__1. Prerequisites__

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

__2. Installation__

Install cookiecutter using below command

`pip install cookiecutter`


--------------------
How to create the template for your repo using cookiecutter
--------------------
__Note:__ We recommand to use command prompt for running these commands (Avoid using Git Bash, for more details refer Known issues section at the end)

1. Traverse to the directory where you want to create project, there are 2 ways to get the Qxf2 POM template
	
	1. Run the cookiecutter command, passing in the link to cookiecutter-pypackage’s HTTPS clone URL like this:
	
		`cookiecutter https://github.com/rohandudam/Qxf2_POM_Template_using_Cookiecutter.git`
	2. Other approach would be to clone it to your local and run the cookiecutter below command
	
		`cookiecutter <path of the repo>`  (For example - cookiecutter c:/code/Qxf2_POM_Template_using_Cookiecutter)

	__Note:__ The project Boilerplate will get created at the current directory path from where you are running the command.

2. After above command is executed following parameters will be prompted to be filled :

	1. directory_name [Qxf2-POM]: [<test-qxf2>] ( Mention the project Directory name)  

	2. project_url [https://www.qxf2.com]: [<https://www.google.co.in>] (Mention the project URL which you want to jumpon)

	3. page_object_name [tutorial_main_page]: [<main_page>] (Mention the first page object name)

	4. page_object_class_name [Tutorial_Main_Page]: [<Main_Page>] (Mention the same page object name but start with capital letter as shown the example)

--------------------
Known Issue(s)
--------------------
1. If you are using Git Bash for running cookiecutter command, please do not use Arrow keys and backspace as it is considering it as input and you will notice that values on generated template.
