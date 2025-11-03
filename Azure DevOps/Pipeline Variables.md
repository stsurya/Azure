| Variable                            | Typical value (on your VM)         | Description                                          |
| ----------------------------------- | ---------------------------------- | ---------------------------------------------------- |
| `$(Agent.RootDirectory)`            | `C:\azagent\A2`                    | Root folder where the agent is installed             |
| `$(Pipeline.Workspace)`             | `C:\azagent\A2\_work\2`            | Folder for this pipeline’s run                       |
| `$(System.DefaultWorkingDirectory)` | `C:\azagent\A2\_work\2\s`          | Folder where the **self (main)** repo is checked out |
| `$(Build.SourcesDirectory)`         | Same as above (`…\s`)              | Alias for the default repo’s source folder           |
| `$(Pipeline.Workspace)/Deployment`  | `C:\azagent\A2\_work\2\Deployment` | Folder for your **external** Deployment repo         |
| `$(Build.ArtifactStagingDirectory)` | `C:\azagent\A2\_work\2\a`          | Temporary output folder for build artifacts          |
| `$(Build.BinariesDirectory)`        | `C:\azagent\A2\_work\2\b`          | Folder used for compiled output/binaries             |
