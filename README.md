# StockmarketAnalysis

High-Level Architecture
1. Data Ingestion & Streaming:
   *Source: Real-time stock market tick data from an API (e.g., Polygon.io)
   *Azure Event Hubs: Stream incoming JSON-formatted market data events.
2. Storage & Lakehouse Architecture:
   *Azure Data Lake Storage Gen2 (ADLS): Central, cost-effective, and scalable storage.
   *Delta Lake (on Databricks): Transactional storage layer for reliability and ACID properties.
3.ETL & Data Transformation:
   *Databricks Structured Streaming: Real-time ETL processes.
   *Delta Live Tables for data quality and schema enforcement.
4.Analytics & Visualization:
   *Compute aggregates (moving averages, volatility) in Databricks.
   *Connect curated Delta tables to Power BI or Azure Synapse for dashboards.
5.Orchestration & CI/CD:
   *Azure Data Factory or Databricks Workflows for scheduling and orchestration.
   *GitHub Actions for CI/CD: Terraform for infra provisioning, Databricks jobs deployment, and continuous integration.
6.Security & Governance:
   *Azure RBAC for access control.
   *Databricks Secret Scopes & Azure Key Vault for secure secret management.
