# taskwarrior-jrnl-hook

Taskwarrior allow annotation of tasks, but I find it less practical than using jrnl to do so. This hook bring together both of this great tools.

* [Taskwarrior](https://taskwarrior.org)
* [jrnl](http://jrnl.sh)

This script was inspirated by [taskwarrior-time-tracking-hook](https://github.com/kostajh/taskwarrior-time-tracking-hook)

## Principal

Starting a task will automatically pass its description to jrnl. If started task have tags they will be added into the title with corresponding symbol in jrnl (by default, jrnl tags are mark with "@").

```sh

$ task list
ID Age D Project                     Tags                     Sch Due        Description                          Urg
-- --- - -------                     ----                     --- ---        ----------------------------------   ---
 1  1d   perso.administration.bill   administration perso         2018-09-21 Pay electricity bill                  14
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

pip install jrnl_hook_taskwarrior

```

Then add the hook to .task/hook folder

```sh
mkdir -p ~/.task/hooks
ln -s ~/.local/bin/taskwarrior_jrnl_hook ~/.task/hooks/on-modify.jrnl

```

## Configuration

Par défaut, ce hook recherche les informations de configuration dans votre fichier de configuration `~/.taskrc`. Les options par défaut sont intégrées dans le crochet, si vous souhaitez modifier le comportement du crochet, placez les options d’entrée dans votre fichier de configuration taskwarrior.

Options :

1. [jrnl name](#jrnl_name)
2. [jrnl configuration](#jrnl_configuration)
3. [tags](#tags)
4. [project](#project)
5. [filter](#filter)

### jrnl name
    
|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_name` | default | jrnl name to write in it|

If specify, this hook will use jrnl name defined in the config, otherwise it will use default jrnl. 

Personaly I written a jrnl for each month, so I add an option to get month name from started task and use it as jrnl name.

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_by_month` | False | Use month as jrnl name|
|`language` | en | langiage to output month |

If set to `True` hook script will call jrnl for the given month. You can specify langue in order to get the right spelling for the month .

### jrnl configuration

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_config` | `~/.jrnl_config` | Path to your jrnl configuration|

In order to use the correct tags symbol you use in your jrnl, the script need to read your jrnl configuration.

### tags

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`jrnl_tags` | True | Add tags to jrnl|

This option allow you to add taskwarrior tags to your jrnl title formated with jrnl tags symbol.

### project

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`add_project` | True | Add project to jrnl|

This option add project entry under your title on jrnl.

### filter 

|Name|Default|Description|
|:--------:|:----------:|:------------------|
|`filter_tags` | None | Task exclude by tags|

This option allow you to exclude by tags tasks that you don't want to see in your jrnl.



