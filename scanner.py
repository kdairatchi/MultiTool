import subprocess
import sys
import platform
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = """
    __  __       _ _   _ _____           _             _         
    |  \/  |     (_) | | |_   _|         | |           | |        
    | \  / | __ _ _| |_| |_| |_ __ _  ___| | _____ _ __| |_ _   _ 
    | |\/| |/ _` | | __| __|  _/ _` |/ __| |/ / _ \ '__| __| | | |
    | |  | | (_| | | |_| |_| || (_| | (__|   <  __/ |  | |_| |_| |
    |_|  |_|\__,_|_|\__|\__\_| \__,_|\___|_|\_\___|_|   \__|\__, |
                                                            __/ |
                                                           |___/ 
                     by kdairatchi
    """
    print(Fore.CYAN + Style.BRIGHT + banner)

def run_naabu(target):
    try:
        # Run naabu command
        command = ['naabu', '-host', target]
        result = subprocess.run(command, capture_output=True, text=True)
        print(Fore.CYAN + "Naabu Output:")
        print(Fore.GREEN + result.stdout)
    except Exception as e:
        print(Fore.RED + f"An error occurred while running naabu: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Usage: python multi_tool.py <target>")
        sys.exit(1)

    target = sys.argv[1]
    print(Fore.MAGENTA + Style.BRIGHT + f"Scanning target: {target}")

    # Run naabu
    run_naabu(target)

if __name__ == '__main__':
    print_banner()
    main()