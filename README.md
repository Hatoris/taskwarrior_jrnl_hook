# jrnl_hook_taskwarrior

Taskwarrior allow annotation, but I found it less pratcle than jrnl. In oder, to bring together both of this great tools this hook has been writen.

## Principal

Starting a task will be automaticly pass its description to jrnl. If task have tags they will be added into the title with cotresponding symbol in jrnl (by default, jrnl tags are mark with "@").

```sh

$ task list
ID Age D Project                     Tags                     Sch Due        Description                              Urg
 1 10d   perso.administration        administration perso         2018-09-21 Pay electricity bill                     14
$ task 1 start
```

That action will call jrnl like this

```sh

jrnl Pay electricity bill @administration @perso

```

## Install

```sh

pip install jrnl_hook_taskwarrior

```

Then add the hook to .task/hook folder

```sh

```

## Configuration

By default this hook will look config info in your ~/.taskrc config file. Defaul option are built in the hook, if you want to change parameters addin your jrnl put these follwing entry in your taswarrior config file.
    
```sh
journal_name=default
```

If specify, this hook will use jrnl name defined in the config, otherwise it will use default jrnl.

```sh
journal_config=~/.jrnl_config
```

Specify an other path for .jrnl_config.

```sh
add_tags=True
```
This option allow you to add taskwarrior tags to your jrnl title

```sh
add_project=False
```
This option add project as entry under your title

```sh
jrnl_by_month=False
langue='En'
```
This option is a petsonal one, if set to `True` hook script will call jrnl for the given month. You can specify langue in order to get the right spelling for the month .

Exemple :
    
```sh

task 2 start 
jrnl september add new result on viabilty assay protocol

```




