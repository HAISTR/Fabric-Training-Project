[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "orders_bronze_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared orders_bronze = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "38e6df0f-a6db-4c1c-ba42-ca0fbe8846c6"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "31d49097-5988-40a5-b2af-498946cfbe3e"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "orders_bronze", ItemKind = "Table"]}[Data],
  #"Filtered rows" = Table.SelectRows(#"Navigation 2", each ([order_amount] <> null and [order_amount] <> 0)),
  #"Inserted conditional column" = Table.AddColumn(#"Filtered rows", "revenue_band", each if [order_amount] > 1000 then "High" else "Low"),
  #"Changed column type" = Table.TransformColumnTypes(#"Inserted conditional column", {{"revenue_band", type text}})
in
  #"Changed column type";
shared orders_bronze_DataDestination = let
  Pattern = Lakehouse.Contents([CreateNavigationProperties = false, EnableFolding = false, HierarchicalNavigation = true]),
  Navigation_1 = Pattern{[workspaceId = "38e6df0f-a6db-4c1c-ba42-ca0fbe8846c6"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "31d49097-5988-40a5-b2af-498946cfbe3e"]}[Data],
  Navigation_3 = Navigation_2{[Id = "dbo", ItemKind = "Schema"]}[Data],
  TableNavigation = Navigation_3{[Id = "orders_silver", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
