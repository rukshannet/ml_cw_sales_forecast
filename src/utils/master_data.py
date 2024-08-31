def createMasterData(traindf,testdf):
    # Action : Save Master dataset to csv
    traindf.to_csv('processed_df_train.csv', index=False)
    testdf.to_csv('processed_df_test.csv', index=False)