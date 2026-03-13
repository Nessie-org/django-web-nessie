import django
import manage
import sys

def main():
    sys.argv = [sys.argv[0], "runserver" ]
    manage.start()

if __name__ == "__main__":
    main()
