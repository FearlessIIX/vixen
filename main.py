from tokenizer import Tokenizer


def main():
    ofstream = open("vixen.txt", "r")

    try:
        source = ofstream.read()
    finally:
        ofstream.close()

    Tokenizer(source)


if __name__ == "__main__":
    main()
