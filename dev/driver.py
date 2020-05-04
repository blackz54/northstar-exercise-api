from dev.UploadTableData import DataUploadToDynamoDB

obj = DataUploadToDynamoDB('conditions.txt')
obj.UploadDataToTable()