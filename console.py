#!/bin/python3
"""
This is the main module for running the command line interpreter,
aka the console. Run this to run the command line interpreter. Read
the readme for a list of commands and more detailed info.
"""
import sys
from sys import argv
from os import isatty, getcwd
try:
    import vlc
    sound = True
except ImportError:
    argc = len(argv)
    if (not (argc > 1 and (argv[1] == '-i' or argv[1] == '--ignore-warnings'))
        and not isatty(sys.stdin.isatty())):
        print("Could not import vlc. Please install package 'vlc' "
              "to hear audio. 1 command uses sound.")
        print("One possible command to install vlc would be this command:")
        print("pip install vlc")
        print("or, if that doesn't work, try:")
        print("pip install python-vlc")
        print("The console will continue without sound. To run without this "
              "message, do './console.py -i' or './console.py --ignore-warnings'\n")
    sound = False
import webbrowser
import os
from cmd import Cmd
from time import sleep
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.colors import *
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(Cmd):
    """
    the main command line interpreter class
    """
    if isatty(sys.stdin.isatty()):  # only sets intro in interactive
        intro = ('Welcome to AirBnB Clone Console! Type '
                      '"help" or "?" for a list of commands. Type '
                      '"exit" or "quit" to exit.')
        prompt = '(hbnb) \033[7m'  # reverses background & foreground
    else:
        prompt = '(hbnb) '

    # ==================== override cmd methods ====================

    def precmd(self, line):
        """
        Overrides the default method the runs between when the input is parsed
        and when the command is run. This override resets the text color to
        undo the effect from adding \033[7m to the prompt, which reverses the
        background and foreground colors for the user input. This makes sure
        that the output doesn't retain this effect.
        :param line: user input
        :return: the same thing the original command returns, which is line,
        according to the source code for cmd.py.
        """
        reset_color()
        return super().precmd(line)

    def emptyline(self):
        """
        Overrides default method that runs when en empty command is run.
        Instead, it will do nothing when there is no command.
        """
        pass

    def default(self, line):
        """
        Overrides default method that runs if the given command is not found.
        If the input is "easter egg" then it runs a hidden command that is not
        listed when you run "help"
        :param line: user input
        """
        if line == "easter egg":
            print("You found the easter egg!")
            sleep(3)
            webbrowser.open_new_tab(
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            print("Never gonna give you up!")
        else:
            super().default(line)

    # ======================== user commands ========================

    # ======================== exit commands ========================

    @staticmethod
    def do_exit(args):
        """Exit the program."""
        return True

    @staticmethod
    def do_quit(args):
        """Exit the program."""
        return True

    @staticmethod
    def do_EOF(args):
        """EOF signal (usually ctl+d) will run this to exit the program."""
        print()  # Prints an extra line to force the next cmd prompt in
                 # the terminal to be on a separate line.
        return True

    # ================== data interaction commands ==================

    @staticmethod
    def do_create(clsname):
        """
Creates and saves an instance of className and prints the ID.
className: name of the class of the new instance to be created
Usage: create <className>
        """
        cls = HBNBCommand.get_class(clsname)
        if cls is None:
            return

        new_instance = cls()
        new_instance.save()  # clay - changed this to new_instance.save()
        print(new_instance.id)

    @staticmethod
    def do_update(argstr):
        """
Update an instance by adding or changing an attribute.
The 'created_at' or 'updated_at' attributes cannot be modified.
If the given attribute name doesn't exist, a new one will be created.
Strings with spaces must have double quotes. (Lists with spaces do not)
Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = HBNBCommand.parse_args(argstr, max(4, len(argstr.split(' '))))
        cls = HBNBCommand.get_class(args[0])
        id = args[1]
        attr_name = args[2]
        attr_value = args[3]

        if cls is None:
            return
        if id == '':
            print("** instance id missing **")
            return
        if attr_name == '':
            print("** attribute name missing **")
            return
        if attr_value == '':
            print("** value missing **")
            return

        instance_found = False
        for instance in storage.all().values():
            if type(instance) is cls and instance.id == id:
                instance_found = True
                if (attr_name == "created_at" or attr_name == "updated_at" or
                    attr_name == "id"):
                    print("** cannot update that attribute **")
                    break
                    # Updating the dates crashes it, and updating id
                    # sometimes causes weird and dangerous behavior.
                    # Why would you need to update any of these anyway?

                # convert to an int, float, bool, list, or string with spaces,
                # if possible

                # allow of a list with spaces
                if attr_value[0] == '[':
                    arg_num = 3  # args[3] is attr_value's first word. This
                    # gets incremented for each word to help keep track of
                    # which arg from args we are at.
                    while len(args) - 1 > arg_num and args[arg_num][-1] != ']':
                        # Note that if there is a list within a list
                        # ([1, 2, [3, 4], 5]), then this arg will still
                        # be terminated at the first ']' char. However,
                        # it is unlikely this will ever be a problem outside
                        # of testing, and it is a somewhat complicated fix.

                        # increment to next word in the arg
                        arg_num += 1

                        # add a space and the next word
                        attr_value += ' ' + args[arg_num]

                    # if there is no closing bracket, treat it like the first
                    # arg is a string, terminated by the first space.
                    if attr_value[-1] != ']':
                        attr_value = args[3]

                # allow for a string with spaces
                if attr_value[0] == '"':
                    arg_num = 3  # args[3] is attr_value's first word. This
                    # gets incremented for each word to help keep track of
                    # which arg from args we are at.
                    while len(args) - 1 > arg_num and args[arg_num][-1] != '"':
                        # note that \" will simply end the string with a \
                        # rather than adding a "

                        # increment to next word in the arg
                        arg_num += 1

                        # add a space and the next word
                        attr_value += ' ' + args[arg_num]

                    # if there is no closing double-quote, treat it like the
                    # first arg is the string, terminated by the first space.
                    if attr_value[-1] != '"':
                        attr_value = args[3]
                try:
                    if attr_value.isdigit():
                        attr_value = int(attr_value)
                    elif (attr_value.replace('.', '', 1).isdigit() and
                          attr_value.count('.') == 1):
                        attr_value = float(attr_value)
                    elif attr_value == "True" or attr_value == "False":
                        attr_value = eval(attr_value)
                    elif attr_value[0] == '[' and attr_value[-1] == ']':
                        try:
                            attr_value = eval(attr_value)  # note:NEVER do this
                        except SyntaxError:
                            print("** incorrect syntax for a list **")
                            return
                        # in a serious project. Because it uses eval(),
                        # the user can execute code using this. This is VERY
                        # DANGEROUS! However, it works for this limited
                        # demonstration.

                    # remove the surrounding double quotes from a string
                    elif attr_value[0] == '"' and attr_value[-1] == ']':
                        attr_value = attr_value[1:-1]

                except ValueError:
                    pass  # Leave as string if conversion fails

                # update the model and save
                setattr(instance, attr_name, attr_value)
                instance.save()
                break

        if not instance_found:
            print("** no instance found **")

    @staticmethod
    def do_destroy(argstr):
        """
Deletes the specified instance.
className: name of the class of the instance to be deleted
id: the id of the instance to be deleted
Usage: destroy <class name> <id>
        """
        args = HBNBCommand.parse_args(argstr, 2)
        cls = HBNBCommand.get_class(args[0])
        id = args[1]

        if cls is None:
            return
        if id == '':
            print("** instance id missing **")
            return

        instance_found = False
        for content, instance in list(storage.all().items()):
            if type(instance) is cls and instance.id == id:
                del storage.all()[content]
                instance_found = True
                break

        if not instance_found:
            print("** no instance found **")
            return

    # ==================== data viewing commands ====================

    @staticmethod
    def do_show(argstr):
        """
Prints the string representation of an instance based on the class name and id
Usage: show <class name> <id>
        """
        args = HBNBCommand.parse_args(argstr, 2)
        cls = HBNBCommand.get_class(args[0])
        id = args[1]

        if cls is None:
            return
        if id == '':
            print("** instance id missing **")
            return

        instance_found = False
        for instance in storage.all().values():
            if isinstance(instance, cls) and instance.id == id:
                print(instance)
                instance_found = True
                break

        if not instance_found:
            print("** no instance found **")
            return

    @staticmethod
    def do_all(clsname):
        """
Prints the representations of all instances of the given class name
Usage: all <class name>
        """
        cls = HBNBCommand.get_class(clsname)
        if cls is None:
            return

        instances = []
        for instance in storage.all().values():
            if isinstance(instance, cls):
                instances.append(str(instance))

        print(instances)

    # ====================== misc fun commands ======================

    @staticmethod
    def do_rickroll(args):
        """Rickrolls you"""
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def do_selfdestruct(self, timer):
        """
Activates self-destruct mode, which starts a countdown from the specified
number, or 5 if not given. Exits the command line interpreter when
the countdown reaches 0.
Arguments: number (optional) - amount of seconds to count down from
Usage: selfdestruct <number>
        """
        t = 5
        if timer.isnumeric():
            t = int(timer)
        elif timer != '':
            print("Please specify a valid number, or leave blank.")
            return

        if sound:
            HBNBCommand.play_sound()

        set_color('red')
        set_color('bold')
        set_color('reverse')
        set_color('blinking')
        print("SELF DESTRUCT MODE INITIATED.\n")
        reset_color()
        while t > 0:
            if t <= 3:
                set_color('light red')
            else:
                reset_color()
            sleep(1)
            print(t)
            t -= 1
        sleep(1)
        reset_color()
        set_color('yellow')
        print("The console has been obliterated. Goodbye.")
        reset_color()
        return True

    # ======================= helper methods =======================

    @staticmethod
    def get_class(clsname):
        """
        Returns the class that matches the string given
        (only if it inherits BaseModel). It also handles printing the correct
        message if clsname is empty or the class was not found.
        :param clsname: string that should exactly match the class name
        :return: the class the matches the string, or none if either
        clsname is an empty string, or there is no match.
        """
        if clsname == "":
            print("** class name missing **")
            return None
        if clsname == 'BaseModel':
            return BaseModel
        elif clsname == 'User':
            return User
        elif clsname == 'Review':
            return Review
        elif clsname == 'Amenity':
            return Amenity
        elif clsname == 'Place':
            return Place
        elif clsname == 'State':
            return State
        elif clsname == 'City':
            return City
        else:
            print("** class doesn't exist **")
            return None

    @staticmethod
    def parse_args(argstr, num_args = 3):
        """
        parse args by converting a string of args (argstr) into individual args
        :param argstr: string of arguments, separated by spaces.
        :param num_args: number of args to parse. 3 by default if left empty
        :return: a list of args
        """
        args = argstr.split(' ')
        if len(args) < num_args:
            add_args = num_args - len(args)
            for i in range(add_args):
                args.append('')
        return args

    @staticmethod
    def play_sound():
        sep = os.sep
        player = vlc.Instance()
        media_list = player.media_list_new()
        media_player = player.media_list_player_new()
        alarm = player.media_new(os.getcwd() + f'{sep}res{sep}alarm.mp3')
        media_list.add_media(alarm)
        media_player.set_media_list(media_list)

        media_player.get_media_player().event_manager().event_attach(
            vlc.EventType.MediaPlayerEndReached,
            lambda event: HBNBCommand.play_sound()
        )

        media_player.play()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
