import os

class Chimame:
    def __init__(self):
        self.characher = {
            "chino": {},
            "maya": {},
            "megu": {}
        }
        self.share = {}
        self.active = "chino"
    
    def accept_command(self) -> str:
        command: list[str] = input(f'{self.active}> ').split(" ")

        index = 0
        for item in command:
            if item.startswith("¥"):
                try:
                    command[index] = str(self.characher[self.active][item[1:].strip()])
                except:
                    pass
            elif item.startswith("$"):
                try:
                    command[index] = str(self.share[item[1:].strip()])
                except:
                    pass
            index += 1

        if command[0] == "pwd":
            print(os.getcwd())
        elif command[0] == "cd":
            try:
                os.chdir(self.eval(" ".join(command[1:])))
            except Exception as e:
                print(f'Error: {e}')
        elif command[0] == "char":
            char = self.eval(" ".join(command[1:]))
            if char in self.characher.keys():
                self.active = char
            else:
                print("Error: undefined characher")
        elif command[0] == "let":
            splited = " ".join(command[1:]).split("=")
            name, value = splited[0], "=".join(splited[1:])
            self.characher[self.active][name.strip()] = self.eval(value)
            print(self.characher)
        elif command[0] == "share":
            splited = " ".join(command[1:]).split("=")
            name, value = splited[0], "=".join(splited[1:])
            self.share[name.strip()] = self.eval(value)
            print({k:v for k, v in self.share.items() if k not in ["__builtins__"]})
        else:
            print(self.eval(" ".join(command)))

    def eval(self, command: str):
        try:
            return eval(command, self.share, self.characher[self.active])
        except Exception as e:
            print(f"Error: {e}")

print("Chimame Squad Shell")
chimame = Chimame()
while True:
    chimame.accept_command()