from time import sleep

def get_input()->list[int]:
    print("insert your time for countdown (h:m:s)")
    args = input().split(":")
    int_args = []
    if len(args) == 3:
        for elem in args:
            if not elem.isnumeric():
                print("Wrong input")
                exit(1)
            if int(elem) >= 0 :
                int_args.append(int(elem))
        return int_args
    print("Wrong input")
    exit(1)

def main():
    args = get_input()
    if args[2] < 0 or args[2] >= 60 or args[1] < 0 or args[1] >= 60:
        print("Wrong input")
        exit(1)
    sum = args[0] * 3600 + args[1] * 60 + args[2]
    while sum >= 0:
        print(f"{sum // 3600}:{(sum // 60 % 60)}:{sum % 60}")
        sleep(1)
        sum -= 1
   
if __name__ == "__main__":
    main()