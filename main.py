from listener import Listener

def p():
    print("hello world")

def main():
    listener = Listener(p)
    listener.StartListening()


if __name__ == '__main__':
    main()