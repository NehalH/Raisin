$installScript = @"
$currentDirectory = Get-Location
$absolutePath = $currentDirectory.Path

# Define the raisin function
function raisin {
    param(
        [string]$arg1
    )

    & "python" "$absolutePath\main.py" $arg1
}

# Set up the function in the user's PowerShell profile
$profilePath = $PROFILE
$functionContent = (Get-Content -Path $profilePath -Raw) + "`n" + (Get-Command raisin | Export-ModuleMember -PassThru)
$functionContent | Set-Content -Path $profilePath
"@

$installScriptPath = Join-Path -Path $PSScriptRoot -ChildPath "Install-RaisinFunction.ps1"
$installScript | Set-Content -Path $installScriptPath

$executableScript = @"
PowerShell.exe -ExecutionPolicy Bypass -NoProfile -File "$installScriptPath"
"@

$executableScriptPath = Join-Path -Path $PSScriptRoot -ChildPath "RaisinSetup.ps1"
$executableScript | Set-Content -Path $executableScriptPath

# Compile the script to an executable using ps2exe
ps2exe $executableScriptPath -output RaisinSetup.exe
Remove-Item $installScriptPath
Remove-Item $executableScriptPath
"@

$scriptContent = @"
$installScript

$executableScript
"@

$scriptContent | Set-Content -Path "create-setup.ps1"

# Compile the setup script to an executable using ps2exe
ps2exe "create-setup.ps1" -output CreateRaisinSetup.exe

# Clean up temporary script
Remove-Item "create-setup.ps1"
"@


.\create-setup.ps1
