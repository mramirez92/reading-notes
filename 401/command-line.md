# The Command Line

## 1. The Command Line

we can have several command lines open and doing different tasks in each at the same time

- optional values to a command typically start with a dash in front "ls -l"
- Shell: defines how the terminal will behave and looks after running (or executing) commands
- Bash: Bourne again shell

## 2. Basic Navigation

linux uses hierarchal structure

- absolute path : in relation to root, starts with /
- relative path: current position in system, don't begin with /
- ` ~ ` (tilde) home directory shortcut, instead of `home/monica/projects` we can navigate there with `~/projects`

## 3. Files

Everything is a file under Linux!

- can use spaces if file names are encased in quote `'cat pictures'`
- backslash (escape character) can also be used `cd cat\ pictures`

## 4. Manual Pages

Manual pages are a set of pages that explain every command available on your system including what they do, the specifics of how you run them and what command line arguments they accept.

`man <command to look up>`

- returns command name, synopsis, description

search for commands with `man -k [search term]`

```markdown
man -k find

btrfs-find-root (8)  - filter to find btrfs root
ffs (3)              - find first bit set in a word
ffsl (3)             - find first bit set in a word
ffsll (3)            - find first bit set in a word
find (1)             - search for files in a directory hierarchy
findfs (8)           - find a filesystem by label or UUID
findmnt (8)          - find a filesystem
git-bisect (1)       - Use binary search to find the commit that introduced a bug
git-cherry (1)       - Find commits yet to be applied to upstream
git-merge-base (1)   - Find as good common ancestors as possible for a merge
git-name-rev (1)     - Find symbolic names for given revs
git-pack-redundant (1) - Find redundant pack files
glob (3)             - find pathnames matching a pattern, free memory from glob()
globfree (3)         - find pathnames matching a pattern, free memory from glob()
lfind (3)            - linear search of an array
Module::Find (3pm)   - Find and use installed modules in a (sub)category
pidof (8)            - find the process ID of a running program.
sane-find-scanner (1) - find SCSI and USB scanners and their device files
systemd-delta (1)    - Find overridden configuration files
tfind (3)            - manage a binary search tree
ttyslot (3)          - find the slot of the current user's terminal in some file
xdg-user-dir (1)     - Find an XDG user dir
```

## 5. File Manipulation

- `mkdir -pv` creates a directory with necessary parent directories, the addition of the -v tells us what its actually doing

```mardown
mkdir -pv linuxtutorialwork/foo/bar
mkdir: created directory 'linuxtutorialwork/foo'
mkdir: created directory 'linuxtutorialwork/foo/bar'

```

- `cp [options] <source> <destination>` copy

- `mv [options] <source> <destination>` move this file/directory to this destination, files can be renamed

```terminal
mv kittens animals/kitties

```

- `rm -r <directory>` removes non-empty directories and ALL of it's files

-----

## Summary

I've had multiple instances where I need to delete directories that are not empty and I always find myself looking up how to. `rm -ri` will come in handy. The manual pages is something I will start using. This will help me search more effectively while working on the terminal. Learning that we can type the tilde as opposed to the home directory to have the same effect is a revelation.

📔[Back to Main Page](../README.md)
