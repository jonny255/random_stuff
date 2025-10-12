# README.md

## TODO

### Automating compression

- [ ]   copy over the 7z compression script
- [ ]   use a boolean to compress folders incrementally from deepest defined level to the surface
- [ ]   Maybe create a temp log of md5 hashes all of 7z files?

### Deduplication Efforts

- [ ]   Start with docker container/image
- [ ]   install sqllite in Dockerfile
- [ ]   Use the find script used for compression to list all directories, but this time .7z files
- [ ]   Store file directories in colume 2 of sql table; `filename.7z` will be stored in colume 3
- [ ]   Run a script that would run independent hash on all files in the list (colume 4).
- [ ]   Use a `if {[hash] - [hash] == 0}` to cycle through files (colume 5)

Or maybe I could keep it even simpler and use json/csv to store all the information.

1. And instead of using `[hash] - [hash] == 0`, if everything is stored via sqllite, the file's hash will also serve as the primary key and the sql server will already have that duplicate detection. Wait, that won't work because it won't accept the hash; yeah just put the hash & calculation on seperate columnes and run the scan that way.

2. One file will need to be the control/reference; how to determine which one.

3. To automate step 3, find ways to categorize everything so that it could be sorted at this staged. For example, make note of all of the similar directories or the frequent ones, then allow the user to decide which directory will be the control/reference. That way as I'm deleting files, I'm not deleting a dup from dirA, then another dup file from dirB, then last I have to recombine/merge the two directories together.
4.  

=======================================================================

This plan captures our work in May 2025. This is a 5-week iteration. We will ship in early June.

Caution

On May 21 we decided to extend the iteration by one week.

Endgame
June 2, 2025: Endgame begins
June 6, 2025: Endgame done
The endgame details for this iteration are tracked here.

Plan Items
Below is a summary of the top level plan items.

Legend of annotations:

Mark Description
🏃  work in progress                        \
✋  blocked task                           \
💪  stretch goal for this iteration         \
🔴  missing issue reference                 \
🔵  more investigation required to remove uncertainty   \
⚫  under discussion within the team    \
⬛   a large work item, larger than one iteration   \
Accessibility

Accessibility issues, see query @meganrogge team
UX

🏃 Remove all hard-coded styles with variables vscode#248725 @mrleemurray
Workbench

💪 Support JSON file as a policy backend on Linux vscode#148945 @joshspicer

💪 Explore anchored quick widget for mouse interactions to attach context vscode#238095 @TylerLeonhardt

Support custom menus with native titlebar vscode#229053 @benibenj

🏃 Suggest to user to move app to /Applications on startup vscode#213909 @deepak1556
Code Editor

Enable EditContext by default on Stable vscode#248893 @aiday-mar

🏃 Add support for multiple fonts in the editor vscode#237346 @aiday-mar

🏃 Investigation: Use tree-sitter for grammar colorization vscode#210475 @alexr00 @hediet
Notebook Editor / Jupyter Notebooks

Auto reveal on cell execution/editing vscode#248546 @Yoyokrazy @amunger

💪 Explore rendering outputs in separate pane/view/editor vscode#143244 @Yoyokrazy @amunger
Languages
LSP

Adopt to new vscode log output channel API vscode#1116 @dbaeumer
Python

Add builtin support for following python env managers vscode-python-environments#79 @karthiknadig

Pyenv

Poetry

💪 Get python for users with no python installed vscode-python#24963 @karthiknadig

"New project" for python work @eleanorjboyd

use built-in templates, uv, poetry, conda to create new project templates for python package, and pep 723 style script vscode-python-environments#390 @eleanorjboyd

Fix outstanding bugs in existing "new project" flow and multiroot scenarios vscode-python-environments#399 @eleanorjboyd

connect "New Project" to /new for copilot vscode-python-environments#286 @eleanorjboyd @bhavyaus

Python Environment Tools (pet) improvments (e.g., conda) @DonJayamanne vscode-python-environment-tools#220
Source Control

Support OOTB git commit message generation action vscode#248697 @lszomoru

Support list of files in SCM graph vscode#248696 @lszomoru

Support commits as context vscode#248699 @lszomoru

Git: Support repository discovery API vscode#248698 @lszomoru
Terminal

Terminal REPL completions using LSP vscode#241167 @anthonykim1
Tasks

