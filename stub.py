#!/usr/bin/env python
"""Create a stub python solution for a Project Euler problem."""

import argparse
import os
import textwrap
import urlparse

import bs4
import jinja2
import requests

EULER_URL = r"https://projecteuler.net/problem=%s"
TEMPLATE = "resources/stub.py.j2"


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
        "resources": [
            a.get("href")
            for a in soup.find_all("a")
            if "resources" in a.get("href")
            ],
        "title": title,
        "url": url,
        }


def get_resource(url, resource):
    """Download additional resource into standard path"""
    resource_url = urlparse.urljoin(url, resource)
    filename = "resources/" + resource.rsplit("/", 1)[-1]
    request = requests.get(resource_url, stream=True)
    with open(filename, "wb") as res_file:
        for chunk in request.iter_content():
            res_file.write(chunk)
    print "Wrote %s" % filename


def main():
    """Perform main logic."""

    filename = "problems/e%04d_01.py" % ARGS.problem_number

    if ARGS.use_stdout is False and os.path.exists(filename):
        if not ARGS.overwrite:
            print "%s already exists, not overwriting without -f" % filename
            return

    with open(TEMPLATE) as template_file:
        template_content = template_file.read()
    template = jinja2.Template(template_content)
    attribs = problem_attributes(ARGS.problem_number)
    data = template.render(attribs).encode("UTF-8")
    if ARGS.use_stdout:
        print data
    else:
        open(filename, "w").write(data+"\n")
        print "Wrote %s" % filename
        os.chmod(filename, 0755)
        for resource in attribs["resources"]:
            get_resource(attribs["url"], resource)


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
