#!/usr/bin/env python
"""Create a stub python solution for a Project Euler problem."""

import argparse
import os
import textwrap

import bs4
import jinja2
import requests

EULER_URL = r"https://projecteuler.net/problem=%s"
TEMPLATE = '''#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Project Euler: {{index}}

{{url}}

{{title}}

{{description}}
"""

PROBLEM = {{problem}}
SOLVED = False
SPEED = float("inf")
TAGS = []


def main():
    """Solve problem."""
    print "Project Euler: %04d" % PROBLEM
    print "Unsolved"


if __name__ == "__main__":
    main()'''


def problem_attributes(problem_number):
    """Return attributes from web."""
    url = EULER_URL % problem_number
    request = requests.get(url)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    title = soup.find("h2").text.strip()
    description = "\n\n".join([
        textwrap.fill(text, 79)
        for text in soup.find("div", class_="problem_content").stripped_strings
        ])
    return {
        "description": description,
        "index": "%04d" % problem_number,
        "problem": problem_number,
        "title": title,
        "url": url}


def main():
    """Perform main logic."""

    filename = "problems/e%04d_01.py" % ARGS.problem_number

    if ARGS.use_stdout is False and os.path.exists(filename):
        if not ARGS.overwrite:
            print "%s already exists, not overwriting without -f" % filename
            return

    template = jinja2.Template(TEMPLATE)
    attribs = problem_attributes(ARGS.problem_number)
    data = template.render(attribs).encode("UTF-8")
    if ARGS.use_stdout:
        print data
    else:
        open(filename, "w").write(data+"\n")
        print "Wrote %s" % filename
        os.chmod(filename, 0755)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="Stub creator")
    PARSER.add_argument(
        "-f",
        "--force",
        dest="overwrite",
        action="store_true",
        help="force overwriting existing file")
    PARSER.add_argument(
        "--stdout",
        dest="use_stdout",
        action="store_true",
        help="write to stdout")
    PARSER.add_argument(
        "problem_number",
        type=int,
        help="Project Euler problem number")
    ARGS = PARSER.parse_args()
    main()
