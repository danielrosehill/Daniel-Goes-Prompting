# Prompt

Please teach me how to create a launcher to this program on my fedora linux computer
I'd like a desktop entry but also for it to be in my menu
And tell me how i could create a hotkey to launch it too:

/home/daniel/Git/vault-prompt-runner/v8/program.py



# Output

Certainly! I'll guide you through creating a desktop entry for your program, adding it to your menu, and setting up a hotkey to launch it. Here's how to do it on your Fedora Linux computer:

## Creating a Desktop Entry

1. First, create a new .desktop file in your local applications directory:

```bash
mkdir -p ~/.local/share/applications
nano ~/.local/share/applications/vault-prompt-runner.desktop
```

2. In the nano editor, add the following content:

```
[Desktop Entry]
Name=Vault Prompt Runner
Comment=Run the Vault Prompt Runner program
Exec=/usr/bin/python3 /home/daniel/Git/vault-prompt-runner/v8/program.py
Icon=terminal
Terminal=false
Type=Application
Categories=Utility;Development;
```

3. Save the file and exit nano (Ctrl+X, then Y, then Enter).

4. Make the .desktop file executable:

```bash
chmod +x ~/.local/share/applications/vault-prompt-runner.desktop
```

5. Update the desktop database:

```bash
update-desktop-database ~/.local/share/applications
```

Now, your program should appear in the application menu under the "Utility" or "Development" categories[1][3].

## Setting Up a Hotkey

To create a hotkey for launching your program:

1. Open the Settings menu and select "Keyboard" from the list.

2. Scroll down to the "Keyboard Shortcuts" section and click "View and Customize Shortcuts".

3. Click on the "Custom Shortcuts" menu item, then click "Add Shortcut".

4. In the "Add Custom Shortcut" window, enter the following details:
   - Name: Vault Prompt Runner
   - Command: /usr/bin/python3 /home/daniel/Git/vault-prompt-runner/v8/program.py

5. Click "Set Shortcut" to open the "Enter the new shortcut" dialog.

6. Type your desired keyboard shortcut, for example, Ctrl+Alt+V.

7. Click "Add"[2].

Your shortcut is now ready to use. You can launch your program using the keyboard shortcut you just set.

## Additional Tips

- If you want the program to run in a terminal, change the `Terminal=false` line to `Terminal=true` in the .desktop file.

- You can customize the icon by replacing `Icon=terminal` with the path to a custom icon file.

- If you need to make any changes to the .desktop file in the future, simply edit it using a text editor and update the desktop database again.

- To make the launcher available system-wide (for all users), you would need to place the .desktop file in `/usr/share/applications/` instead, but this requires root privileges[4].

By following these steps, you've created a launcher for your program that appears in the application menu and can be launched using a custom hotkey. Enjoy using your Vault Prompt Runner with ease!

