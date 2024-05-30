# Project Description
The company has some event data that come as JSONs, and it needs some transformations to be structured as tables. 

## Tasks
Convert the presented case.json file to three CSV files with the following rules:

### 1. CuratedOfferOptions.csv:
- CurationProvider: in quotes 
- OfferId: in quotes
- DealerId: in quotes
- UniqueOptionId: in quotes
- OptionId: in quotes
- IsMobileDealer: without quotes
- IsOpen: without quotes
- Eta: in quotes
- ChamaScore: without quotes
- ProductBrand: in quotes
- IsWinner: without quotes
- MinimumPrice: without quotes
- MaximumPrice: without quotes
- DynamicPrice: without quotes
- FinalPrice: without quotes
- DefeatPrimaryReason: in quotes
- DefeatReasons: in quotes
- EnqueuedTimeSP: DD/MM/YYYY (converted to Brasilian timezone - UTC-3)

### 2. DynamicPriceOption.csv:
- Provider: in quotes
- OfferId: in quotes
- UniqueOptionId: in quotes
- BestPrice: without quotes
- EnqueuedTimeSP: DD/MM/YYYY (converted to Brasilian timezone - UTC-3)

### 3. DynamicPriceRange.csv:
- Provider: in quotes
- OfferId: in quotes
- MinGlobal: without quotes
- MinRecommended: without quotes
- MaxRecommended: without quotes
- DifferenceMinRecommendMinTheory: without quotes
- EnqueuedTimeSP: DD/MM/YYYY (converted to Brasilian timezone - UTC-3)

