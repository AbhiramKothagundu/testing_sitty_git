import os
import subprocess
import random
import string
import time

# Directory to initialize the git repository (change if needed)
repo_dir = os.getcwd()  # Assuming you are running this from the repo directory

# Perfect web app structure directory
set1_dir = os.path.join(repo_dir, "set1")

# Function to run git commands
def run_git_command(command, cwd=None):
    print(f"Running command: {command}")
    result = subprocess.run(command, cwd=cwd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.strip()

# Function to create a random string for dirty commits
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to create a dirty commit with random text
def create_dirty_commit():
    # Create a random file or modify an existing one
    file_name = random.choice(["file1.txt", "file2.txt", "file3.txt", "README.md"])
    with open(file_name, "a") as f:
        f.write(f"\n{random_string()}")  # Adding random string to simulate dirty commit
    
    # Stage and commit the changes
    run_git_command("git add .", repo_dir)
    commit_message = f"Dirty commit with random changes: {random_string()}"
    run_git_command(f'git commit -m "{commit_message}"', repo_dir)

# Function to create a clean commit with a perfect web app structure
def create_perfect_commit():
    if not os.path.exists(set1_dir):
        os.makedirs(set1_dir)

    # Create the clean web app structure in /set1 folder
    files = ["index.html", "style.css", "app.js"]
    for file_name in files:
        with open(os.path.join(set1_dir, file_name), "w") as f:
            if file_name == "index.html":
                f.write("<!DOCTYPE html><html><head><title>Perfect Web App</title></head><body><h1>Hello World</h1></body></html>")
            elif file_name == "style.css":
                f.write("body { font-family: Arial, sans-serif; background-color: #f4f4f4; }")
            elif file_name == "app.js":
                f.write("console.log('Hello World');")

    # Stage and commit the clean structure
    run_git_command("git add .", repo_dir)
    run_git_command('git commit -m "Add perfect web app structure in set1"', repo_dir)

# Main function to simulate dirty commits with random clean commits
def main():
    num_commits = random.randint(5, 15)  # Number of commits before the perfect commit
    for _ in range(num_commits):
        if random.random() < 0.2:  # 20% chance of a clean commit
            print("Creating a clean commit with perfect web app structure...")
            create_perfect_commit()
        else:
            print("Creating a dirty commit...")
            create_dirty_commit()
        
        # Simulate time delay between commits
        time.sleep(random.randint(1, 3))  # Sleep for 1 to 3 seconds before next commit
    
    print("Finished generating commits.")

if __name__ == "__main__":
    main()
