; Script generated by the Inno Script Studio Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "myEditor"
#define MyAppVersion "1.5"
#define MyAppPublisher "USN"
#define MyAppURL "http://www.usn.no"
#define MyAppExeName "FileEditAndSave.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{470F6D8E-85BB-452C-9EC9-CB1D999228E3}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=release
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\dist\FileEditAndSave\FileEditAndSave.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\FileEditAndSave\_internal\*"; DestDir: "{app}\_internal\"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
Source: "..\dist\FileEditAndSave\_internal\folder_open_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\dist\FileEditAndSave\_internal\save_24dp_5F6368_FILL0_wght400_GRAD0_opsz24.svg"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[PreCompile]
Name: "PreCompileBuild.bat"; Flags: redirectoutput abortonerror cmdprompt
