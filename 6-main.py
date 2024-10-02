#!/usr/bin/python3
from models import *
from models import user

if __name__ == '__main__':
    instance_found = False
    for content, instance in list(storage.all().items()):
        if type(instance) is user.User and instance.id == 'never-gonna-give-you-up-r1cl<r011':
            print(instance.email)
            instance_found = True
            break
