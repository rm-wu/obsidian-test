# obsidian-test
A repo to test obsidian as a collaborative note taking tool for a research group.

---
<img src=".assets/interface.png" alt="Obsidian Interface" width="100%">

### How to use
Let's start by cloning the repo:
```shell
git clone https://github.com/rm-wu/obsidian-test.git
```
Open the folder as a vault in Obsidian.
`Obsidian > File > Open Vault > Open Folder as Vault > Select the folder you cloned the repo into. `


> [!IMPORTANT]
> I need to try if the files contained in `.obsidian/` are enough to download all the needed plugins and enable all the hotkeys.

### Obsidian setup
You need to install the following plugins:
- [obsidian-git](https://github.com/Vinzent03/obsidian-git)
- [dataview](https://github.com/blacksmithgu/obsidian-dataview)

First go to `Obsidian Preferences > Files and links` and select `Default location for new notes > In the folder specified below > notes` and `Default location for attachments > In the folder specified below > files`.

For enabling hotkeys, `Obsidian Preferences > Hotkeys > Plugins > Search for template > Templates: Insert Template > cmd+t`.

For template, go to `Obsidian Preferences > Templates > Template Folder location > templates`.

## How to install the repo
This are the commands to clone the repo into your personal vault and then setup the new git remote.
```bash
export VAULT_PATH=/path/to/your/vault
mkdir $VAULT_PATH
git clone https://github.com/rm-wu/obsidian-test.git $VAULT_PATH
cd $VAULT_PATH
rm -rf .git 
git init .
# ... proceed setting up your remote on GitHub (needed for collaborate on the vault)
```

## Folder organization
```
vault/
│
├── files/
├── meeting/
├── notes/
├── papers/
├── templates/
└── README.md
```

### Folder contents guide

- `files/`: Store miscellaneous files related to the research project, such as datasets, images, or other non-text resources.

- `meeting/`: Contains notes and minutes from research group meetings, organized by date or topic.

- `notes/`: Houses individual research notes, ideas, and observations from team members.

- `papers/`: Stores academic papers, articles, and literature reviews relevant to the research project.

- `templates/`: Holds reusable templates for various types of notes, such as meeting minutes, literature reviews, or experiment logs.

- `README.md`: This file, providing an overview of the repository and its structure.

## Setup Guide

To set up this collaborative note-taking vault using Obsidian and Git, follow these steps:

1. **Install Obsidian**: Download and install Obsidian from [https://obsidian.md/](https://obsidian.md/).

2. **Install Git**: If you don't have Git installed, download and install it from [https://git-scm.com/](https://git-scm.com/).

3. **Clone the repository**:
   - Open a terminal or command prompt.
   - Navigate to the directory where you want to store the vault.
   - Run the following command:
     ```
     git clone https://github.com/rm-wu/obsidian-test.git
     ```

4. **Open the vault in Obsidian**:
   - Launch Obsidian.
   - Click "Open folder as vault".
   - Navigate to the cloned `obsidian-test` directory and select it.

5. **Install Obsidian Git plugin**:
   - In Obsidian, go to Settings (gear icon) > Community plugins.
   - Turn off "Safe mode" if it's enabled.
   - Click "Browse" and search for "Obsidian Git". [Obsidian-git plugin](obsidian://show-plugin?id=obsidian-git)

   - Click "Install" next to the Obsidian Git plugin.
   - After installation, enable the plugin.

6. **(OPTIONAL) Configure Obsidian Git plugin**:
   - Go to Settings > Community plugins > Obsidian Git > Options.
   - Set up your preferred auto-backup frequency and commit message format.

7. **Start collaborating**:
   - Create or edit notes in the appropriate folders.
   - The Obsidian Git plugin will automatically commit and push changes based on your settings.
   - To manually sync changes:
     - Use the command palette (Ctrl/Cmd + P) and search for "Obsidian Git: Pull" to get the latest changes.
     - Use "Obsidian Git: Commit all changes" followed by "Obsidian Git: Push" to send your changes to the repository.

Remember to communicate with your team about Git best practices, such as pulling before making changes and resolving conflicts when they arise.

By following these steps, you and your research group can start using this Obsidian vault for collaborative note-taking, with changes synchronized through Git.


## Note taking with Obsidian
<img src=".assets/obsidian-vis.png" alt="Obsidian Interface" width="90%">

File preview support:
<img src=".assets/file-integration.png" alt="File Preview" width="90%">

## Graph View
<img src=".assets/graph-view.png" alt="Graph View" width="90%">

## Meeting Notes
<img src=".assets/meeting.png" alt="Graph View" width="90%">
