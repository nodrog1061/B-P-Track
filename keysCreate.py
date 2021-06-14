import secrets
import os
import pickle
import argparse

filename = "apiKeys.pickle"

parser = argparse.ArgumentParser(description="Used for the handling of api keys for pTrack for RDUTC", epilog="© Lead Dev Lewis Taylor(Scott Marshall) Armed Excellence Software 2021")

parser.add_argument("-g","--generate" , type=int, help="Generate's a set of api keys will create a pickle file for them if none exites already otherwise adds them to exciting file * Define number of keys that need creating* Int")

parser.add_argument("-r","--remove", type=str, help="Remove a api key from the system must be as writen Str")

parser.add_argument("-c","--check", type=str, help="Check if a api key is in the pickle file")

parser.add_argument("-d","--display", action="store_true", help="Display all api keys in command line")

parser.add_argument("-du","--dump", type=str , help="Dump all api keys to a txt file *define file location and file name e.g 'C:\Documents\api_keys.txt' * str")

args = parser.parse_args()

def keyCreate(number):
    count = 1
    output_key = []
    while count <= number:
        generated_key = secrets.token_urlsafe(20)
        output_key.append(generated_key)
        count += 1
    return output_key

if args.check is not None:
    if len(str(args.check)) == 27:
        if os.path.isfile(filename):
            with open(filename, "rb") as f:
                try:
                    fromFile = pickle.load(f)

                    if args.check in fromFile:
                        print(True)
                    else:
                        print(False)

                except Exception: # so many things could go wrong, can't be more specific.
                    print("a error has occoured")
                    pass
        else:
            print("a error has occoured probably due to there being no api keys list you need to parse -g to do this")
    else:
        print("Api Key is incorect length")

if args.generate is None and args.remove is None and args.display is False and args.dump is None and args.check is None:
    print("You need to parse an argument use -h for more info")
    exit()


if args.generate is not None:

    if os.path.isfile(filename):
        with open(filename, "rb") as f:
            try:
                fromFile = pickle.load(f)

                if args.display:
                    print("New keys are as folows")
                if args.dump is not None:
                    print ("New api keys added they have been put into the definded txt file")
                    with open(args.dump, "a") as b:
                        b.write("The folowing is for reference only it will NOT effect the code if changed")

                for i in keyCreate(args.generate):
                    if args.display:
                        print(i)

                    if args.dump is not None:
                        with open(args.dump, "a") as b:
                            b.write(f"\n {i}")
                    
                    fromFile.append(i)

                with open(filename, "wb") as b:
                    pickle.dump(fromFile, b)
            except Exception: # so many things could go wrong, can't be more specific.
                print("a error has occoured")
                pass 

    else:
        with open(filename, "wb") as f:
            toFileC = keyCreate(args.generate)

            if args.dump is None:
                print ("New file was created for api keys the flolowing keys are valid:")
                for i in toFileC:
                        print(i)
                print("If you wish for these in text form do -d FILENAME")
            elif args.dump is not None:
                print ("New file was created for api keys it has been put into the definded txt file")

                with open(args.dump, "a") as b:
                    b.write("The folowing is for reference only it will NOT effect the code if changed")
                    b.write(f"\n {toFileC}")
            pickle.dump(toFileC, f)

