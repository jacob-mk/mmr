class Player:
    def __init__(self,name,mmr):
        self.name = name
        self.mmr = mmr
    #String representation of an Account object - "name: $balance"
    def __repr__(self):
        return self.name + ": " + str(self.mmr)

    def __lt__(self, other):
        if self.mmr < other.mmr:
            return True
        else:
            return False

def get_list():
    mmr_list = []
    with open("mmr.csv","r") as fl:
        for line in fl:
            split_line = line.split(",")
            mmr_list += [Player(split_line[0],int(split_line[1].replace("\n","")))]
    return mmr_list

def get_player(name,ls):
    for i in ls:
        if i.name == name:
            return i
    return None

def get_mmr(name,ls):
    player = get_player(name, ls)
    if player == None:
        return None
    return player.mmr

def update_mmr(name,new_mmr,ls):
    player = get_player(name, ls)
    if player == None:
        return -1
    player.mmr = int(new_mmr)
    return 0

def main():
    mmr_list = get_list()
    done = False

    print("MMR updater")
    print("'get [name]' to get player's mmr")
    print("'update [name] [new mmr]' to set player's mmr")
    print("'push' to push MMR updates to file")
    print("'end' to leave program")
    print()

    while not done:
        cmd = input("> ")
        if cmd[:3] == "get":
            this_mmr = get_mmr(cmd[4:],mmr_list)
            if this_mmr == None:
                print("Player not found!")
            else:
                out = cmd[4:]+"'s MMR is "+str(this_mmr)
                print(out)

        elif cmd[:6] == "update":
            split_cmd = cmd.split(" ")
            res = update_mmr(split_cmd[1], split_cmd[2].replace("\n",""), mmr_list)
            if res == -1:
                print("MMR Update failed!")
            else:
                out = split_cmd[1] + "'s MMR has been updated to " + split_cmd[2].replace("\n","")
                print(out)

        elif cmd == "push":
            mmr_list.sort(reverse=True)
            with open("mmr.csv","w") as fl:
                for player in mmr_list:
                    fl.write(player.name + "," + str(player.mmr) + "\n")

        elif cmd == "end":
            return



if __name__ == "__main__":
    main()
