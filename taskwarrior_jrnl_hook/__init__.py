#!/usr/bin/env python3
from babel.dates import format_date
import datetime
import json
import yaml
import os
import re
import subprocess
import sys

from taskw import TaskWarrior

TIME_FORMAT = "%Y%m%dT%H%M%SZ"

original = json.loads(sys.stdin.readline())
modified = json.loads(sys.stdin.readline())

if "start" in modified and "start" not in original:

    # read config info from taskwarrior config file
    w = TaskWarrior()
    TASK_CONFIG = w.load_config()

    # read infos from taskrc config file
    JRNL_NAME = TASK_CONFIG.get("jrnl_name", "default")
    JRNL_CONFIG_PATH = os.path.expanduser(
        TASK_CONFIG.get("jrnl_config", "~/.jrnl_config")
    )
    ADD_TAGS = TASK_CONFIG.get("add_tags", True)
    ADD_PROJECT = TASK_CONFIG.get("add_project", False)
    JRNL_BY_MONTH = TASK_CONFIG.get("jrnl_by_month", False)
    LANGUAGE = TASK_CONFIG.get("language", "en")
    FILTER_TAGS = TASK_CONFIG.get("filter_tags", False)

    # read informations from modifed task

    TAGS = modified.get("tags", [])
    PROJECT = modified.get('project', '')

    # read info from jrnl_config
    with open(JRNL_CONFIG_PATH, "r") as f:
        try:
            JRNL_CONFIG = json.load(f)
        except json.JSONDecodeError:
            JRNL_CONFIG = yaml.load(f, Loader=yaml.FullLoader)
    TAGS_SYMBOL = JRNL_CONFIG.get("tagsymbols", "@")

    title = modified["description"]

    #add taskwarrior task to title
    if TAGS and ADD_TAGS:
        for tag in TAGS:
            title += f" {TAGS_SYMBOL}{tag}"

    #add taskwarrior project to new entry
    if ADD_PROJECT and PROJECT:
        title += f"\nproject:{PROJECT}"


    # Extract month name from task date
    if JRNL_BY_MONTH:
        date = datetime.datetime.strptime(modified["start"], TIME_FORMAT)
        JRNL_NAME = format_date(date, "MMMM", locale=LANGUAGE)
        # French month can have accent, jrnl do not support journal name with it
        JRNL_NAME.replace(r"é", "e")
        JRNL_NAME.replace(r"û", "u")

    #Check if started task is in filtered task list
    if FILTER_TAGS and TAGS:
        FILTER_TAGS = list(FILTER_TAGS.split(","))
        filtered = any(map(lambda tag : tag in FILTER_TAGS,TAGS))
    else:
        filtered = False

    if not filtered:
        p = subprocess.Popen(["jrnl", JRNL_NAME, title], stdout=subprocess.PIPE)
        p.communicate()

sys.stdout.write(json.dumps(modified, separators=(",", ":")))
sys.exit(0)
