# chatgpt-terminal-helper
This video show how to create a ChatGPT Helper for terminal using python,  and Also, its shows how to add any Python script to executable files. With this, we can call our Terminal Helper at any location in our Terminal.

![Thumbnail-ChatGPT](https://user-images.githubusercontent.com/115108831/211735034-dfaec578-8d65-4469-b433-072b66c1afb2.jpg)

## Installation 
```
https://github.com/Toronto-Dev/chatgpt-terminal-helper.git
```

Please Add Generate API key on [Openai.com](https://www.openai.com) and replace it with "Your key goes here" in the script.

## Python Modules Installation
```
pip3 install openai colorama
```

**YouTube Video Link:** [ChatGPT Video](https://youtu.be/QVYFLRzgPJY)


## How to Add script to Executable Files
Create s folder in home directory and move the script in it;for instance, **/Users/JohnDoe/scripts/helper.py**

Add the below in .zshrc or .bashrc
```
export PATH="$PATH:dir/scripts"

```
