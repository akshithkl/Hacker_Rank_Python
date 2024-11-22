if __name__ == '__main__':
    N = int(input())
    
    l = []
    
    for i in range(N):
        commands = input().split()
        command = commands[0]
        
        if command == "insert":
            l.insert(int(commands[1]), int(commands[2]))
        elif command == "remove":
            l.remove(int(commands[1]))
        elif command == "append":
            l.append(int(commands[1]))
        elif command == "print":
            print(l)
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()
