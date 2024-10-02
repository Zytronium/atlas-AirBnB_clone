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

### Example usage

<details>
<summary>See Example Output</summary>

```
Welcome to AirBnB Clone Console! Type "help" or "?" for a list of commands. Type "exit" or "quit" to exit.
(hbnb) ? help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create   exit  quit      selfdestruct  update
all  destroy  help  rickroll  show        

(hbnb) ?

Documented commands (type help <topic>):
========================================
EOF  create   exit  quit      selfdestruct  update
all  destroy  help  rickroll  show        

(hbnb) help exit
Exit the program.
(hbnb) help EOF
EOF signal (usually ctl+d) will run this to exit the program.
(hbnb) help all

Prints the representations of all instances of the given class name
Usage: all <class name>
        
(hbnb) all BaseModel
[]
(hbnb) create User
62d68c37-8159-4c89-b13c-1cc5206e2601
(hbnb) all User
["[User] (62d68c37-8159-4c89-b13c-1cc5206e2601) {'id': '62d68c37-8159-4c89-b13c-1cc5206e2601', 'created_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205153), 'updated_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205219), 'email': '', 'password': '', 'first_name': '', 'last_name': ''}"]
(hbnb) create Place
c2f58d25-bc59-42ad-a442-3f516673bfcf
(hbnb) all BaseModel
["[User] (62d68c37-8159-4c89-b13c-1cc5206e2601) {'id': '62d68c37-8159-4c89-b13c-1cc5206e2601', 'created_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205153), 'updated_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205219), 'email': '', 'password': '', 'first_name': '', 'last_name': ''}", "[Place] (c2f58d25-bc59-42ad-a442-3f516673bfcf) {'id': 'c2f58d25-bc59-42ad-a442-3f516673bfcf', 'created_at': datetime.datetime(2024, 10, 1, 22, 36, 5, 450135), 'updated_at': datetime.datetime(2024, 10, 1, 22, 36, 5, 450212), 'city_id': '', 'user_id': '', 'name': '', 'description': '', 'number_rooms': 0, 'number_bathrooms': 0, 'max_guest': 0, 'price_by_night': 0, 'latitude': 0.0, 'longitude': 0.0, 'amenities': []}"]
(hbnb) all Place
["[Place] (c2f58d25-bc59-42ad-a442-3f516673bfcf) {'id': 'c2f58d25-bc59-42ad-a442-3f516673bfcf', 'created_at': datetime.datetime(2024, 10, 1, 22, 36, 5, 450135), 'updated_at': datetime.datetime(2024, 10, 1, 22, 36, 5, 450212), 'city_id': '', 'user_id': '', 'name': '', 'description': '', 'number_rooms': 0, 'number_bathrooms': 0, 'max_guest': 0, 'price_by_night': 0, 'latitude': 0.0, 'longitude': 0.0, 'amenities': []}"]
(hbnb) show Place 62d68c37-8159-4c89-b13c-1cc5206e2601
** no instance found **
(hbnb) show User 62d68c37-8159-4c89-b13c-1cc5206e2601
[User] (62d68c37-8159-4c89-b13c-1cc5206e2601) {'id': '62d68c37-8159-4c89-b13c-1cc5206e2601', 'created_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205153), 'updated_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205219), 'email': '', 'password': '', 'first_name': '', 'last_name': ''}
(hbnb) help update

Update an instance by adding or changing an attribute.
The 'created_at' or 'updated_at' attributes cannot be modified.
If the given attribute name doesn't exist, a new one will be created.
Strings with spaces must have double quotes. (Lists with spaces do not)
Usage: update <class name> <id> <attribute name> <attribute value>
        
(hbnb) update User 62d68c37-8159-4c89-b13c-1cc5206e2601 first_name Joe
(hbnb) update User 62d68c37-8159-4c89-b13c-1cc5206e2601 last_name Mama
(hbnb) update User 62d68c37-8159-4c89-b13c-1cc5206e2601 nickname "Jomama Jobama"
(hbnb) update User 62d68c37-8159-4c89-b13c-1cc5206e2601 fav_songs ['never gonna give you up', 'rub some bacon on it', 'complete silence', True, 28, 'random data', -0.2, attr_name]
(hbnb) show User 62d68c37-8159-4c89-b13c-1cc5206e2601
[User] (62d68c37-8159-4c89-b13c-1cc5206e2601) {'id': '62d68c37-8159-4c89-b13c-1cc5206e2601', 'created_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205153), 'updated_at': datetime.datetime(2024, 10, 1, 22, 38, 25, 986322), 'email': '', 'password': '', 'first_name': 'Joe', 'last_name': 'Mama', 'nickname': '"Jomama Jobama"', 'fav_songs': ['never gonna give you up', 'rub some bacon on it', 'complete silence', True, 28, 'random data', -0.2, 'fav_songs']}
(hbnb) exit
SmartFridge@fedora:~/PycharmProjects/atlas-airbnb_clone$ ./console.py 
Place.__init__() got an unexpected keyword argument 'id'
Welcome to AirBnB Clone Console! Type "help" or "?" for a list of commands. Type "exit" or "quit" to exit.
(hbnb) show User 62d68c37-8159-4c89-b13c-1cc5206e2601
[User] (62d68c37-8159-4c89-b13c-1cc5206e2601) {'id': '62d68c37-8159-4c89-b13c-1cc5206e2601', 'created_at': datetime.datetime(2024, 10, 1, 22, 35, 57, 205153), 'updated_at': datetime.datetime(2024, 10, 1, 22, 38, 25, 986322), 'email': '', 'password': '', 'first_name': '', 'last_name': '', 'nickname': '"Jomama Jobama"', 'fav_songs': ['never gonna give you up', 'rub some bacon on it', 'complete silence', True, 28, 'random data', -0.2, 'fav_songs']}
(hbnb) destroy User 62d68c37-8159-4c89-b13c-1cc5206e2601
(hbnb) all User
[]
(hbnb) show User 62d68c37-8159-4c89-b13c-1cc5206e2601
** no instance found **
(hbnb) quit
username@windows:~/atlas-airbnb_clone$ ./virus.exe
deleting system32...
^C^C
unable to cancel currently running operation. Error 404^C^C^̴C̵^̴̥̺̥̫̱̞̆͋C̴̬̺̐̓́̎͆͝^̸͎̙́̒͌̑͗̉̋̍͂͝Ç̴̼͔͉̻͎͚͔͕̗̤̯̝͇̗͌͛̀͋̄̄ͅ 
```
Sorry for the inconvenience, we'll be back with more examples after sorting
out some technical difficulties...
</details>

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
- settings
  - Change console settings.
  - Usage:
    - `settings <setting> <value>` | change a setting's value
    - `settings <setting>` | see a setting's current value
    - `settings` | list all settings and their current values
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
