A scripty tool used to assist you in configuring your own build scripts
be it Make or a bash/python script. If you can obtain the compilation
output from an application you are using to build for you. You can forge
your own build path. This tool will assist in getting the proper commands,
flags, options, libraries, etc. from a compilation output you provide for it.

## Usage

```
./dis-compilate.py -h
usage: ./dis-compilate [options] [source_file]

Retreives useful options, flags, libraries, etc. from a verbose compilation
file.

positional arguments:
  source_file

optional arguments:
  -h, --help         show this help message and exit
  --commands         list commands used for compilation
  --flags            list flags used for compilation
  --options          list options used for compilation
  --libraries        list libraries used for compilation
  --include INCLUDE  include any commands to search for that may not be
                     supported for the script
```
