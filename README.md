[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12421504)

# P3 - COMP0010 Shell
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The following repository contains Group P3's implementation of the Shell Coursework.

Group Members: 
- Edgar Tsang
- Robbie Morris 
- Wonjun Lee

Written in 2023, for Professor Sergey Mechtaev.

## Table of Contents

- Executing & Testing Shell
- Convenience Features
- Testing
- UML Diagram
- Application Descriptions

## Executing & Testing Shell

COMP0010 Shell can be executed in a Docker container. To build a container image (let's call it `shell`), run

    docker build -t shell .

To execute the shell in interactive mode, run

    docker run -it --rm shell /comp0010/sh

To execute the shell in non-interactive mode (to evaluate a specific command such as `echo foo`), run

    docker run --rm shell /comp0010/sh -c 'echo foo'

To execute unit tests, run

    docker run -p 80:8000 -ti --rm shell /comp0010/tools/test

Then, the results of unit testing will be available at [http://localhost](http://localhost).

To execute code analysis, run

    docker run -p 80:8000 -ti --rm shell /comp0010/tools/analysis

Then, the results of code analysis will be available at [http://localhost](http://localhost).

To execute test coverage, run

    docker run -p 80:8000 -ti --rm shell /comp0010/tools/coverage

Then, the results of coverage computation will be available at [http://localhost](http://localhost).

To execute mutation tests, run

    docker run -p 80:8000 -ti --rm shell /comp0010/tools/mutation

Then, the results of the mutation tests will be available at [http://localhost](http://localhost).

Please be aware that completing the mutation test could take a substantial amount of time, depending on the hardware it is run.

To execute system tests, your first need to build a Docker image named `comp0010-system-test`:

    docker build -t comp0010-system-test .

Then, execute system tests using the following command (Python 3.7 or higher is required):

    python3 system_test/tests.py -v

Individual system tests (e.g. `test_cat`) can be executed as

    python3 system_test/tests.py -v TestShell.test_cat

## Convenience Features

Our implementation of the Shell contains a variety of convenience features to ensure ease of use and accessibility. Aside from application-related convenience features, such as `color`, we have also implemented autocompleting commands, command input history, and command help features.

Autocompleting commands can be done by pressing `TAB`, command input history can be checked by pressing the `UP` arrow, and using the `-h` / `--help` flag after any application command will output more information about it.

## Testing

Our version of the COMP0010 Shell has unit, property-based, and mutation testing mechanisms. Test cases were made for all scenarios in all files that were written by us, where appropriate. This includes all of the applications, as well as the application_factory, application, call, error, help_decorator, shell, unsafe_decorator, and visitor.

### Unit Testing

Unit testing is a software testing method by which individual units of source code are tested to determine whether they are fit for use. Our Shell implementation incorporates unit testing via that Unittest module.

All reasonable aspects of our code were tested, as shown by the coverage report. Code that was not feasible to be tested, such as ANTLR files, were specifically excluded not unit tested and thus excluded from the coverage report.

### Property-based Testing

Property-based testing checks that a function abides by a certain property that exists inherently. This is done by comparing the output with invariants that must be followed by the function, regardless of the specific output. Our Shell implementation incorporates property-based testing via the Hypothesis module.

Property-based testing was used where appropriate; functions that had clear invariants and specific edge cases were all thoroughly tested. 

### Mutation Testing

Mutation testing, also known as code mutation testing, is a form of white box testing in which specific components of an application's source code are changed to ensure a software test suite can detect the changes. Our Shell implementation incorporates mutation testing via the Mutatest module.

Though all unit and property-based tests pass (as they should), some mutation tests are expected to fail. For example, in mv, the length of args is always 2. Due to this, the mutation args[i + 1] to args[i - 1] will yield the same output.

```python
for i in range(0, len(args), 2):
    source = args[i]
    destination = args[i + 1] -> args[i - 1]
    self.move_file(source, destination, force)
```

This occurs in a few different applications and has been dimissed accordingly.

## UML Diagram

![](https://github.com/comp0010/comp0010-shell-python-p3/blob/master/UML_Diagram_Shell.png)

## Applications

In our version of the COMP0010 Shell, we have implemented the following applications below:

### help

Displays a description of the commands available and syntax to follow.

    help

Use <command> --help or <command> -h for more information about a command.

### cat

Concatenates the content of given files and prints it to stdout:

    cat [FILE]...

- `FILE`(s) is the name(s) of the file(s) to contatenate. If no files are specified, uses stdin.

### cd

Changes the current working directory.

    cd PATH

- `PATH` is a relative path to the target directory.

### color

Changes the font color of the shell; Currently not all colours are supported.

    color COLOR

- `COLOR` specifies the color of text displayed: (Not all supported colors are displayed below)
    - `red` changes the text to red.
    - `purple` changes the text to purple.
    - `reset` resets the text color.

### cp

Copies a file/directory from a source to a destination.

    cp [OPTION] [SOURCE] [DESTINATION]

- `OPTION` specifies the behaviour of cp:
    - `-f` forces a file to be overwritten.
    - `-r` performs a recursive copy for directories (All subfiles and subdirectories copied).
- `SOURCE` specifies the file/directory to be copied.
- `DESTINATION` specifies the output file/directory.

### cut

Cuts out sections from each line of a given file or stdin and prints the result to stdout.

    cut OPTIONS [FILE]

- `OPTION` specifies the bytes to extract from each line:
    - `-b 1,2,3` extracts 1st, 2nd and 3rd bytes.
    - `-b 1-3,5-7` extracts the bytes from 1st to 3rd and from 5th to 7th.
    - `-b -3,5-` extracts the bytes from the beginning of line to 3rd, and from 5th to the end of line.
- `FILE` is the name of the file. If not specified, uses stdin.

### echo

Prints its arguments separated by spaces and followed by a newline to stdout, when no arguments are presented, stdin is used:

    echo [ARG]...

### exit

Exits the shell, ending the process.

    exit

### find

Recursively searches for files with matching names. Outputs the list of relative paths, each followed by a newline.

    find [PATH]? -name PATTERN

- `PATTERN` is a file name with some parts replaced with `*` (asterisk).
- `PATH` is the root directory for search. If not specified, uses the current directory.

### font

Changes the font styling of the text, multiple styles can be used in parallel.

    font FONT

- `FONT` specifies the style of the text displayed:
    - `bold` - **bold text**
    - `italic` - *italicized text*
    - `underline` - <ins>underlined text</ins>
    - `crossed` - ~~Strikethrough text~~
    - `dark`
    - `reversed`
    - `reset`

### grep

Searches for lines containing a match to the specified pattern. The output of the command is the list of lines. Each line is printed followed by a newline.

    grep PATTERN [FILE]...

- `PATTERN` is a regular expression in [PCRE](https://en.wikipedia.org/wiki/Perl_Compatible_Regular_Expressions) format.
- `FILE`(s) is the name(s) of the file(s). When multiple files are provided, the found lines should be prefixed with the corresponding file paths and colon symbols. If no file is specified, uses stdin.

### head

Prints the first N lines of a given file or stdin. If there are less than N lines, prints only the existing lines without raising an exception.

    head [OPTIONS] [FILE]

- `OPTIONS`, e.g. `-n 15` means printing the first 15 lines. If not specified, prints the first 10 lines.
- `FILE` is the name of the file. If not specified, uses stdin.

### ls

Lists the content of a directory. It prints a list of files and directories separated by tabs and followed by a newline. Ignores files and directories whose names start with `.`.

    ls [PATH]

- `PATH` is the directory. If not specified, list the current directory.

### mkdir

Makes a new directory if it does not already exist.

    mkdir [PATH]

- `PATH` is the name of the directory.

### mv

Moves a file from one directory to another.

    mv [OPTION] [SOURCE] [DESTINATION]

- `OPTION`:
    - `-f` forces the destination file to be overwritten if it already exists.
- `SOURCE` is the source file to be moved.
- `DESTINATION` is the path to which the file is to be moved.
    

### pwd

Outputs the current working directory followed by a newline.

    pwd

### rm

Removes the file at the path specified.

    rm [PATH]

- `PATH` is the file to be removed. Cannot remove directories with rm.

### rmdir

Removes the specified directory, first removing all files and subdirectories within.

    rm [DIRECTORY]

- `DIRECTORY` is the directory to be removed.

### sed

Replaces a string with another string within a file.

    sed [OPTIONS] [FILE]

- `OPTIONS` follows the format [PROCESS/PATTERN/REPLACEMENT/FLAG]
    - `PROCESS`
    - `PATTERN` is the string to be replaced
    - `REPLACEMENT` is the replacement
    - `FLAG` is the option to replace all occurences or just a certain line
        - `g` replaces all occurences
- `FILE` is the name of the file. If not specified, uses stdin.

### sort

Sorts the contents of a file/stdin line by line and prints the result to stdout.

    sort [OPTIONS] [FILE]

- `OPTIONS`:
    - `-r` sorts lines in reverse order
- `FILE` is the name of the file. If not specified, uses stdin.

### tail

Prints the last N lines of a given file or stdin. If there are less than N lines, prints only the existing lines without raising an exception.

    tail [OPTIONS] [FILE]

- `OPTIONS`, e.g. `-n 15` means printing the last 15 lines. If not specified, prints the last 10 lines.
- `FILE` is the name of the file. If not specified, uses stdin.

### touch

Creates an empty file if no file exists in the directory under the same name.

    touch [FILE]

- `FILE` is the name of the file, can be a filepath e.g. `dir1/filename.txt`.

### uniq

Detects and deletes adjacent duplicate lines from an input file/stdin and prints the result to stdout.

    uniq [OPTIONS] [FILE]

- `OPTIONS`:
    - `-i` ignores case when doing comparison (case insensitive)
- `FILE` is the name of the file. If not specified, uses stdin.

### wc

Counts the number of lines, words, and characters in a file/stdin.

    wc [OPTIONS] [FILE]

- `OPTIONS` where multiple options can be used in conjunction e.g. `-l -w`:
    - `l` counts the number of lines
    - `w` counts the number of words
    - `m` counts the number of characters
- `FILE` is the name of the files to be used. If not specified, uses stdin.

### Unsafe applications

In COMP0010 Shell, each application has an unsafe variant. An unsafe version of an application is an application that has the same semantics as the original application, but instead of raising exceptions, it prints the error message to its stdout. This feature can be used to prevent long sequences from terminating early when some intermediate commands fail. The names of unsafe applications are prefixed with `_`, e.g. `_ls` and `_grep`.
