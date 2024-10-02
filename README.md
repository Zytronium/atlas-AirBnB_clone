# AirBnB Clone Console

---
AirBnB Clone is exactly what it sounds like, or at least based on it. It is
based on a console for AirBnB. With it, you can create, update, and delete
instances of Users, Cities, Places, Amenities, Reviews, etc.  

The console is a command line interpreter. In it, you can execute specially
built commands to interact with the AirBnB (clone) database. It also contains a
few custom commands unrelated to the database, just for fun. One command even
has a sound effect, and you will have to have the vlc or python-vlc package
installed. If you have pip installed, the most likely methods to install it are:
```bash
pip install vlc
```
```bash
pip install python-vlc
```
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && sudo python get-pip.py
```
Installing vlc is not required to run it, and you can continue without sound.
Run with the additional program argument "-i" or "--ignore-warnings" to ignore
the warning printed on startup when vlc is not installed.
---

### How to start the console
Because of certain restrictions, this console was designed for Python 3.8,*
though it works on the latest Python 3.12 and most likely with 3.13 (whose
expected release date is Oct 7th 2024). It is also recommended to use a
terminal that supports the following text effects: colors, bold, concealed,
reversed, and blinking.

To start the command interpreter, the best way to run it is by opening it in
a terminal. Here are the most likely commands that are needed to run in the
terminal, based on which operating system you are on (assuming the current
directory is `atlas-AirBnB_clone`):

<details>
<summary>Linux (or WSL)</summary>

With python installed in /bin/python3:
```bash 
./console.py
```
With python installed somewhere else:
```bash
python3 ./console.py
```
or
```bash
python ./console.py
```
</details>

<details>
<summary>MacOS</summary>

```zsh
./console.py
```
or 
```zsh
python3 console.py
```
</details>

<details>
<summary>Windows</summary>

```shell
.\console.py
```
or
```shell
python3 .\console.py
```
</details>

<details>
<summary>Minecraft (Command Block)</summary>

```commandblock
/execute as @p run file[name=console.py]
```
Okay, maybe that doesn't work in Minecraft, but it could be recreated in
Minecraft with some time and dedication.
</details>

*: Support for Python 3.8 will drop when 3.13 comes out sometime around October
7th. It is therefore recommended to use 3.9 or later instead, if you are
running it after that date.

---

### How to use it
To use the console, you can enter commands to interact with the database.
For example, `create User` will create a new user and print out its ID so
that you can keep track of it. `show User` will show its details. Type
`help` or `?` for a list of commands. Type `help` or `?` followed by a command
name to see what the command does. type `exit`, `quit`, or send EOF signal
(usually ctrl+d) to exit the console. Below are some example usages and a list
of every command and what it does.

### Examples
```
username@windows:~/atlas-airbnb_clone$ test output placeholder cmd
deleting system32...
^C^C
unable to cancel currently running operation. Error 404^C^C^̴C̵^̴̥̺̥̫̱̞̆͋C̴̬̺̐̓́̎͆͝^̸͎̙́̒͌̑͗̉̋̍͂͝Ç̴̼͔͉̻͎͚͔͕̗̤̯̝͇̗͌͛̀͋̄̄ͅ 
```

### Commands

- ?, help:
  - Displays a list of available commands, or show documentation for a specific command
  - Usage: (`<>` indicates an argument. Do not type the brackets.)
    - `help`
    - `?`
    - `help <command>`
    - `? <command>`
- exit, quit, EOF (ctrl+d)
  - Exits the command line interpreter.
  - Usage:
    - `exit`
    - `quit`
    - `EOF`
    - `^d` (ctrl+d)
- create
  - Creates and saves an instance of className and prints the ID.
  - Usage:
    - `create <className>`
- destroy
  - Deletes the specified instance.
  - Usage:
    - `destroy <class name> <id>`
- update
  - Updates an instance by adding or changing an attribute.
  - The 'created_at' or 'updated_at' attributes cannot be modified.
  - If the given attribute name doesn't exist, a new one will be created.
  - Usage:
    - `update <class name> <id> <attribute name> <attribute value>`
- all
  - Prints the representations of all instances of the given class name
  - Usage:
    - `all <class name>`
- show
  - Prints the string representation of an instance based on the class name and id
  - Usage:
    - `show <class name> <id>`
- rickroll
  - Rickroll the user by opening the video on their default browser.
  - *Might not work on Windows or WSL
  - Usage:
    - `rickroll`
- selfdestruct
  - Activates a countdown from the specified number, or 5 if not given.
  Exits the command line interpreter when the countdown reaches 0.
  - Usage:
    - `selfdestruct <number>`
    - `selfdestruct`

Fun challenge: find the easter egg in the program.
There's a hidden command that does something special.
