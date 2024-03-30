from hb_parser import Parser

def main():
    parser = Parser("")
    while(True):
        text = input(">")
        parser.reset(text)


if __name__ == "__main__":
    main()
