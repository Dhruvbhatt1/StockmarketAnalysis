# StockmarketAnalysis

### Built With

* [![Azure][Azure]][Azure-url]
* [![Databricks][Databricks]][Databricks-url]
* [![Delta Lake][DeltaLake]][DeltaLake-url]
* [![Azure Data Factory][ADF]][ADF-url]
* [![Power BI][PowerBI]][PowerBI-url]
* [![Terraform][Terraform]][Terraform-url]
* [![GitHub Actions][GitHubActions]][GitHubActions-url]
* [![Azure Key Vault][KeyVault]][KeyVault-url]

[Azure]: https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white
[Azure-url]: https://azure.microsoft.com/

[Databricks]: https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white
[Databricks-url]: https://databricks.com/

[DeltaLake]: https://img.shields.io/badge/Delta%20Lake-0A2E5C?style=for-the-badge
[DeltaLake-url]: https://delta.io/

[ADF]: https://img.shields.io/badge/Azure%20Data%20Factory-0062AD?style=for-the-badge&logo=microsoftazure&logoColor=white
[ADF-url]: https://azure.microsoft.com/services/data-factory/

[PowerBI]: https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=black
[PowerBI-url]: https://powerbi.microsoft.com/

[Terraform]: https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white
[Terraform-url]: https://www.terraform.io/

[GitHubActions]: https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white
[GitHubActions-url]: https://github.com/features/actions

[KeyVault]: https://img.shields.io/badge/Azure%20Key%20Vault-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white
[KeyVault-url]: https://azure.microsoft.com/services/key-vault/


## High-Level Architecture


## Data Ingestion & Streaming
- **Source**: Real-time stock market tick data from an API.
- **Azure Event Hubs**: Ingest and stream JSON-formatted market data events in near real-time.

## Storage & Lakehouse Architecture
- **Azure Data Lake Storage Gen2 (ADLS)**: A central, cost-effective, and scalable data lake for both raw and structured data.
- **Delta Lake (on Databricks)**: Provides transactional capabilities (ACID compliance), schema evolution, and time-travel queries, enabling a robust Lakehouse architecture.

## ETL & Data Transformation
- **Databricks Structured Streaming**: Continuously process and transform streaming data from Event Hubs.
- **Delta Live Tables**: Implement data quality checks, schema validation, and maintain clean, reliable data pipelines.

## Analytics & Visualization
- **Aggregations & Metrics**: Compute moving averages, daily trading volumes, and volatility measures within Databricks.
- **BI Integration**: Connect curated Delta tables to visualization tools like Power BI or Azure Synapse for interactive dashboards and real-time insights.

## Orchestration & CI/CD
- **Azure Data Factory or Databricks Workflows**: Schedule and orchestrate both batch and streaming ETL processes.
- **GitHub Actions**: Implement CI/CD pipelines for:
  - Infrastructure provisioning with Terraform.
  - Automated deployment and testing of Databricks jobs and notebooks.
  - Continuous integration to ensure code quality and reliability.

## Security & Governance
- **Azure RBAC**: Apply role-based access control to secure resources and control access at a granular level.
- **Databricks Secret Scopes & Azure Key Vault**: Securely store and manage sensitive credentials (API keys, tokens) and securely access them within Databricks notebooks and jobs.

