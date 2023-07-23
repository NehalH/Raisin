$currentDirectory = Get-Location
$absolutePath = $currentDirectory.Path

# Define the raisin function
function raisin {
    param(
        [string]$arg1
    )

    & "python" "$absolutePath+main.py" $arg1
}

# Set up the function in the user's PowerShell profile
$profilePath = $PROFILE
$functionContent = (Get-Content -Path $profilePath -Raw) + "`n" + (Get-Command raisin | Export-ModuleMember -PassThru)
$functionContent | Set-Content -Path $profilePath
