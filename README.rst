netflix exploit automation program
=====================

Getting Started
================

    * If you want to run `exploit_automation` locally:
    * Unzip the tarball into a directory
    $ tar -xvf WM-NETFLIX-Python.tar.gz
    $ cd netflix
    $ make setup
    $ source "$HOME/.virtualenvs/exploit_automation/bin/activate"
    $ exploit_automation
    * You should now be able to run the `exploit_automation` command anywhere


Design Assumptions
==================

    * `Python 3.10.5` and newer
    * The secret is alphanumeric string with length between `30` and `50` characters

Run Tests
==========

    * If you want to run tests:
    * cd to the unzipped folder
    $ python -m unittest tests/test_vulnerable_urls.py



