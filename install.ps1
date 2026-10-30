# Install the prompt-coach skill on Windows.
#
#   irm https://raw.githubusercontent.com/justinjd00/prompt-coach/main/install.ps1 | iex
#
# Installs to %USERPROFILE%\.claude\skills (Claude Code, also read by Cursor/Copilot/opencode)
# and %USERPROFILE%\.agents\skills (Codex, Cursor, Gemini CLI, GitHub Copilot, opencode).
# Set $env:PROMPT_COACH_REF to install a branch or tag other than main.

$ErrorActionPreference = 'Stop'
$repo = 'justinjd00/prompt-coach'
$ref = if ($env:PROMPT_COACH_REF) { $env:PROMPT_COACH_REF } else { 'main' }

$tmp = Join-Path ([IO.Path]::GetTempPath()) ("prompt-coach-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
    $zip = Join-Path $tmp 'src.zip'
    Write-Host "Downloading $repo@$ref ..."
    Invoke-WebRequest -Uri "https://codeload.github.com/$repo/zip/$ref" -OutFile $zip -UseBasicParsing
    Expand-Archive -Path $zip -DestinationPath $tmp
    $src = Get-ChildItem -Path $tmp -Directory -Recurse -Filter 'prompt-coach' |
        Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } | Select-Object -First 1
    if (-not $src) { throw 'skill not found in download' }

    foreach ($base in @("$env:USERPROFILE\.claude\skills", "$env:USERPROFILE\.agents\skills")) {
        New-Item -ItemType Directory -Force -Path $base | Out-Null
        $dest = Join-Path $base 'prompt-coach'
        if (Test-Path $dest) { Remove-Item -Recurse -Force $dest }
        Copy-Item -Recurse -Path $src.FullName -Destination $dest
        Write-Host "Installed to $dest"
    }
    Write-Host 'Done. Start a new session and say: /prompt-coach  (or just ask to build out a prompt).'
}
finally {
    Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
