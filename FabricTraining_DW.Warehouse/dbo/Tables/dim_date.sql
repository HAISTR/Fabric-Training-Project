CREATE TABLE [dbo].[dim_date] (

	[Date] date NOT NULL
);


GO
ALTER TABLE [dbo].[dim_date] ADD CONSTRAINT PK_dim_date primary key NONCLUSTERED ([Date]);