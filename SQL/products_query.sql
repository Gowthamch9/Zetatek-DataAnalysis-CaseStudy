--Cleansed DIM_Products Table --
SELECT
p.ProductKey,
p.ProductAlternateKey AS ProductItemCode,
p.EnglishProductName AS [Product Name],
ps.EnglishProductSubCategoryName AS [Sub Category], --From Sub category table
pc.EnglishProductCategoryName AS [Product Category], -- from Category Table
p.Color AS [Product Color],
p.Size AS [Product Size],
p.ProductLine AS [Product Line],
p.ModelName AS [Product Model Name],
p.EnglishDescription AS [Product Description],
ISNULL (p.Status, 'Outdated') AS [Product Status]
FROM dbo.DimProduct as p
LEFT JOIN dbo.DimProductSubcategory AS ps ON ps.ProductSubcategoryKey = p.ProductSubcategoryKey
LEFT JOIN dbo.DimProductCategory AS pc ON ps.ProductCategoryKey = pc.ProductCategoryKey
order by 
p.ProductKey ASC