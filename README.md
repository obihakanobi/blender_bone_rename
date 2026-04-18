# Auto Bone Renamer (Blender Add-on)

A simple Blender add-on to rename armature bones by:

* Converting "left"/"right" → `_L` / `_R`
* Removing custom user-defined text from bone names
* Works on all bones in the active armature

## Installation

1. Download the `blender_bone_rename_addon.py` file
2. Open Blender
3. Go to **Edit → Preferences → Add-ons**
4. Click **Install**
5. Select the `.py` file and enable the add-on

## Usage

1. Select an armature
2. Open the **3D View → Sidebar (N) → Tool tab**
3. Use:

   * **Auto Rename L/R** for automatic suffix renaming
   * **Text to Remove + Remove Text** to clean custom strings

