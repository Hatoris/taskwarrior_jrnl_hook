#!/usr/bin/env python3
from babel.dates import format_date
import datetime
import json
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

    # read info from jrnl_config
    with open(JRNL_CONFIG_PATH, "r") as f:
        JRNL_CONFIG = json.load(f)
    TAGS_SYMBOL = JRNL_CONFIG.get("tagsymbols", "@")

    title = modified["description"]

    # add taskwarrior task to title
    if "tags" in modified and ADD_TAGS:
        for tag in modified["tags"]:
            title += f" {TAGS_SYMBOL}{tag}"

    # add taskwarrior project to new entry
    if ADD_PROJECT:
        title += f"\nproject:{modified['project']}"

    # Extract month name from task date
    if JRNL_BY_MONTH:
        date = datetime.datetime.strptime(modified["start"], TIME_FORMAT)
        JRNL_NAME = format_date(date, "MMMM", locale=LANGUAGE)

    # Check if started task is in filtered task list
    if FILTER_TAGS:
        FILTER_TAGS = list(FILTER_TAGS.split(","))
        filtered = any(map(lambda tag: tag in FILTER_TAGS, modified["tags"]))

    if not filtered:
        p = subprocess.Popen(["jrnl", JRNL_NAME, title], stdout=subprocess.PIPE)
        p.communicate()

sys.stdout.write(json.dumps(modified, separators=(",", ":")))
sys.exit(0)
