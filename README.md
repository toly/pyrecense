pyrecense
=========

Tool for recense python projects

## features

Now script have only two features, but ones may be very useful for review code of new project:

 - output function/method definitions with repited names
 - output functions/methods what was defined, but used less then 5 times

## usage

    $ ./recense.py -h
    usage: recense.py [-h] -d PROJECT_DIRECTORY

    optional arguments:
      -h, --help            show this help message and exit
      -d PROJECT_DIRECTORY, --project-directory PROJECT_DIRECTORY
                            Project directory for recense