# taskwarrior_jrnl_hook

Taskwarrior allow annotation of tasks, but I find it less practical than using jrnl to do so. This hook bring together both of this great tools.

* [Taskwarrior](https://taskwarrior.org)
* [jrnl](http://jrnl.sh)

This script was inspirated by [taskwarrior-time-tracking-hook](https://github.com/kostajh/taskwarrior-time-tracking-hook)

## Principal

Starting a task will automatically pass its description to jrnl. If started task have tags they will be added into the title with corresponding symbol in jrnl (by default, jrnl tags are mark with "@").

```sh

$ task list
ID Tags                                  Due              Description       
 1  administration perso     2018-09-21 Pay electricity bill
$ task 1 start
```

That action will call the hook and run jrnl as a subprocess.

```sh
jrnl "Pay electricity bill @administration @perso"
```

Now, if you look in your jrnl you should see task description added as title with tags from taskwarrior.

```sh
jrnl -1
2018-09-21 9h35 Pay electricity bill @administration @perso
```

## Install

```sh
pip install taskwarrior-jrnl-hook
```

Then add the hook to .task/hook folder

```sh
mkdir -p ~/.task/hooks
ln -s ~/.local/bin/taskwarrior_jrnl_hook ~/.task/hooks/on-modify.jrnl
```

## Configuration

By default this hook will look config info in your ~/.taskrc config file. Default options are built in the hook, if you want to change hook behavior put options entry in your taskwarrior config file.

Options :

1. [jrnl name](#jrnl_name)
2. [jrnl configuration](#jrnl_configuration)
3. [tags](#tags)
4. [project](#project)
5. [filter](#filter)

### jrnl name
    
|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_name` | default | jnrl name to call|

If specify, this hook will use the jrnl name defined in the config, otherwise it will use `default` as jrnl name.

Personally I write a journal for each month, so I added an option to get month name from started task and use it as jrnl name.

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_by_month` | False | Use month as jrnl name|
|`language` | en | month's language to output| 

If set to `True` hook script will call jrnl for the given month. You can specify language in order to get the right spelling for the month. Month is written in all letters with no capital. 

### jrnl configuration

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_config` | `~/.jrnl_config` | Path to your jrnl configuration|

In order to use correct tags symbol used in your jrnl, the script need to read your jrnl's configuration.

### tags

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_tags` | True | Add tags to jrnl|

This option allow you to add taskwarrior tags to your jrnl's title.

### project

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`add_project` | True | Add project to jrnl|

This option add project name under your title in the body.

### filter 

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`filter_tags` | None | Tasks to be excluded by tags|

This option allow you to exclude by tags tasks that you don't want to see in your jrnl.



