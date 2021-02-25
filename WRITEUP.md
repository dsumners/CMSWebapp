# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

APP SERVICE:
Since this is a small, light application the costs, scalability, and availability for the CMS appplication deployed through an App Service is an effective solution.  The CMSD application doesn't require large compute capability. GitHub workflows on the Azure portal ensure deployments/syncs are easily accomplished.

VM:
The costs, scalability and availability through a VM are also reasonable. Some developers may wish to have more control or custimazation abilities

My Choice:
I chose the App Service because the CMS app is a simple light application requiring little computing power.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

APP Service:
Chages in features and usage requiring more computing power could dictate a change to a VM solution.

VM:
With increased usage this solution could become more expensive requiing additional hardware or computing resources.