Add a task instance limit policy to task runOptions vscode#90125 @meganrogge

Improve problem matcher error debugging with Copilot vscode#192811 @meganrogge

Add setting to gracefully kill tasks vscode#206607 @meganrogge
API

API proposals: query @jrieken @mjbvz

API finalization: query @jrieken @mjbvz
Extensions

Warn about installed extensions that are no longer available in Marketplace vscode#181248 @joshspicer

💪 Add support for bulk actions in extensions list view vscode#48616 @joshspicer

💪 Make Workspace Extensions more intuitive to find and activate vscode#216433 @joshspicer

Support local secret scanning vscode-vsce#1136 @benibenj

Prevent .env files from being bundled in the VSIX vscode-vsce#1135 @benibenj
Extension Contributions

Investigate various module load failures with ESLint and flat configs vscode-eslint#2015 vscode-eslint#1994 vscode-eslint#2006 vscode-eslint#1992 @dbaeumer

GHPRI: URL handler for PR and Issues, to open them within VS Code vscode-pull-request-github#6869 @alexr00

GHPRI: Support images from private repos in comments vscode-pull-request-github#6175 @alexr00
AI
Architecture

🏃 Open-source AI functionality provided by the Copilot Chat extension vscode#249031 @kieferrm @alexdima

🏃 Support Copilot Chat in web vscode#245860 @bpasero
MCP

Rework MCP tool prefixing behavior vscode#249281 @connor4312

Support MCP prompts vscode#244173 @connor4312

Explore support MCP resources vscode#244159 @connor4312

Explore support for MCP sampling vscode#244162 @connor4312

🏃 MCP: Better discovery/registry and one-click installation flow vscode#245717 @sandy081

Explore MCP Server Authentication according to MCP OAuth Spec vscode#247759 @TylerLeonhardt
Prompt and Instruction Files

Support definition of modes using prompt files vscode-copilot-release#9452 @aeschli @legomushroom @digitarald

Improve frontmatter support in prompt files vscode#249271 @aeschli @legomushroom @digitarald

Allow to reuse the chat tool picker from within frontmatter vscode#249272 @jrieken @aeschli @legomushroom @digitarald
Chat

Make it easier to distinguish & trigger chat completion types vscode#249249 @jrieken

Support the concept tool sets in the UI and API vscode#247860 @jrieken @roblourens

Chat editing UX should adjust to the editing strategy vscode#249083 @jrieken

🏃 Improve checkpoint experience in chat vscode#249229 @jo-oikawa @justschen @roblourens

Support a /list command to list all registered tools vscode#249237 @roblourens

🏃 Improve recovering from response errors: auto retry, let user click to continue vscode-copilot-release#9496 @roblourens @justschen

Improve ease of keyboard use for attachment management vscode#249304 @justschen @roblourens

🏃 Support Katex syntax rendering in Chat vscode-copilot-release#978 @mjbvz

🏃 Support Mermaid diagram rendering in Chat vscode-copilot-release#7440 @mjbvz
NES / Completions

🏃 Improve next edit suggestions @alexdima team

Make language-specific context available to Copilot inline completions @dbaeumer
Engineering

💪 🏃 Support building the monaco-editor AMD variant from new sources vscode#234114 @hediet @alexdima

Investigation: Explore a more stable Windows update story vscode#249239 @deepak1556
Electron

Electron 35 update vscode#245420 @deepak1556
Documentation

Add guidance to API docs about running MCP server in extension vscode-docs#8216 @ntrogh

Include AI guidance in terminal docs vscode-docs#8275 @ntrogh

Make chat context more visible and discoverable in docs vscode-docs#8362 @ntrogh
Deferred

Improve VS Code Figma design resources vscode#249227 @kkbrooks

Support fetching history as tool vscode-copilot-release#9471 @lszomoru

Support mcp servers as a first class resource vscode#248401 @sandy081

🏃 Update Conpty in VS Code vscode#224488 @Tyriar @deepak1556

🏃 Explore GPU rendering of the code editor vscode#221145 @Tyriar @hediet

💪 Finalize Related code vscode#126932 @connor4312

VSCode freezing when adding folder to workspace while working on remote Linux machine vscode-remote-release#10168 @joshspicer

💪 Resolve unique connection issues vscode-remote-release#10412, vscode-remote-release#6319, vscode-remote-release#6600 @joshspicer
