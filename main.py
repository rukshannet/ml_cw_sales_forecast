from src.data_loader import load_data
from src.utils.data_processor import DataProcessor
from src.utils.master_data import createMasterData
from pipelines.model_training import createPipeline
def main():
    #load data
    df_train, df_test = load_data()

    #run dataprocessing pipline
    processed_df_train = DataProcessor.fit_transform(df_train)
    processed_df_test = DataProcessor.fit_transform(df_test)

    #run master data creation
    createMasterData(processed_df_train,processed_df_test)

    #run model training pipline
    createPipeline()

main()

