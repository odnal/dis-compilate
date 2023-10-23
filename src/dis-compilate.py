#!/usr/bin/python -O

# This tool is used to help configure your own build structure
# be it Make or some executable script. Sometimes its nice to 
# have a say in what compilation flags you want to include rather
# than have whatever application you are using do it for you when 
# building your program. If you can obtain the verbose output from
# your applications compilation step and feed it into dis-compilate
# you may find useful libraries, flags, and options to "steal" and
# forge your own path.

import argparse

keywords = ['bin', 'gcc', 'g++', 'objdump', 'objcop', 'size', 'as', 'ld']

# Program usage/layout 
parser = argparse.ArgumentParser(prog="./dis-compilate", description="Retreives useful options, flags, libraries, etc. from a verbose compilation file.", usage="%(prog)s [options] [source_file]")
parser.add_argument("--commands", action="store_true", help="list commands used for compilation")
parser.add_argument("--flags", action="store_true", help="list flags used for compilation")
parser.add_argument("--options", action="store_true", help="list options used for compilation")
parser.add_argument("--libraries", action="store_true", help="list libraries used for compilation")
parser.add_argument("--include", action="store", help="include any commands to search for that may not be supported for the script")
parser.add_argument("source_file", type=open)

args = parser.parse_args()
file_data = args.source_file.readlines()

if __debug__:
  print(args)
  print(file_data)


# Remove '\n' from file data
file_data_new = []
for line in file_data:
  new_line = line.replace('\n', '')
  file_data_new.append(new_line)


# Include any commands that may not be supported
if args.include:
  keywords.append(args.include)


# Commands used
commands = []
sep = ' '
if args.commands:
  for data in file_data_new:
    parts = data.split(sep, 1)[0]
    commands.append(parts) 
  for command in commands:
    keyword_exist = True
    for word in keywords:
      if word in command:
        print(command)
        break
      else:
        keyword_exist = False


# Flags used (should contain options as flags are usually aliases for options)
sep = ' '
if args.flags:
  for data in file_data_new:
    flag_exist = False
    parts = data.split(sep)
    for part in parts:
      if part.startswith('-'):
        print(''.join(part), end=" ")
        flag_exist = True
    if flag_exist:
      print()


# Options used (usually lead with '--' i.e --foo)
sep = ' '
if args.options:
  for data in file_data_new:
    option_exist = False
    parts = data.split(sep)
    for part in parts:
      if part.startswith('--'):
        print(''.join(part), end=" ")
        option_exist = True
    if option_exist:
      print()


# Libraries used
sep = ' '
if args.libraries:
  for data in file_data_new:
    lib_exist = False
    parts = data.split(sep)
    for part in parts:
      if part.startswith('-I'):
        print(''.join(part), end=" ")
        lib_exist = False
    if lib_exist:
      print()

